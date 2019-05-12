import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myone2.settings')
import django
django.setup()


from faker import Faker
from random import *
from django.utils import timezone
from testapp.models import hydjobs,bngljobs

def phonenumgen():
    d=randint(7,9)
    num=str(d)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate_data(n):
    fakegen=Faker()
    for i in range(n):
        company=fakegen.company()
        role=fakegen.random_element(elements=('developer','tester','teamlead','projectmanager'))
        addr=fakegen.random_element(elements=('hyd','bnglr','pune','mumbai','noida'))
        email=fakegen.email()
        number=phonenumgen()
        hydjobs_records=hydjobs.objects.get_or_create(company=company,role=role,addr=addr,email=email,number=number)
        bngljobs_records=bngljobs.objects.get_or_create(company=company,role=role,addr=addr,email=email,number=number)


populate_data(25)
