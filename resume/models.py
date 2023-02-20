from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cv(models.Model):

#personal fields
    image = models.ImageField(upload_to='resume/images')
    fullname = models.CharField(max_length=100)
    desiredjobtitle = models.CharField(max_length=100,default="")
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200,blank= True)
    address3 = models.CharField(max_length=200,blank= True)
    phone = models.BigIntegerField(blank=True,null=True )
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100,blank= True)

#objective field
    objective = models.CharField(max_length=10000)

#skill fields
    skill = models.CharField(max_length=1000)
    skill2 = models.CharField(max_length=1000,blank=True)
    skill3= models.CharField(max_length=1000,blank=True)
    skill4 = models.CharField(max_length=1000,blank=True)
    skill5 = models.CharField(max_length=1000,blank=True)
    skill6 = models.CharField(max_length=1000,blank=True)
    skill7 = models.CharField(max_length=1000,blank=True)
    skill8 = models.CharField(max_length=1000,blank=True)
    skill9 = models.CharField(max_length=1000,blank=True)
    skill10 = models.CharField(max_length=1000,blank=True)

#education fields
    see = models.CharField(max_length=200)
    passyear1 = models.DateField(auto_now_add=False)
    inter = models.CharField(max_length=200,blank=True)
    passyear2 = models.DateField(auto_now_add=False, null=True,blank=True)
    bachelor = models.CharField(max_length=200,blank=True)
    passyear3 = models.DateField(auto_now_add=False,null=True,blank=True)
    master = models.CharField(max_length=100,blank=True)
    passyear4 = models.DateField(auto_now_add=False,null=True,blank=True)
    phd = models.CharField(max_length=100,blank=True)
    passyear5 = models.DateField(auto_now_add=False,null=True,blank=True)
    Other = models.CharField(max_length=200,blank=True)
    passyear6 = models.DateField(auto_now_add=False,null=True,blank=True)
    
#Work experience fields
    jobtitle = models.CharField(max_length=100)
    startdate = models.DateField(auto_now_add=False,null=True,blank=True)
    enddate = models.DateField(auto_now_add=False,null=True,blank=True)
    responbility = models.CharField(max_length=1000,blank=True)
    jobtitle2 = models.CharField(max_length=100,blank=True)
    startdate2 = models.DateField(auto_now_add=False,null=True,blank=True)
    enddate2 = models.DateField(auto_now_add=False,null=True,blank=True)
    responbility2 = models.CharField(max_length=1000,blank=True)
    jobtitle3 = models.CharField(max_length=100,blank=True)
    startdate3 = models.DateField(auto_now_add=False,null=True,blank=True)
    enddate3 = models.DateField(auto_now_add=False,null=True,blank=True)
    responbility3 = models.CharField(max_length=1000,blank=True)
    
#personal detail fields
    father_name = models.CharField(max_length=100)
    mother_name= models.CharField(max_length=100)
    sex = models.CharField(max_length=50)
    Hobbies = models.CharField(max_length=300)
    nationality = models.CharField(max_length=100)
    marrital_status= models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now_add=False,default=False)


#declaration fields
    declaration = models.CharField(max_length=10000)