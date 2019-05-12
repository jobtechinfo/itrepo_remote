from django import forms
from testapp.models import jobs,hydjobs,bngljobs

class jobsform(forms.ModelForm):
    class Meta:
        model=jobs
        fields='__all__'
class hydjobsform(forms.ModelForm):
    class Meta:
        model=hydjobs
        fields='__all__'
class bngljobsform(forms.ModelForm):
    class Meta:
        model=bngljobs
        fields='__all__'
from django.contrib.auth.models import User
class signup_form(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password','date_joined']
