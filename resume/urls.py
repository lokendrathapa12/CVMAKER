from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.Profile_View.as_view(),name='profilepage'),
    path("personalform/",views.personal_View.as_view(),name='personalformpage'),
    path("resumelist/",views.Resumelist.as_view(),name='resumelistpage'),
    path("resume/<int:pk>/",views.Resumepage_View.as_view(),name='resumepage'),
    path("resumepdf/<int:pk>/",views.pdfconverter,name='resumepdfpage'),
    #path("thank/",views.thank.as_view(),name='thank'),
    #path("skill/",views.Skill_View.as_view(),name='skillformpage'),
    #path("education/",views.Education_View.as_view(),name='educationformpage'),
    #path("experience/",views.Experience_View.as_view(),name='experienceformpage'),
    #path("personaldetail/",views.PersonalDetail_View.as_view(),name='personaldetailformpage'),
    #path("declaration/",views.Declaration_View.as_view(),name='declarationpage'),
        
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)