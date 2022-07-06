from django.contrib import admin
from  . import models


# Register your models here.

#personladetails
class PdetailAdmin(admin.ModelAdmin):
    list_display= ('name','date_of_birth','Gender','phone_number','Email','Address','City')
admin.site.register(models.Pdetail, PdetailAdmin)


#Fileadmin
class FileAdmin(admin.ModelAdmin):
   list_display= ('Title','Document')
admin.site.register(models.Fileupload,FileAdmin)

#EMPLOYEMENT
class EmployementAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display= ('Total_Experience','Your_Designation' ,'your_organization','start_date','end_date','Describe_job_profile')
admin.site.register(models.Employement, EmployementAdmin)


#Educaiton
class EducationAdmin(admin.ModelAdmin):
    list_display=('education','passing_year','School_College','Specializaion','percentage')
admin.site.register(models.Educations, EducationAdmin)


#Skills
class SkillsetAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display= ('Tech_Skill', 'Description','Non_Tech_Skill','Description','Experience')
admin.site.register(models.Skills,SkillsetAdmin)


#Project
class ProjectAdmin(admin.ModelAdmin):
    list_display=('Project_Title','Project_Description','Project_Location','Team_Size','Team_Role','Technology_used')
admin.site.register(models.Project, ProjectAdmin)


#SOCIALPROFILE
class SocialProfileAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display= ('Social_name','Social_url','Description')
admin.site.register(models.Online_profile, SocialProfileAdmin)


#Sample Work
class SampleAdmin(admin.ModelAdmin):
    list_display=('Work_title','Work_link','Description')
admin.site.register(models.SampleWork, SampleAdmin)


#CERTIFICATION
class certificationAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display= ('certification_on','certificate_Id' ,'certificate_url')
admin.site.register(models.certification, certificationAdmin)



#DataAdmin

class DataAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display= ('d1','d2')
admin.site.register(models.data, DataAdmin)
