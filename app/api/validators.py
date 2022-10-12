from rest_framework import serializers


class ValueAllowedValidator:
    """Validator that checks if a value is in an allowed array"""

    def __init__(self, allowed):
        """allowed: List of allowed values"""
        self.allowed = allowed

    def __call__(self, value):
        if value not in self.allowed:
            message = f'This field must be a value of {self.allowed}'
            raise serializers.ValidationError(message)
