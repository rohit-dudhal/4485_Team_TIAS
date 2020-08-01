from django.template.defaultfilters import slugify
import uuid
from django.db import models
from django.contrib.auth.models import User

# Class Records(models.Model):

class UserDetails(models.Model):
	ERROR_DICT={1:'Enter Valid Information'}
	# Unique Id
	#parentUser=models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
	userID=models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
	# Name
	firstname = models.CharField(max_length=140,error_messages=ERROR_DICT,default='')
	lastname = models.CharField(max_length=140,error_messages=ERROR_DICT,default='')

	# Birth Details
	dob = models.CharField(max_length=10,help_text="Enter in DD/MM/YYYY Format",error_messages=ERROR_DICT,default='',blank=True)
	placeOfBirth = models.CharField(max_length=140,error_messages=ERROR_DICT,default='',blank=True)
	# Gender
	gender = models.CharField(max_length=7,error_messages=ERROR_DICT,default='',blank=True)

	# Contact Details
	address = models.CharField(max_length=255,error_messages=ERROR_DICT,default='',blank=True)
	city = models.CharField(max_length=72,error_messages=ERROR_DICT,default='',blank=True)
	country = models.CharField(max_length=72,error_messages=ERROR_DICT,default='',blank=True)
	zipcode = models.CharField(max_length=10,error_messages=ERROR_DICT,default='',blank=True)
	email = models.EmailField(error_messages=ERROR_DICT,default='',blank=True)

	# Identification Details
	aadhar = models.CharField(max_length=12,unique=True,error_messages=ERROR_DICT,default='',blank=True)
	pancard = models.CharField(max_length=10,unique=True,error_messages=ERROR_DICT,default='',blank=True)
	passport = models.CharField(max_length=14,unique=True,error_messages=ERROR_DICT,default='',blank=True)
	dlicense =models.CharField(max_length=14,unique=True,error_messages=ERROR_DICT,default='',blank=True)

	# Physical details
	height = models.CharField(max_length=3,error_messages=ERROR_DICT,blank=True,default='')
	unique_feature = models.TextField(max_length=255,error_messages=ERROR_DICT,blank=True,default='')

	# Previous records
	prev_records = models.CharField(max_length=1000,blank=True,default='')


	def __str__(self):
		return f'{self.firstname}-{self.lastname}-{self.userID}'


def get_image_filename(instance, filename):
    title = instance.user.firstname+'-'+instance.user.lastname
    slug = slugify(title)
    return "user_images/%s-%s" % (slug, filename) 

class UserImages(models.Model):
	user=models.ForeignKey(UserDetails,on_delete=models.CASCADE)
	image=models.ImageField(upload_to=get_image_filename, verbose_name='Image')

	def __str__(self):
		return f'{self.user.firstname}-{self.user.lastname}-{self.user.userID}'