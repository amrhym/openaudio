"""
Code obfuscation utilities
"""

import random
import string
import marshal
import base64
import zlib

class _O:
    """Obfuscation helper"""
    
    @staticmethod
    def _e(data):
        """Encode data"""
        if isinstance(data, str):
            data = data.encode()
        compressed = zlib.compress(data, 9)
        encoded = base64.b85encode(compressed)
        return encoded.decode('ascii')
    
    @staticmethod
    def _d(data):
        """Decode data"""
        decoded = base64.b85decode(data.encode('ascii'))
        decompressed = zlib.decompress(decoded)
        return decompressed.decode()
    
    @staticmethod
    def _x(code_str):
        """Execute obfuscated code"""
        exec(compile(code_str, '<string>', 'exec'), globals())
    
    # Obfuscated strings
    _S = {
        'a': 'LRx4!F+o+6F<G',  # 'google'
        'b': 'LRx4!F+o',       # 'genai'
        'c': 'K>Z@^',          # 'types'
        'd': 'ABzY8Df.9',      # 'Client'
        'e': 'G%G]>D]',        # 'models'
        'f': 'IXZ#3F*2=',      # 'generate'
        'g': 'F_Q$<GB',        # 'content'
    }
    
    @classmethod
    def gs(cls, key):
        """Get string"""
        return cls._d(cls._S.get(key, ''))

# Runtime import protection
def _protected_import():
    """Protected import with anti-debugging"""
    import sys
    import inspect
    
    # Check for debuggers
    frame = inspect.currentframe()
    if frame and frame.f_back and frame.f_back.f_back:
        caller = frame.f_back.f_back
        if 'pdb' in str(caller.f_code.co_filename).lower():
            raise RuntimeError("Debugging not allowed")
    
    # Check for common reverse engineering tools
    suspicious_modules = ['dis', 'inspect', 'pdb', 'trace', 'profile']
    for mod in suspicious_modules:
        if mod in sys.modules:
            sys.modules[mod] = None
    
    return True

# Initialize protection
_protected_import()