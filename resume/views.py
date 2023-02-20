from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,DetailView,ListView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from django import forms
from django.views import generic
from .models import Cv
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# Create your views here.
        
class Profile_View(TemplateView):
    template_name = 'resume/profile.html'

class personal_View(CreateView):
    model = Cv
    template_name = 'resume/personalform.html'
    fields = ['id','image','fullname','desiredjobtitle','address1','address2','address3',
    'phone','mobile','email','objective','skill','skill2','skill3','skill4',
    'skill5','skill6','skill7','skill8','skill9','skill10','see','passyear1',
    'inter','passyear2','bachelor','passyear3','master','passyear4','phd',
    'passyear5','Other','passyear6','jobtitle','startdate','enddate',
    'responbility','jobtitle2','startdate2','enddate2','responbility2',
    'jobtitle3','startdate3','enddate3','responbility3','father_name',
    'mother_name','sex','Hobbies','nationality','marrital_status',
    'date_of_birth','declaration']
    success_url = '/resumelist/'
    label = {'desiredjobtitle':'Job Title'}
    def get_form(self):
        form = super().get_form()
        form.fields['fullname'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['desiredjobtitle'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['address1'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['address2'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['address3'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['phone'].widget = forms.NumberInput(attrs={'class':'form-control'})
        form.fields['mobile'].widget = forms.NumberInput(attrs={'class':'form-control'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control'})


        form.fields['objective'].widget = forms.Textarea(attrs={'class':'form-control'})

        form.fields['skill'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['skill2'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['skill3'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['skill4'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['skill5'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['skill6'].widget = forms.NumberInput(attrs={'class':'form-control'})
        form.fields['skill7'].widget = forms.NumberInput(attrs={'class':'form-control'})
        form.fields['skill8'].widget = forms.EmailInput(attrs={'class':'form-control'})
        form.fields['skill9'].widget = forms.NumberInput(attrs={'class':'form-control'})
        form.fields['skill10'].widget = forms.EmailInput(attrs={'class':'form-control'})
        
        form.fields['see'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['passyear1'].widget = forms.DateInput(attrs={'class':'form-control'})
        form.fields['inter'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['passyear2'].widget = forms.DateInput(attrs={'class':'form-control'})
        form.fields['bachelor'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['passyear3'].widget = forms.DateInput(attrs={'class':'form-control'})
        form.fields['master'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['passyear4'].widget = forms.DateInput(attrs={'class':'form-control'})
        form.fields['phd'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['passyear5'].widget = forms.DateInput(attrs={'class':'form-control'})
        form.fields['Other'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['passyear6'].widget = forms.DateInput(attrs={'class':'form-control'})

        form.fields['jobtitle'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['startdate'].widget = forms.DateInput(attrs={'class':'form-control'})
        form.fields['enddate'].widget = forms.DateInput(attrs={'class':'form-control'})
        form.fields['responbility'].widget = forms.Textarea(attrs={'class':'form-control'})
        form.fields['jobtitle2'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['startdate2'].widget = forms.DateInput(attrs={'class':'form-control'})
        form.fields['enddate2'].widget = forms.DateInput(attrs={'class':'form-control'})
        form.fields['responbility2'].widget = forms.Textarea(attrs={'class':'form-control'})
        form.fields['jobtitle3'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['startdate3'].widget = forms.DateInput(attrs={'class':'form-control'})
        form.fields['enddate3'].widget = forms.DateInput(attrs={'class':'form-control'})
        form.fields['responbility3'].widget = forms.Textarea(attrs={'class':'form-control'})


        form.fields['father_name'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['mother_name'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['sex'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['Hobbies'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['nationality'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['marrital_status'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['date_of_birth'].widget = forms.DateInput(attrs={'class':'form-control'})

        form.fields['declaration'].widget = forms.Textarea(attrs={'class':'form-control'})
        return form

class Resumelist(ListView):
    model = Cv
    template_name = 'resume/resumelist.html'
    context_object_name = 'cvlist'

class Resumepage_View(DetailView):
    model = Cv
    template_name = 'resume/resumetemp1.html'
    context_object_name = 'per'

def pdfconverter(request, pk):
    per = Cv.objects.get(id=pk)
    template_path = 'resume/resumepdf.html'
    context = {'per': per}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
