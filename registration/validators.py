from rest_framework import serializers

def validate_semester(value):
      allowed = ["Spring2026", "Summer2026", "Fall2026"]
      if value not in allowed:
          raise serializers.ValidationError(f"Semester must be one of {allowed}")
      return value