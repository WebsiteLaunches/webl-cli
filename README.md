# webl - Domain Intelligence CLI

Command-line tool for domain intelligence lookups. Get WebL Site Authority, age, launch detection, and industry data directly from your terminal.

## Installation

### Quick Install (recommended)

```bash
curl -fsSL https://websitelaunches.com/install.php | bash
```

This installer will automatically:
- Detect your OS and Python version
- Choose the best installation method (Homebrew, pipx, or pip)
- Verify the installation
- Show you quick start examples

### macOS (Homebrew)

```bash
brew tap websitelaunches/tap
brew install webl
```

### pip (all platforms)

```bash
pip install webl
```

### pipx (recommended for CLI tools)

```bash
pipx install webl
```

## Quick Start

```bash
# Look up a domain (no API key needed for 3k/month)
webl github.com

# Include historical data (requires Growth+ tier)
webl github.com --history

# Output as JSON
webl github.com --json

# Output as CSV
webl github.com --csv

# For higher limits, set your API key
webl config set-key YOUR_API_KEY

# Batch lookup (requires API key)
webl batch domains.txt
```

## Free Tier (No API Key Required!)

You can use `webl` immediately without any signup:
- **3,000 requests per month** based on your IP address
- Perfect for personal use and testing
- No registration required

## Upgrade for More

Sign up for an API key to get higher limits:
- **Starter**: 50,000 requests/month + AI descriptions
- **Growth**: 250,000 requests/month + historical data + batch lookups
- **Pro**: 1,000,000 requests/month
- **Business**: 5,000,000 requests/month + custom rate limits

Get your API key at: https://websitelaunches.com/api/

## Usage

### Single Domain Lookup

```bash
webl github.com
webl stripe.com --history
webl shopify.com --json
```

Output includes:
- WebL Site Authority score (0-100)
- Domain age and registration date
- Launch detection and date
- Industry category classification
- AI-generated description

### Batch Lookup

Create a text file with one domain per line:

```
# domains.txt
github.com
stripe.com
shopify.com
```

Then run:

```bash
webl batch domains.txt
webl batch domains.txt --csv > results.csv
```

### Configuration

```bash
# Set API key
webl config set-key YOUR_API_KEY

# Show current config
webl config show

# Show config file path
webl config path
```

### Output Formats

- **Pretty** (default): Beautiful terminal output with tables
- **JSON**: Machine-readable JSON (`--json`)
- **CSV**: CSV format for spreadsheets (`--csv`)

## Environment Variables

You can also set your API key via environment variable:

```bash
export WEBL_API_KEY=your_api_key
webl github.com
```

## Examples

### Basic lookup
```bash
$ webl github.com

╭─────────────── Domain Intelligence ───────────────╮
│ Domain         github.com                         │
│ Authority      85/100                             │
│ Age            17.2 years (2007-10-01)            │
│ Launch Date    2008-04-10                         │
│ Category       Developer Tools > Code Hosting     │
│ Description    GitHub is a development platform...│
╰────────────────────────────────────────────────────╯

API Usage: 1,247/250,000 requests this month (growth tier)
```

### Historical data
```bash
$ webl github.com --history

╭─────────────── Domain Intelligence ───────────────╮
│ Domain         github.com                         │
│ Authority      85/100                             │
│ ...                                                │
╰────────────────────────────────────────────────────╯

Historical Authority:
Date      Authority  Release ID
2018-01   75         CC-MAIN-2018-05
2019-01   78         CC-MAIN-2019-04
2025-10   85         CC-MAIN-2025-40

Authority Change: +10 (+13.3%)
```

### JSON output
```bash
$ webl github.com --json | jq
{
  "ok": true,
  "data": {
    "domain": "github.com",
    "site_authority": 85,
    "domain_age": 17.2,
    ...
  }
}
```

### CSV output
```bash
$ webl github.com --csv
domain,authority,age_years,age_date,launch_detected,launch_date,category...
github.com,85,17.2,2007-10-01,true,2008-04-10,Developer Tools,...
```

### Batch processing
```bash
$ webl batch domains.txt --csv > results.csv
```

## API Tiers

- **Free**: 3,000 requests/month (no API key needed!)
- **Starter**: 50,000 requests/month + AI descriptions
- **Growth**: 250,000 requests/month + historical data + batch lookups
- **Pro**: 1,000,000 requests/month
- **Business**: 5,000,000 requests/month + custom rate limits

Historical data (`--history` flag) requires Growth tier or higher.
Batch lookups (`webl batch`) require an API key (any paid tier).

## Support

- Documentation: https://websitelaunches.com/docs
- Dashboard: https://websitelaunches.com/api/dashboard
- Issues: https://github.com/websitelaunches/webl-cli/issues

## License

MIT License - See LICENSE file for details
