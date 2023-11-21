from django.core.exceptions import ValidationError


def validate_is_profile_servie(value):
    if not value.is_service:
        raise ValidationError(
            'Профиль не является сервисом'
        )
