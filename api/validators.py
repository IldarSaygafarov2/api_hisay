from django.core.exceptions import ValidationError

from accounts.models import SimpleUserProfile


def validate_user_is_service(user_profile: SimpleUserProfile):
    if not user_profile.is_service:
        raise ValidationError(
            "This user profile is not a service"
        )
