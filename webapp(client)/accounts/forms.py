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

	# Contact Details
	address = forms.CharField(max_length=255,error_messages=ERROR_DICT,required=False)
	city = forms.CharField(max_length=72,error_messages=ERROR_DICT,required=False)
	country = forms.CharField(max_length=72,error_messages=ERROR_DICT,required=False)
	zipcode = forms.CharField(max_length=10,error_messages=ERROR_DICT,required=False)
	email = forms.EmailField(error_messages=ERROR_DICT,required=False)

	# Identification Details
	aadhar = forms.CharField(max_length=12,error_messages=ERROR_DICT,required=False)
	pancard = forms.CharField(max_length=10,error_messages=ERROR_DICT,required=False)
	passport = forms.CharField(max_length=14,error_messages=ERROR_DICT,required=False)
	dlicense =forms.CharField(max_length=14,error_messages=ERROR_DICT,required=False)

	# Physical details
	height = forms.CharField(max_length=3,error_messages=ERROR_DICT,required=False)
	unique_feature = forms.CharField(max_length=255,error_messages=ERROR_DICT,required=False)

	# Previous records
	prev_records = forms.CharField(max_length=1000,required=False)

	
#class UserDetails(forms.Form):

class UserImagesForm(forms.ModelForm):
	class Meta:
		model=UserImages
		fields=('image',)