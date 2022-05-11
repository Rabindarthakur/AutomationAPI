from dataclasses import field, fields
from rest_framework import serializers
from .models import *


#Pdetails Serializers
# class Pdetailserializers(serializers.ModelSerializer):
#     class Meta:
#         model=Pdetail
#         fields='__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fileupload
        fields = "__all__"


class Employementserializers(serializers.ModelSerializer):
    class Meta:
        model = Employement
        fields = '__all__'

class Educationserializers(serializers.ModelSerializer):
    class Meta:
        model = Educations
        fields= '__all__'

class skillserializers(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class Projectserializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class profileserializers(serializers.ModelSerializer):
    class Meta:
        model = Online_profile
        fields = '__all__'

class Sampleserializers(serializers.ModelSerializer):
    class Meta:
        model = SampleWork
        fields = '__all__'

class certificateserializers(serializers.ModelSerializer):
    class Meta:
        model = certification
        fields = '__all__'

