

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserVerificationSerializer
from accounts.models import UserDetails,UserImages


def searchRecords(request):
	records=UserDetails.objects.all()
	name_contains=request.GET.get('name_contains')
	city_contains=request.GET.get('city_contains')

	if name_contains!='' and name_contains is not None:
		records=records.filter(firstname__icontains=name_contains)
	if city_contains!='' and city_contains is not None:
		records=records.filter(city__icontains=city_contains)

	return render(request,'searchRecords.html',{'records':records})


def recordDetails(request,userID):
	record=UserDetails.objects.get(userID=userID)
	#images=get_object_or_404(UserImages,user_id=userID)
	return render(request,'recordDetails.html',{'record':record})


class VerifyUserDetails(viewsets.ModelViewSet):
	#queryset=Chapter.objects.filter(bookName__slug__contains=slug)
	serializer_class=UserVerificationSerializer
	def get_queryset(self):
		firstname = self.request.query_params.get('firstname')
		lastname = self.request.query_params.get('lastname')
		dob = self.request.query_params.get('dob')
		placeOfBirth = self.request.query_params.get('placeOfBirth')
		gender = self.request.query_params.get('gender')
		address = self.request.query_params.get('address')
		city = self.request.query_params.get('city')
		country = self.request.query_params.get('country')
		zipcode = self.request.query_params.get('zipcode')
		email = self.request.query_params.get('email')
		aadhar = self.request.query_params.get('aadhar')
		pancard = self.request.query_params.get('pancard')
		passport = self.request.query_params.get('passport')
		dlicense = self.request.query_params.get('dlicense')
		height = self.request.query_params.get('height')
		unique_feature = self.request.query_params.get('unique_feature')
		prev_records = self.request.query_params.get('prev_records')

		queryset=UserDetails.objects.filter(firstname__exact=firstname,
											lastname__exact=lastname,
											dob__icontains=dob,
											placeOfBirth__icontains=placeOfBirth,
											gender__icontains=gender,
											address__icontains=address,
											city__icontains=city,
											country__icontains=country,
											zipcode__icontains=zipcode,
											email__icontains=email,
											aadhar__icontains=aadhar,
											pancard__icontains=pancard,
											passport__icontains=passport,
											dlicense__icontains=dlicense,
											height__icontains=height,
											unique_feature__icontains=unique_feature,
											prev_records__icontains=prev_records
											)

		return queryset
