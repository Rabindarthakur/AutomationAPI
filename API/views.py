from http.client import responses
from urllib import response
from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAdminUser


# Create your views here.


#Profiledetails
##Create
class PdetailCreate(generics.CreateAPIView):
    queryset = Pdetail.objects.all()
    serializers_class= Pdetailserializers


#List
class PdetailList(generics.ListAPIView):
    queryset = Pdetail.objects.all()
    serializers_class= Pdetailserializers

#Update
class PdetailUpdate(generics.UpdateAPIView):
    queryset = Pdetail.objects.all()
    serializers_class= Pdetailserializers
    


#Filefield
class FileuploadCreate(generics.CreateAPIView):
    queryset = Fileupload.objects.all()
    serializer_class = FileSerializer

# Employement LIST VIEW READ
class FileUploadList(generics.ListAPIView):
    queryset = Fileupload.objects.all()
    serializer_class = FileSerializer

class FileUploadUpdate(generics.UpdateAPIView):
    queryset = Fileupload.objects.all()
    serializer_class = FileSerializer

# #ListView
# class PdetailList(generics.ListAPIView):
#     queryset = Pdetail.objects.all()
#     serializer_class = Pdetailserializers

# #Update
# class PdetailUpdate(generics.UpdateAPIView):
#     queryset = Pdetail.objects.all()
#     serializer_class = Pdetailserializers


#Employement
#Employement CREATE POST 
class EmployementCreate(generics.ListCreateAPIView):
    queryset = Employement.objects.all()
    serializer_class = Employementserializers

# Employement LIST VIEW READ
class EmployementList(generics.ListAPIView):
    queryset = Employement.objects.all()
    serializer_class = Employementserializers

class EmployeeUpdate(generics.UpdateAPIView):
    queryset = Employement.objects.all()
    serializer_class = Employementserializers

#Employement DETAILS
# ##class EmployementDetail(generics.RetrieveDestroyAPIView):
# ##    queryset = Employement.objects.all()
# ##    serializer_class = Employementserializers

# Employement DELETE 
# ##class EmployementDelete(generics.DestroyAPIView):
# ##    queryset = Employement.objects.all()
# ##    serializer_class = Employementserializers


#Education
#Post
class EduationCreate(generics.ListCreateAPIView):
    queryset=Educations.objects.all()
    serializer_class=Educationserializers

#ListView
class EduationList(generics.ListAPIView):
    queryset=Educations.objects.all()
    serializer_class=Educationserializers

#Update
class EduationUpdate(generics.UpdateAPIView):
    queryset=Educations.objects.all()
    serializer_class=Educationserializers


#SKILLS
#SKILLS CREATE POST 
class SkillsCreate(generics.ListCreateAPIView):
    queryset = Skills.objects.all()
    serializer_class = skillserializers

# SKILLS LIST VIEW READ
class SkillsList(generics.ListAPIView):
    queryset = Skills.objects.all()
    serializer_class = skillserializers


class SkillsUpdate(generics.UpdateAPIView):
    queryset = Skills.objects.all()
    serializer_class = skillserializers

#DETAILS
#class SkillsDetail(generics.RetrieveDestroyAPIView):
#    queryset = Skills.objects.all()
#    serializer_class = skillserializers#
#
#DELETE 
#class SkillsDelete(generics.DestroyAPIView):
#    queryset = Skills.objects.all()
#    serializer_class = skillserializers


#Projects
#Post
class ProjectsCreate(generics.ListCreateAPIView):
    queryset=Project.objects.all()
    serializer_class=Projectserializers

#ListView
class ProjectsList(generics.ListAPIView):
    queryset=Project.objects.all()
    serializer_class=Projectserializers

#Update
class ProjectsUpdate(generics.UpdateAPIView):
    queryset=Project.objects.all()
    serializer_class=Projectserializers


#SocialProfile
#Online_profile CREATE POST 
class Online_profileCreate(generics.ListCreateAPIView):
    queryset = Online_profile.objects.all()
    serializer_class = profileserializers

# Online_profile LIST VIEW READ
class Online_profileList(generics.ListAPIView):
    queryset = Online_profile.objects.all()
    serializer_class = profileserializers

#Online Social Profile
class Online_profileUpdate(generics.UpdateAPIView):
    queryset = Online_profile.objects.all()
    serializer_class = profileserializers

#Online_profile DETAILS
#class Online_profileDetail(generics.RetrieveDestroyAPIView):
#    queryset = Online_profile.objects.all()
#    serializer_class = profileserializers

#Online_profile DELETE 
#class Online_profileDelete(generics.DestroyAPIView):
#    queryset = Online_profile.objects.all()
#    serializer_class = profileserializers


#SampleWork
#Post
class SampleCreate(generics.CreateAPIView):
    queryset = SampleWork.objects.all()
    serializer_class = Sampleserializers


#ListView
class SampleList(generics.ListAPIView):
    queryset = SampleWork.objects.all()
    serializer_class = Sampleserializers

#Post
class SampleUpdate(generics.UpdateAPIView):
    queryset = SampleWork.objects.all()
    serializer_class = Sampleserializers


#certification
#certification CREATE POST 
class certificationCreate(generics.ListCreateAPIView):
    queryset = certification.objects.all()
    serializer_class = certificateserializers

# certification LIST VIEW READ
class certificationList(generics.ListAPIView):
    queryset = certification.objects.all()
    serializer_class = certificateserializers

#Certification Update
class certificationUpdate(generics.UpdateAPIView):
    queryset = certification.objects.all()
    serializer_class = certificateserializers

#certification DETAILS
##class certificationDetail(generics.RetrieveDestroyAPIView):
##    queryset = certification.objects.all()
##    serializer_class = certificateserializers

#certification DELETE 
##class certificationDelete(generics.DestroyAPIView):
##    queryset = certification.objects.all()
##    serializer_class = certificateserializers



