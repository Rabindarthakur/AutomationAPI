from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import EmailField
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
#Pdetails
class Pdetail(models.Model):
    Name =models.TextField(max_length=20)
    DOB = models.DateField()
    Phone_number= models.IntegerField()
    Email= models.EmailField()
    Address=models.TextField(max_length=100)
    Town=models.TextField(max_length=50)

#class Fileupload(models.Model):
#    choose_file = models.FileField(upload_to='documents/')
#    uploaded_at = models.DateTimeField(auto_now_add=True)

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
    passing_year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
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
    Project_Lcation=models.TextField(max_length=50)
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
    Work_title=models.TextField(100)
    Work_link=models.URLField()
    Description=models.TextField(max_length=100)


#Certification
class certification(models.Model):
    certification_on=models.TextField(max_length=100)
    certificate_Id=models.IntegerField()
    certificate_url=models.URLField()



