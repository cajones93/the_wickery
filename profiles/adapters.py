from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError


class UsernameMaxAdapter(DefaultAccountAdapter):
    def clean_username(self, username):
        MAX_USERNAME_LENGTH = 20

        if len(username) > MAX_USERNAME_LENGTH:
            raise ValidationError(
                f'Please enter a username with less than {MAX_USERNAME_LENGTH} characters.'
            )

        return DefaultAccountAdapter.clean_username(self, username)
