#!/usr/bin/env python
"""
Build script for PyPI distribution
"""

import os
import sys
import shutil
import subprocess

def clean_build():
    """Remove build artifacts"""
    dirs_to_remove = ['build', 'dist', '*.egg-info', '__pycache__']
    for pattern in dirs_to_remove:
        for item in ['build', 'dist', 'openaudio.egg-info']:
            if os.path.exists(item):
                print(f"Removing {item}...")
                shutil.rmtree(item)

def build_package():
    """Build the distribution packages"""
    print("Building distribution packages...")
    
    # Install build tools if needed
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'build'])
    
    # Build the package
    subprocess.check_call([sys.executable, '-m', 'build'])
    
    print("\nPackage built successfully!")
    print("Distribution files created in 'dist/' directory:")
    for file in os.listdir('dist'):
        print(f"  - {file}")

def prepare_upload():
    """Prepare for PyPI upload"""
    print("\n" + "="*50)
    print("Package is ready for PyPI upload!")
    print("="*50)
    print("\nTo upload to PyPI, you need to:")
    print("\n1. Install twine (if not already installed):")
    print("   pip install twine")
    
    print("\n2. Create a PyPI account at https://pypi.org/account/register/")
    
    print("\n3. Create an API token at https://pypi.org/manage/account/token/")
    
    print("\n4. Test upload to TestPyPI first (optional but recommended):")
    print("   python -m twine upload --repository testpypi dist/*")
    
    print("\n5. Upload to PyPI:")
    print("   python -m twine upload dist/*")
    
    print("\n6. After upload, users can install with:")
    print("   pip install openaudio")
    
    print("\nNOTE: When prompted for username, use '__token__'")
    print("      For password, use your PyPI API token (including 'pypi-' prefix)")

if __name__ == "__main__":
    print("Building OpenAudio SDK for PyPI distribution...")
    print("-" * 50)
    
    # Clean previous builds
    clean_build()
    
    # Build the package
    build_package()
    
    # Show upload instructions
    prepare_upload()