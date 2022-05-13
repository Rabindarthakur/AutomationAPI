from email.policy import default
from random import choices
from secrets import choice
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import FileExtensionValidator
from django.core.validators import RegexValidator


# Create your models here.
#Pdetails
class Pdetail(models.Model):
    name=models.TextField(max_length=255)
    date_of_birth = models.DateField()
    Sexchoice=([('Male','Male'),('Female','Femail')])
    Gender=models.TextField(choices=Sexchoice,max_length=20,blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    Email=models.EmailField()
    Address=models.TextField(max_length=255)
    City=models.TextField(max_length=255)


#FileUpload
class Fileupload(models.Model):
    Title=models.TextField(max_length=255)
    Document= models.FileField(upload_to='uploads/documents/',null=True,blank=True,validators=[FileExtensionValidator( ['pdf','.doc','docx'])])
    
  
#Employement 
class Employement(models.Model):
    Total_Experience = models.IntegerField(default=1)
    Your_Designation=models.TextField(max_length=50,default='Designation You have Worked With')
    your_organization=models.TextField(max_length=20,default='Your Orzanization name')
    start_date=models.DateField()
    end_date=models.DateField()
    Describe_job_profile=models.TextField(max_length=100, default='Explain About Your Job')
    

def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

#Education
class Educations(models.Model):
    education = models.TextField(max_length=40)
    passing_year = models.IntegerField(default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    School_College = models.TextField(max_length=100)
    Specializaion = models.TextField(max_length=100)
    percentage = models.DecimalField(max_digits=5,decimal_places=2)

#Skills
class Skills(models.Model):
    #TECH_CHOICES = [('Tech','Tech'),('Non Tech','Non Tech')]
    Non_Tech_Skill = models.TextField(max_length=100,default='') 
    Tech_Skill = models.TextField(max_length=100,default='') 
    Description = models.TextField(max_length=100,default='')
    Non_Tech_Skill = models.TextField(max_length=100,default='') 
    Description = models.TextField(max_length=100,default='')
    Experience = models.IntegerField()

    class Meta:
        verbose_name_plural = "Skills"

#Project
class Project(models.Model):
    Project_Title=models.TextField(max_length=30)
    Project_Description=models.TextField(max_length=100)
    Project_Location=models.TextField(max_length=50)
    Team_Size=models.IntegerField()
    Team_Role=models.TextField(max_length=200)
    Technology_used= models.TextField(max_length=100)

#Profile
class Online_profile(models.Model):
    Social_media = [('Facebook','Facebook'),('Instagram','Instagram'),('LinkedIn','LinkedIn'),('Github','Github')]
    Social_name=models.TextField(choices=Social_media,max_length=20,blank=True)
    Social_url= models.URLField()
    Description= models.TextField(max_length=200,default='')


#Sample Work
class SampleWork(models.Model):
    Work_title=models.TextField(max_length=100)
    Work_link=models.URLField()
    Description=models.TextField(max_length=100)


#Certification
class certification(models.Model):
    certification_on=models.TextField(max_length=100)
    certificate_Id=models.IntegerField()
    certificate_url=models.URLField()



