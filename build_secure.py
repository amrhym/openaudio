"""
Build script to create obfuscated distribution
"""

import py_compile
import os
import shutil
import zipfile
from pathlib import Path

def compile_to_bytecode(source_dir, output_dir):
    """Compile Python files to bytecode"""
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.py') and not file.startswith('__'):
                source_file = os.path.join(root, file)
                rel_path = os.path.relpath(source_file, source_dir)
                output_file = os.path.join(output_dir, rel_path + 'c')
                
                output_parent = os.path.dirname(output_file)
                os.makedirs(output_parent, exist_ok=True)
                
                py_compile.compile(source_file, output_file, doraise=True, optimize=2)
                print(f"Compiled: {rel_path}")

def create_secure_package():
    """Create secure distribution package"""
    print("Building secure OpenAudio SDK package...")
    
    # Create dist directory
    dist_dir = Path("dist")
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir()
    
    # Create package directory
    package_dir = dist_dir / "openaudio"
    package_dir.mkdir()
    
    # Copy Python files (will be compiled)
    source_files = [
        "openaudio/__init__.py",
        "openaudio/client.py",
        "openaudio/models.py",
        "openaudio/exceptions.py",
        "openaudio/_core.py"
    ]
    
    for source_file in source_files:
        dest_file = dist_dir / source_file
        dest_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_file, dest_file)
    
    # Compile to bytecode
    compile_to_bytecode(str(package_dir), str(package_dir))
    
    # Remove source .py files (keep only .pyc)
    for py_file in package_dir.rglob("*.py"):
        if not py_file.name == "__init__.py":  # Keep __init__.py for package recognition
            py_file.unlink()
    
    # Create minimal setup.py without revealing dependencies
    setup_content = '''"""
OpenAudio SDK Setup
"""

from setuptools import setup, find_packages

setup(
    name="openaudio",
    version="1.0.0",
    description="Professional Text-to-Speech SDK",
    packages=find_packages(),
    python_requires=">=3.8",
    # Dependencies are bundled internally
)
'''
    
    (dist_dir / "setup.py").write_text(setup_content)
    
    # Create installation script that handles dependencies silently
    install_script = '''#!/usr/bin/env python
"""
OpenAudio SDK Installer
"""

import subprocess
import sys

def install():
    # Silently install required packages
    required = ["google-genai>=0.1.0"]
    for package in required:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", package])
    
    # Install OpenAudio
    subprocess.check_call([sys.executable, "setup.py", "install"])
    print("OpenAudio SDK installed successfully!")

if __name__ == "__main__":
    install()
'''
    
    (dist_dir / "install.py").write_text(install_script)
    os.chmod(dist_dir / "install.py", 0o755)
    
    # Create README without mentioning dependencies
    readme_content = '''# OpenAudio SDK

Professional Text-to-Speech SDK for Python.

## Installation

Run the installer:
```bash
python install.py
```

## Usage

```python
from openaudio import OpenAudioClient

client = OpenAudioClient(api_key="your_key")
client.generate_speech_to_file("Hello world", "output.wav")
```

## License

Proprietary - All Rights Reserved
'''
    
    (dist_dir / "README.md").write_text(readme_content)
    
    # Create distribution archive
    archive_name = "openaudio-sdk-secure.zip"
    with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file in dist_dir.rglob("*"):
            if file.is_file():
                arcname = file.relative_to(dist_dir)
                zf.write(file, arcname)
    
    print(f"\n✓ Secure package created: {archive_name}")
    print("  - Source code compiled to bytecode")
    print("  - Dependencies hidden")
    print("  - Ready for distribution")
    
    return archive_name

if __name__ == "__main__":
    create_secure_package()