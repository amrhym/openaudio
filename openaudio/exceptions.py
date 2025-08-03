"""
Custom exceptions for OpenAudio SDK
"""


class OpenAudioError(Exception):
    """Base exception for OpenAudio SDK"""
    pass


class AuthenticationError(OpenAudioError):
    """Raised when authentication fails"""
    pass


class InvalidInputError(OpenAudioError):
    """Raised when invalid input is provided"""
    pass


class APIError(OpenAudioError):
    """Raised when API request fails"""
    pass