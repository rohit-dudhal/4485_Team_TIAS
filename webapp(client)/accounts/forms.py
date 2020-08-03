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
	

class UserDetailsForm(forms.Form):
	ERROR_DICT={1:'Enter Valid Information'}
	# Unique Id
	#parentUser=models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
	#userID=forms.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
	# Name
	firstname = forms.CharField(max_length=140,error_messages=ERROR_DICT,required=True)
	lastname = forms.CharField(max_length=140,error_messages=ERROR_DICT,required=True)

	# Birth Details
	dob = forms.CharField(max_length=10,help_text="Enter in DD/MM/YYYY Format",error_messages=ERROR_DICT,required=False)
	placeOfBirth = forms.CharField(max_length=140,error_messages=ERROR_DICT,required=False)
	# Gender
	gender = forms.CharField(max_length=7,error_messages=ERROR_DICT,required=False)

	
#class UserDetails(forms.Form):

class UserImagesForm(forms.ModelForm):
	class Meta:
		model=UserImages
		fields=('image',)