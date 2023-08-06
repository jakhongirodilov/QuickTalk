from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = CustomUser
        # fields = ('username', 'email', 'phone_no', 'first_name', 'last_name', 'avatar')
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar')

    def clean(self):
        cleaned_data = super().clean()
        # Add debug statements to print the cleaned_data and errors
        print(cleaned_data)
        print(self.errors)
        return cleaned_data

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')
