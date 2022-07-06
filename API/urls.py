from django.urls import path
from .views  import *
from API import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [

  #Profiledetails
  path('api/users/Pdetail/post', PdetailCreate.as_view(queryset=Pdetail.objects.all(), serializer_class=Pdetailserializers), name='user-list'),
  path('api/user/Pdetail/list/',views.PdetailList.as_view(queryset=Pdetail.objects.all(), serializer_class=Pdetailserializers), name='pdetail_list'),
  path('api/user/Pdetail/update/<int:pk>',views.PdetailUpdate.as_view(queryset=Pdetail.objects.all(), serializer_class=Pdetailserializers), name='pdetail_update'),
  
  #FileField
  path('api/users/file/upload/post/',views.FileuploadCreate.as_view(), name='fileupload'),
  path('api/users/file/list/',views.FileUploadList.as_view(), name='fileList'),
  path('api/users/file/update/<int:pk>',views.FileUploadUpdate.as_view(), name='fileUpdate'),
  

  #Employement
  path('api/user/Employement/post/',views.EmployementCreate.as_view(),  name='Employement_post'),
  path('api/user/Employement/listview/',views.EmployementList.as_view(),  name='Employement_list'),
  path('api/user/Employement/update/<int:pk>',views.EmployeeUpdate.as_view(),  name='Employement_update'),
  #path('api/user/Employement/<int:pk>',views.EmployementDetail.as_view(),  name='Employement_details'),
  #path('api/user/Employement/delete/<int:pk>',views.EmployementDelete.as_view(),  name='Employement_delete'),


  #Education
  path('api/user/eduaction/post/',views.EduationCreate.as_view(), name='eduaction_post'),
  path('api/user/eduaction/list/',views.EduationList.as_view(), name='eduaction_List'),
  path('api/user/eduaction/update/<int:pk>',views.EduationUpdate.as_view(), name='eduaction_update'),

  #Skills
  path('api/user/Skills/post/',views.SkillsCreate.as_view(),  name='skill_post'),
  path('api/user/Skills/listview/',views.SkillsList.as_view(),  name='skill_list'),
  path('api/user/Skills/update/<int:pk>',views.SkillsUpdate.as_view(),  name='skill_update'),
  #path('api/user/Skills/<int:pk>',views.SkillsDetail.as_view(),  name='skills_details'),
  #path('api/user/Skills/delete/<int:pk>',views.SkillsDelete.as_view(),  name='skills_delete'),
    

  #Project
  path('api/user/project/post/',views.ProjectsCreate.as_view(), name='project_post'),
  path('api/user/project/list/',views.ProjectsList.as_view(), name='project_list'),
  path('api/user/project/update/<int:pk>',views.ProjectsUpdate.as_view(), name='project_update'),


  #Online Profiles
  path('api/user/socialprofiles/post/',views.Online_profileCreate.as_view(),  name='social_post'),
  path('api/user/socialprofiles/listview/',views.Online_profileList.as_view(),  name='social_list'),
  path('api/user/socialprofiles/update/<int:pk>',views.Online_profileUpdate.as_view(),  name='social_update'),
  #path('api/user/socialprofiles/<int:pk>',views.Online_profileDetail.as_view(),  name='social_details'),
  #path('api/user/socialprofiles/delete/<int:pk>',views.Online_profileDelete.as_view(),  name='social_delete'),


  #SampleWork
  path('api/user/samplework/post/',views.SampleCreate.as_view(), name= 'sample_post'),
  path('api/user/samplework/list/',views.SampleList.as_view(), name= 'sample_list'),
  path('api/user/samplework/update/<int:pk>',views.SampleUpdate.as_view(), name= 'sample_update'),


  #Certificaion
  path('api/user/Certificaion/post/',views.certificationCreate.as_view(),  name='certification_post'),
  path('api/user/Certificaion/listview/',views.certificationList.as_view(),  name='certification_list'),
  path('api/user/Certificaion/update/<int:pk>',views.certificationUpdate.as_view(),  name='certification_update'),
  #path('api/user/Certificaion/<int:pk>',views.certificationDetail.as_view(),  name='certification_details'),
  #path('api/user/Certificaion/delete/<int:pk>',views.certificationDelete.as_view(),  name='certification_delete',),


  #DataModel

  path('api/user/data/post/',views.dataCreate.as_view(),  name='datapost'),
  path('api/user/data/list/',views.dataList.as_view(),  name='dataList'),
  path('api/user/data/update/<int:pk>',views.dataUpdate.as_view(),  name='dataUpdate'),
    


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



