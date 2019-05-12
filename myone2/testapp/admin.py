from django.contrib import admin
from testapp.models import jobs,hydjobs,bngljobs
# Register your models here.
class jobs_admin(admin.ModelAdmin):
    list_display=['date','company','role','addr','email']

class hydjobs_admin(admin.ModelAdmin):
    list_display=['date','company','role','addr','email','number']

class bngljobs_admin(admin.ModelAdmin):
    list_display=['date','company','role','addr','email','number']

admin.site.register(jobs,jobs_admin)
admin.site.register(hydjobs,hydjobs_admin)
admin.site.register(bngljobs,bngljobs_admin)
