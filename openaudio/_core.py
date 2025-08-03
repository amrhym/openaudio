"""
Internal core module - obfuscated implementation
"""

import base64
import importlib
import sys
from typing import Any

class _ModuleLoader:
    """Internal module loader to hide dependencies"""
    
    _modules = {}
    
    @classmethod
    def _import(cls, encoded_name: str) -> Any:
        """Import module with obfuscated name"""
        if encoded_name in cls._modules:
            return cls._modules[encoded_name]
        
        # Decode the module name
        decoded = base64.b64decode(encoded_name).decode('utf-8')
        
        try:
            if '.' in decoded:
                # Handle submodule imports
                main_module = decoded.split('.')[0]
                if main_module not in sys.modules:
                    importlib.import_module(main_module)
                module = importlib.import_module(decoded)
            else:
                module = importlib.import_module(decoded)
            
            cls._modules[encoded_name] = module
            return module
        except ImportError:
            # Fallback for nested imports
            main_parts = decoded.split('.')
            main_mod = importlib.import_module(main_parts[0])
            
            current = main_mod
            for part in main_parts[1:]:
                current = getattr(current, part)
            
            cls._modules[encoded_name] = current
            return current
    
    @classmethod
    def get_client_class(cls):
        """Get the obfuscated client class"""
        # Use __import__ with fromlist to properly import submodules
        # Z29vZ2xlLmdlbmFp = base64('google.genai')
        module_name = base64.b64decode(b'Z29vZ2xlLmdlbmFp').decode()
        parts = module_name.split('.')
        m = __import__(module_name, fromlist=[parts[-1]])
        # Q2xpZW50 = base64('Client')
        class_name = base64.b64decode(b'Q2xpZW50').decode()
        return getattr(m, class_name)
    
    @classmethod
    def get_types(cls):
        """Get the types module"""
        # Z29vZ2xlLmdlbmFpLnR5cGVz = base64('google.genai.types')
        module_name = base64.b64decode(b'Z29vZ2xlLmdlbmFpLnR5cGVz').decode()
        parts = module_name.split('.')
        return __import__(module_name, fromlist=[parts[-1]])

# Obfuscated constants using more complex encoding
_MODEL_ID = base64.b64encode(b'gemini-2.5-flash-preview-tts').decode()
_AUDIO_MOD = base64.b64encode(b'AUDIO').decode()

# Additional obfuscation layer
def _x(s):
    """Extra decode layer"""
    return ''.join(chr(ord(c) ^ 42) for c in s)

def _decode(data: str) -> str:
    """Decode obfuscated string"""
    return base64.b64decode(data).decode('utf-8')

def _get_config_builder():
    """Get configuration builder function"""
    types = _ModuleLoader.get_types()
    
    def build_config(voice_name: str):
        # Build config without exposing class names - all base64 encoded
        # R2VuZXJhdGVDb250ZW50Q29uZmln = base64('GenerateContentConfig')
        conf_class = getattr(types, base64.b64decode(b'R2VuZXJhdGVDb250ZW50Q29uZmln').decode())
        
        # U3BlZWNoQ29uZmln = base64('SpeechConfig')
        speech_conf = getattr(types, base64.b64decode(b'U3BlZWNoQ29uZmln').decode())
        
        # Vm9pY2VDb25maWc= = base64('VoiceConfig')
        voice_conf = getattr(types, base64.b64decode(b'Vm9pY2VDb25maWc=').decode())
        
        # UHJlYnVpbHRWb2ljZUNvbmZpZw== = base64('PrebuiltVoiceConfig')
        prebuilt_conf = getattr(types, base64.b64decode(b'UHJlYnVpbHRWb2ljZUNvbmZpZw==').decode())
        
        return conf_class(
            response_modalities=[_decode(_AUDIO_MOD)],
            speech_config=speech_conf(
                voice_config=voice_conf(
                    prebuilt_voice_config=prebuilt_conf(
                        voice_name=voice_name,
                    )
                )
            ),
        )
    
    return build_config

def _create_client(api_key=None):
    """Create obfuscated client instance"""
    ClientClass = _ModuleLoader.get_client_class()
    if api_key:
        return ClientClass(api_key=api_key)
    return ClientClass()

def _generate_content(client, text, voice_name, system_prompt=None):
    """Generate content with obfuscated API"""
    model = _decode(_MODEL_ID)
    
    content = text
    if system_prompt:
        content = f"{system_prompt}: {text}"
    
    config_builder = _get_config_builder()
    config = config_builder(voice_name)
    
    # Use getattr with base64 encoded names to avoid exposing API structure
    # bW9kZWxz = base64('models')
    models_attr = getattr(client, base64.b64decode(b'bW9kZWxz').decode())
    # Z2VuZXJhdGVfY29udGVudA== = base64('generate_content')
    gen_method = getattr(models_attr, base64.b64decode(b'Z2VuZXJhdGVfY29udGVudA==').decode())
    
    response = gen_method(
        model=model,
        contents=content,
        config=config
    )
    
    # Navigate response structure with obfuscated attribute names
    # Y2FuZGlkYXRlcw== = base64('candidates')
    candidates = getattr(response, base64.b64decode(b'Y2FuZGlkYXRlcw==').decode())
    # Y29udGVudA== = base64('content')
    content_obj = getattr(candidates[0], base64.b64decode(b'Y29udGVudA==').decode())
    # cGFydHM= = base64('parts')
    parts = getattr(content_obj, base64.b64decode(b'cGFydHM=').decode())
    # aW5saW5lX2RhdGE= = base64('inline_data')
    inline = getattr(parts[0], base64.b64decode(b'aW5saW5lX2RhdGE=').decode())
    # ZGF0YQ== = base64('data')
    return getattr(inline, base64.b64decode(b'ZGF0YQ==').decode())