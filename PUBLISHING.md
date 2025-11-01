# Publishing webl to PyPI

## One-Time Setup

1. **Create PyPI account**
   - Sign up at https://pypi.org/account/register/
   - Sign up at https://test.pypi.org/account/register/ (for testing)

2. **Install build tools**
   ```bash
   pip install build twine
   ```

3. **Create API token on PyPI**
   - Go to https://pypi.org/manage/account/token/
   - Create a new API token
   - Save it securely (you'll only see it once)

## Publishing Process

### 1. Test Build

```bash
cd webl-cli

# Clean previous builds
rm -rf build/ dist/ *.egg-info

# Build the package
python3 -m build
```

This creates:
- `dist/webl-0.1.0-py3-none-any.whl` (wheel)
- `dist/webl-0.1.0.tar.gz` (source)

### 2. Test on Test PyPI (optional but recommended)

```bash
# Upload to Test PyPI
python3 -m twine upload --repository testpypi dist/*

# Test install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ webl
```

### 3. Publish to Real PyPI

```bash
# Upload to PyPI
python3 -m twine upload dist/*
```

You'll be prompted for:
- Username: `__token__`
- Password: Your PyPI API token (starts with `pypi-`)

### 4. Verify Installation

```bash
# Install from PyPI
pip install webl

# Test it works
webl --version
webl --help
```

## Publishing Updates

1. **Update version** in `setup.py` and `webl/__init__.py`
   ```python
   version="0.1.1"  # Increment version
   ```

2. **Clean and rebuild**
   ```bash
   rm -rf build/ dist/ *.egg-info
   python3 -m build
   ```

3. **Upload new version**
   ```bash
   python3 -m twine upload dist/*
   ```

## Using .pypirc (easier authentication)

Create `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR_TOKEN_HERE

[testpypi]
username = __token__
password = pypi-YOUR_TEST_TOKEN_HERE
```

Set permissions:
```bash
chmod 600 ~/.pypirc
```

Now you can upload without entering credentials:
```bash
python3 -m twine upload dist/*
```

## Checklist Before Publishing

- [ ] Version number updated in `setup.py` and `__init__.py`
- [ ] README.md is up to date
- [ ] All tests pass
- [ ] Clean build (`rm -rf build/ dist/ *.egg-info`)
- [ ] Build package (`python3 -m build`)
- [ ] Check package (`twine check dist/*`)
- [ ] Upload to Test PyPI first
- [ ] Test install from Test PyPI
- [ ] Upload to real PyPI
- [ ] Test install from real PyPI
- [ ] Tag release in git: `git tag v0.1.0 && git push --tags`

## Quick Commands Reference

```bash
# Clean
rm -rf build/ dist/ *.egg-info

# Build
python3 -m build

# Check package
twine check dist/*

# Upload to Test PyPI
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*

# Install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ webl

# Install from PyPI
pip install webl
```

## After Publishing

Users can now install with:

```bash
pip install webl
```

Or with pipx:

```bash
pipx install webl
```

Then use:

```bash
webl github.com
```
