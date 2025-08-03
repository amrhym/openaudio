# PyPI Upload Guide for OpenAudio SDK

## Prerequisites

1. **Create PyPI Account**
   - Go to https://pypi.org/account/register/
   - Verify your email

2. **Create API Token**
   - Log in to PyPI
   - Go to https://pypi.org/manage/account/token/
   - Create a new API token with scope "Entire account" or project-specific
   - Save the token securely (starts with `pypi-`)

## Installation

```bash
# Install twine for uploading
pip install twine
```

## Upload Process

### Option 1: Test Upload (Recommended First)

1. Create TestPyPI account at https://test.pypi.org/account/register/
2. Create API token at https://test.pypi.org/manage/account/token/
3. Upload to TestPyPI:

```bash
python -m twine upload --repository testpypi dist/*
```

When prompted:
- Username: `__token__`
- Password: Your TestPyPI token (including `pypi-` prefix)

4. Test installation from TestPyPI:
```bash
pip install --index-url https://test.pypi.org/simple/ openaudio
```

### Option 2: Direct Upload to PyPI

```bash
python -m twine upload dist/*
```

When prompted:
- Username: `__token__`
- Password: Your PyPI token (including `pypi-` prefix)

## After Upload

Once uploaded, users can install with:
```bash
pip install openaudio
```

## Updating the Package

1. Update version in `pyproject.toml` and `setup.py`
2. Clean old builds: `rm -rf dist/ build/ *.egg-info`
3. Rebuild: `python build_for_pypi.py`
4. Upload new version: `python -m twine upload dist/*`

## Security Note

- Never commit your PyPI tokens to git
- Use environment variables or `.pypirc` file (not in repo)
- Keep the dependency installation mechanism obfuscated

## Package Contents

The uploaded package includes:
- `openaudio/` - Main package with obfuscated implementation
- `README.md` - Documentation
- `LICENSE` - MIT License
- Hidden dependency installation via setup.py

## Verification

After upload, verify at:
- https://pypi.org/project/openaudio/

The package will automatically install required dependencies silently during installation.