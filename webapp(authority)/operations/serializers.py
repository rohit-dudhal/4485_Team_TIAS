from rest_framework import serializers
from accounts.models import UserDetails

class UserVerificationSerializer(serializers.ModelSerializer):
	class Meta:
		model=UserDetails
		fields=('__all__')