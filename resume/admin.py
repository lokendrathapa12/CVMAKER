from django.contrib import admin
from .models import Cv
# Register your models here.

@admin.register(Cv)
class Personal_AdminModel(admin.ModelAdmin):
    list_display = ['id','image','fullname','jobtitle','address1','address2','address3','phone','mobile','email','objective','skill','skill2','skill3','skill4','skill5','skill6','skill7','skill8','skill9','skill10','see','passyear1','inter','passyear2','bachelor','passyear3','master','passyear4','phd','passyear5','Other','passyear6','jobtitle','startdate','enddate','responbility','jobtitle2','startdate2','enddate2','responbility2','jobtitle3','startdate3','enddate3','responbility3','father_name','mother_name','sex','Hobbies','nationality','marrital_status','date_of_birth','declaration']
