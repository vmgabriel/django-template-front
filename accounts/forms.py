"""Forms for user"""

# Libraries
from django import forms
from django.core.mail import send_mail
from versatileimagefield.forms import SizedImageCenterpointClickBootstrap3Field
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

# Models
from .models import User

EMAIL_CONTENT = """
Welcome to platform,

email: {email}
password: {password}

Please, change the password when you signup.
"""


class RegisterForm(forms.ModelForm):
    """Register Form"""
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "telephone")

    def save(self, commit=True):
        password = User.objects.make_random_password()
        user = super().save(commit=False)
        user.set_password(password)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.telephone = self.cleaned_data["telephone"]

        if commit:
            if settings.SEND_EMAIL:
                send_mail(
                    subject=f"Welcome to platform {user.first_name}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    message=EMAIL_CONTENT.format(email=user.email, password=password),
                    recipient_list=[user.email],
                    fail_silently=False,
                )
            user.save()
        return user


class UserForm(forms.ModelForm):
    """User Base Form Related Model"""
    # image = SizedImageCenterpointClickBootstrap3Field(required=False)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "telephone", "image"]
