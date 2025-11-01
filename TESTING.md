# Testing webl CLI

## Local Development Testing

### Install in Development Mode

```bash
cd /home/website_launches/webl-cli
pip install -e .
```

This installs the package in "editable" mode, so changes to code are immediately reflected.

### Test Commands

```bash
# Show help
webl --help

# Show version
webl --version

# Config commands
webl config show
webl config set-key YOUR_API_KEY
webl config path

# Lookup (requires valid API key)
webl github.com
webl github.com --history
webl github.com --json
webl github.com --csv

# Batch lookup
echo -e "github.com\nstripe.com\nshopify.com" > test_domains.txt
webl batch test_domains.txt
webl batch test_domains.txt --csv
```

## Testing Before Publishing

### 1. Set API Key

Get your API key from https://websitelaunches.com/api/dashboard

```bash
webl config set-key YOUR_API_KEY
```

### 2. Test Single Lookup

```bash
webl github.com
```

Expected output:
```
╭─────────────── Domain Intelligence ───────────────╮
│ Domain         github.com                         │
│ Authority      85/100                             │
│ Age            17.2 years (2007-10-01)            │
│ Launch Date    2008-04-10                         │
│ Category       Developer Tools > Code Hosting     │
│ Description    GitHub is a development platform...│
╰────────────────────────────────────────────────────╯

API Usage: X/Y requests this month (tier)
```

### 3. Test Historical Data

```bash
webl github.com --history
```

Should show additional historical authority data and change metrics.

### 4. Test JSON Output

```bash
webl github.com --json
```

Should output valid JSON.

### 5. Test CSV Output

```bash
webl github.com --csv
```

Should output CSV format with headers.

### 6. Test Batch Lookup

Create a test file:
```bash
cat > test_domains.txt <<EOF
github.com
stripe.com
shopify.com
EOF
```

Run batch:
```bash
webl batch test_domains.txt
```

Test CSV export:
```bash
webl batch test_domains.txt --csv > results.csv
cat results.csv
```

### 7. Test Error Handling

```bash
# Test without API key
rm ~/.config/webl/config.json
webl github.com
# Should show error and instructions

# Test invalid domain
webl config set-key YOUR_API_KEY
webl invalid-domain-that-doesnt-exist.com
# Should handle gracefully

# Test batch with empty file
touch empty.txt
webl batch empty.txt
# Should show warning
```

## Manual Test Checklist

- [ ] `webl --help` shows help text
- [ ] `webl --version` shows version
- [ ] `webl config set-key KEY` saves API key
- [ ] `webl config show` displays masked key
- [ ] `webl github.com` shows pretty output
- [ ] `webl github.com --history` shows historical data (if tier supports it)
- [ ] `webl github.com --json` outputs valid JSON
- [ ] `webl github.com --csv` outputs valid CSV
- [ ] `webl batch file.txt` processes multiple domains
- [ ] `webl batch file.txt --csv` exports CSV
- [ ] Error handling works (no API key, invalid domain, etc.)
- [ ] Config file permissions are secure (600)

## Unit Tests (Future)

To add proper unit tests, create `tests/` directory:

```bash
mkdir webl-cli/tests
```

Create `tests/test_cli.py`:

```python
import pytest
from click.testing import CliRunner
from webl.cli import cli

def test_version():
    runner = CliRunner()
    result = runner.invoke(cli, ['--version'])
    assert result.exit_code == 0
    assert '0.1.0' in result.output

def test_help():
    runner = CliRunner()
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert 'Domain Intelligence CLI' in result.output

# Add more tests...
```

Run tests:
```bash
pip install pytest
pytest
```

## Integration Testing

Test the actual API integration:

```bash
# Test with real API
export WEBL_API_KEY=your_real_api_key
webl github.com

# Test rate limiting
# (Make requests until rate limit hit)

# Test different tiers
# (Test with free, starter, growth tier keys)
```

## Build Testing

Test the package build:

```bash
# Clean
rm -rf build/ dist/ *.egg-info

# Build
python3 -m build

# Check package
twine check dist/*

# Install locally from wheel
pip install dist/webl-0.1.0-py3-none-any.whl

# Test installed version
webl --version
webl --help
```

## Documentation Review

- [ ] README.md has clear installation instructions
- [ ] All examples in README work
- [ ] setup.py metadata is correct
- [ ] LICENSE file is present
- [ ] .gitignore is appropriate
