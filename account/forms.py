from django import forms
from account.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.core import validators


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="گذر واژه", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="تکرار گذر واژه", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["phone", ]


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["phone", "password", "is_active", "is_admin"]




class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


    def clean_username(self):
        username = self.cleaned_data['username']

        if len(username) > 50:
            raise ValidationError(
                'Invalid username: %(value)s is invalid',
                code = 'invalid',
                params={'value': f'{username}'},
            )
        

    
class OtpLoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), validators=[validators.MaxLengthValidator(11)])

   

        
class CheckOtpCodeForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), validators=[validators.MaxLengthValidator(4)])
