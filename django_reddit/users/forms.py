"""Users app forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from .models import Profile


class SignupForm(forms.Form):
    """Sign up form."""
    
    username = forms.CharField(
        min_length=3,
        max_length=50,
        widget = forms.TextInput(
            attrs={
                    'placeholder':'username',
                    'class': 'form-control',
                    'required': True
                }
            )
    )
    
    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                    'placeholder':'Password',
                    'class': 'form-control',
                    'required': True
                }
            )
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                    'placeholder':'Confirm Password',
                    'class': 'form-control',
                    'required': True
                }
            )
    )

    first_name = forms.CharField(
        min_length=2,
        max_length=60,
        widget = forms.TextInput(
            attrs={
                'placeholder':'First Name',
                'class': 'form-control',
                'required': True
            }
        )
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=60,
        widget = forms.TextInput(
            attrs={
                'placeholder':'First Name',
                'class': 'form-control',
                'required': True
            }
        )
    )

    email = forms.CharField(
        min_length=6,
        max_length=80,
        widget=forms.EmailInput(
            attrs={
                    'placeholder':'Confirm Password',
                    'class': 'form-control',
                    'required': True
                }
            )
    )

    def clean_username(self):
        """Verify if the username is unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError('Username is already in use.')

        return username

    def clean(self):
        """Verify password confirmation match"""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)

        profile.save()