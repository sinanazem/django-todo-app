from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields=("email", "first_name", "last_name", "phone_number")
    
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password1"] and cd["password2"] and cd["password1"] != cd["password2"]:
            raise forms.ValidationError("passwords not match!")
        return cd["password2"]
    
    def save(self, commit=True):
        user = super().save(commit=False)
        cd = self.cleaned_data
        user.set_password(cd["password2"])
        if commit:
            user.save()
        return user
        
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="you can change password with <a href=\" ../password/ \" > this link </a>")

    class Meta:
        model = User
        fields=("email", "first_name", "last_name", "phone_number", "password", "last_login")
    

class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
