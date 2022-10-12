from rest_framework import serializers


class ValueAllowedValidator:
    """
    Checks if value is one of allowed values
    """

    def __init__(self, allowed):
        """
        self.allowed: List of allowed values
        """
        self.allowed = allowed

    def __call__(self, value):
        if value not in self.allowed:
            message = f'This field must be a value of {self.allowed}'
            raise serializers.ValidationError(message)
