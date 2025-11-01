"""
Main CLI interface for webl
"""
import click
import sys
from pathlib import Path

from .config import Config
from .client import WeblAPIClient, APIError
from .formatter import format_domain_data, format_batch_data, console


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """
    webl - Domain Intelligence CLI

    Get domain authority, age, launch detection, and industry data
    from the command line.

    \b
    Examples:
        webl github.com
        webl github.com --history
        webl github.com --json
        webl batch domains.txt
        webl config set-key YOUR_API_KEY

    \b
    No API key needed! You get 3,000 free requests per month.
    Sign up for more at: https://websitelaunches.com/api/
    """
    pass


@cli.command()
@click.argument('domain')
@click.option('--history', is_flag=True, help='Include historical authority data (Growth+ tiers)')
@click.option('--json', 'output_json', is_flag=True, help='Output as JSON')
@click.option('--csv', 'output_csv', is_flag=True, help='Output as CSV')
def lookup(domain, history, output_json, output_csv):
    """
    Look up domain intelligence

    DOMAIN: Domain name to lookup (e.g., github.com)

    \b
    Examples:
        webl github.com
        webl github.com --history
        webl github.com --json
        webl github.com --csv

    \b
    Note: API key is optional. Without a key, you get 3,000 requests/month
    based on your IP address. Sign up for a key to get higher limits.
    """
    config = Config()
    api_key = config.get_api_key()

    # API key is now optional - will use IP-based rate limiting if not provided

    # Determine output format
    format_type = 'pretty'
    if output_json:
        format_type = 'json'
    elif output_csv:
        format_type = 'csv'

    try:
        client = WeblAPIClient(api_key) if api_key else WeblAPIClient(None)
        data = client.lookup_domain(domain, history=history)
        format_domain_data(data, format_type)
    except APIError as e:
        console.print(f"[red]Error:[/red] {str(e)}")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]Unexpected error:[/red] {str(e)}")
        sys.exit(1)


# Allow direct domain lookup without 'lookup' subcommand
@cli.command(name='domain', hidden=True)
@click.argument('domain')
@click.option('--history', is_flag=True, help='Include historical authority data')
@click.option('--json', 'output_json', is_flag=True, help='Output as JSON')
@click.option('--csv', 'output_csv', is_flag=True, help='Output as CSV')
def domain_shortcut(domain, history, output_json, output_csv):
    """Shortcut for domain lookup (hidden command)"""
    # Just call the lookup command
    ctx = click.get_current_context()
    ctx.invoke(lookup, domain=domain, history=history, output_json=output_json, output_csv=output_csv)


@cli.command()
@click.argument('file', type=click.Path(exists=True))
@click.option('--history', is_flag=True, help='Include historical authority data (Growth+ tiers)')
@click.option('--json', 'output_json', is_flag=True, help='Output as JSON')
@click.option('--csv', 'output_csv', is_flag=True, help='Output as CSV')
def batch(file, history, output_json, output_csv):
    """
    Batch lookup multiple domains from a file

    FILE: Text file with one domain per line

    \b
    Examples:
        webl batch domains.txt
        webl batch domains.txt --json
        webl batch domains.txt --csv > results.csv

    \b
    Note: Batch lookups require an API key. Sign up at:
    https://websitelaunches.com/api/
    """
    config = Config()
    api_key = config.get_api_key()

    if not api_key:
        console.print("[red]Error:[/red] Batch lookups require an API key.")
        console.print("\nRun: [cyan]webl config set-key YOUR_API_KEY[/cyan]")
        console.print("Sign up at: [cyan]https://websitelaunches.com/api/[/cyan]")
        sys.exit(1)

    # Read domains from file
    try:
        with open(file, 'r') as f:
            domains = [line.strip() for line in f if line.strip()]
    except IOError as e:
        console.print(f"[red]Error reading file:[/red] {str(e)}")
        sys.exit(1)

    if not domains:
        console.print("[yellow]Warning:[/yellow] No domains found in file")
        sys.exit(0)

    # Determine output format
    format_type = 'pretty'
    if output_json:
        format_type = 'json'
    elif output_csv:
        format_type = 'csv'

    try:
        client = WeblAPIClient(api_key)
        data = client.batch_lookup(domains, history=history)
        format_batch_data(data, format_type)
    except APIError as e:
        console.print(f"[red]Error:[/red] {str(e)}")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]Unexpected error:[/red] {str(e)}")
        sys.exit(1)


@cli.group()
def config():
    """Manage webl configuration"""
    pass


@config.command(name='set-key')
@click.argument('api_key')
def set_key(api_key):
    """
    Set your API key

    API_KEY: Your Website Launches API key

    \b
    Example:
        webl config set-key wl_abc123...

    \b
    Get your API key at: https://websitelaunches.com/api/dashboard
    """
    cfg = Config()
    cfg.set_api_key(api_key)
    console.print("[green]✓[/green] API key saved successfully!")
    console.print(f"\nConfig file: [dim]{cfg.get_config_path()}[/dim]")


@config.command(name='show')
def show_config():
    """Show current configuration"""
    cfg = Config()
    api_key = cfg.get_api_key()

    if api_key:
        # Mask the API key for security
        masked = api_key[:7] + '...' + api_key[-4:] if len(api_key) > 11 else '***'
        console.print(f"API Key: [cyan]{masked}[/cyan]")
        console.print(f"Config file: [dim]{cfg.get_config_path()}[/dim]")
    else:
        console.print("[yellow]No API key configured[/yellow]")
        console.print("\nRun: [cyan]webl config set-key YOUR_API_KEY[/cyan]")
        console.print("Get your API key at: [cyan]https://websitelaunches.com/api/dashboard[/cyan]")


@config.command(name='path')
def show_path():
    """Show path to config file"""
    cfg = Config()
    console.print(cfg.get_config_path())


# Make it so `webl github.com` works without subcommand
@cli.command(context_settings=dict(ignore_unknown_options=True, allow_extra_args=True), hidden=True)
@click.argument('args', nargs=-1)
@click.pass_context
def default(ctx, args):
    """Hidden default handler for direct domain lookup"""
    if not args:
        # No arguments, show help
        click.echo(ctx.parent.get_help())
        return

    # First arg should be domain
    domain = args[0]

    # Parse options
    history = '--history' in args
    output_json = '--json' in args
    output_csv = '--csv' in args

    ctx.invoke(lookup, domain=domain, history=history, output_json=output_json, output_csv=output_csv)


def main():
    """Entry point for the CLI"""
    # Allow direct domain lookup: `webl github.com`
    # If first arg doesn't match a subcommand and looks like a domain, treat it as lookup
    if len(sys.argv) > 1:
        first_arg = sys.argv[1]
        subcommands = ['lookup', 'batch', 'config', '--help', '-h', '--version', '-V']

        # If first arg is not a known subcommand and contains a dot (likely a domain)
        if first_arg not in subcommands and '.' in first_arg and not first_arg.startswith('-'):
            # Insert 'lookup' command
            sys.argv.insert(1, 'lookup')

    cli()


if __name__ == '__main__':
    main()
