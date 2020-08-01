from django import forms
from .models import UserDetails,UserImages

class RegisterForm(forms.Form):
	email=forms.EmailField(required=True)
	username=forms.CharField(max_length=50,required=True)
	password= forms.CharField(widget=forms.PasswordInput,required=True)
	confirm_password= forms.CharField(widget=forms.PasswordInput,required=True)

	
class LoginForm(forms.Form):
	username=forms.CharField(max_length=50,required=True)
	password= forms.CharField(widget=forms.PasswordInput,required=True)
	

class UserDetailsForm(forms.ModelForm):
	class Meta:
		model=UserDetails
		fields='__all__'
#class UserDetails(forms.Form):

class UserImagesForm(forms.ModelForm):
	class Meta:
		model=UserImages
		fields=('image',)