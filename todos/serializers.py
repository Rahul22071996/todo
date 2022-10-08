from rest_framework import serializers
from .models import *
  
class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDOWorks
        fields = ('__all__')