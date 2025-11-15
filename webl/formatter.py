"""
Output formatting for webl CLI
"""
import json
import csv
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text


console = Console()


def format_domain_data(data, format_type='pretty'):
    """
    Format domain data for display

    Args:
        data: Domain data from API
        format_type: Output format ('pretty', 'json', 'csv')
    """
    if format_type == 'json':
        print(json.dumps(data, indent=2))
        return

    if format_type == 'csv':
        output_csv(data)
        return

    # Pretty format (default)
    output_pretty(data)


def output_pretty(data):
    """Pretty formatted output using rich"""
    if not data.get('ok'):
        error = data.get('error', {})
        console.print(f"[red]Error:[/red] {error.get('message', 'Unknown error')}")
        return

    domain_data = data.get('data', {})

    # Create main info table
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Field", style="cyan", width=20)
    table.add_column("Value", style="white")

    # Add basic info
    table.add_row("Domain", domain_data.get('domain', 'N/A'))
    table.add_row("Authority", f"{domain_data.get('site_authority', 'N/A')}/100")

    age = domain_data.get('domain_age')
    age_date = domain_data.get('domain_age_date')
    if age and age_date:
        table.add_row("Age", f"{age} years ({age_date})")

    launch_detected = domain_data.get('launch_detected')
    if launch_detected:
        launch_date = domain_data.get('launch_date', 'Unknown')
        table.add_row("Launch Date", launch_date)

    category = domain_data.get('category')
    if category:
        subcats = []
        if domain_data.get('subcategory'):
            subcats.append(domain_data.get('subcategory'))
        if domain_data.get('subcategory2'):
            subcats.append(domain_data.get('subcategory2'))

        cat_str = category
        if subcats:
            cat_str += " > " + " > ".join(subcats)
        table.add_row("Category", cat_str)

    description = domain_data.get('description')
    if description:
        # Truncate long descriptions
        if len(description) > 80:
            description = description[:77] + "..."
        table.add_row("Description", description)

    # Display main table
    console.print("\n")
    console.print(Panel(table, title="[bold]Domain Intelligence[/bold]", border_style="green"))

    # Display historical data if present
    history = domain_data.get('history')
    if history:
        console.print("\n[bold cyan]Historical Authority:[/bold cyan]")

        history_table = Table(show_header=True, box=None)
        history_table.add_column("Date", style="cyan")
        history_table.add_column("Authority", style="white")
        history_table.add_column("Release ID", style="dim")

        for record in history[-5:]:  # Show last 5 records
            history_table.add_row(
                record.get('date', 'N/A'),
                str(record.get('authority', 'N/A')),
                record.get('release_id', 'N/A')
            )

        console.print(history_table)

        # Show authority change if available
        authority_change = domain_data.get('authority_change')
        if authority_change:
            abs_change = authority_change.get('absolute', 0)
            pct_change = authority_change.get('percentage', 0)

            change_color = "green" if abs_change > 0 else "red" if abs_change < 0 else "white"
            change_sign = "+" if abs_change > 0 else ""

            console.print(f"\n[{change_color}]Authority Change: {change_sign}{abs_change} ({change_sign}{pct_change:.1f}%)[/{change_color}]")

    # Display usage info
    meta = data.get('meta', {})
    usage = meta.get('usage')
    if usage:
        used = usage.get('used', 0)
        limit = usage.get('limit', 0)
        tier = meta.get('tier', 'free')

        console.print(f"\n[dim]API Usage: {used:,}/{limit:,} requests this month ({tier} tier)[/dim]")

    console.print("\n")


def output_csv(data):
    """CSV formatted output"""
    if not data.get('ok'):
        console.print("[red]Error: Cannot output error as CSV[/red]")
        sys.exit(1)

    domain_data = data.get('data', {})

    writer = csv.writer(sys.stdout)

    # Header
    writer.writerow([
        'domain',
        'authority',
        'age_years',
        'age_date',
        'launch_detected',
        'launch_date',
        'category',
        'subcategory',
        'subcategory2',
        'description'
    ])

    # Data row
    writer.writerow([
        domain_data.get('domain', ''),
        domain_data.get('site_authority', ''),
        domain_data.get('domain_age', ''),
        domain_data.get('domain_age_date', ''),
        domain_data.get('launch_detected', ''),
        domain_data.get('launch_date', ''),
        domain_data.get('category', ''),
        domain_data.get('subcategory', ''),
        domain_data.get('subcategory2', ''),
        domain_data.get('description', '')
    ])


def format_batch_data(data, format_type='pretty'):
    """Format batch lookup results"""
    if format_type == 'json':
        print(json.dumps(data, indent=2))
        return

    if format_type == 'csv':
        output_batch_csv(data)
        return

    # Pretty format
    output_batch_pretty(data)


def output_batch_pretty(data):
    """Pretty formatted batch output"""
    if not data.get('ok'):
        error = data.get('error', {})
        console.print(f"[red]Error:[/red] {error.get('message', 'Unknown error')}")
        return

    results = data.get('data', {}).get('results', [])

    if not results:
        console.print("[yellow]No results found[/yellow]")
        return

    # Create results table
    table = Table(show_header=True, box=None, padding=(0, 1))
    table.add_column("Domain", style="cyan", width=30)
    table.add_column("Authority", style="white", width=10)
    table.add_column("Age", style="white", width=12)
    table.add_column("Category", style="green", width=30)

    for result in results:
        domain = result.get('domain', 'N/A')
        authority = result.get('site_authority', 'N/A')
        age = result.get('domain_age', 'N/A')
        category = result.get('category', 'N/A')

        age_str = f"{age} years" if age != 'N/A' else 'N/A'

        table.add_row(domain, str(authority), age_str, category)

    console.print("\n")
    console.print(table)
    console.print(f"\n[dim]Total results: {len(results)}[/dim]\n")


def output_batch_csv(data):
    """CSV formatted batch output"""
    if not data.get('ok'):
        console.print("[red]Error: Cannot output error as CSV[/red]")
        sys.exit(1)

    results = data.get('data', {}).get('results', [])

    writer = csv.writer(sys.stdout)

    # Header
    writer.writerow([
        'domain',
        'authority',
        'age_years',
        'age_date',
        'launch_detected',
        'launch_date',
        'category',
        'subcategory',
        'subcategory2',
        'description'
    ])

    # Data rows
    for result in results:
        writer.writerow([
            result.get('domain', ''),
            result.get('site_authority', ''),
            result.get('domain_age', ''),
            result.get('domain_age_date', ''),
            result.get('launch_detected', ''),
            result.get('launch_date', ''),
            result.get('category', ''),
            result.get('subcategory', ''),
            result.get('subcategory2', ''),
            result.get('description', '')
        ])
