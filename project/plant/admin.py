from django.contrib import admin

from .models import Plant
from .models import Motor 
# Register your models here.
admin.site.register(Plant)
admin.site.register(Motor)