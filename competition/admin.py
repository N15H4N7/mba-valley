from django.contrib import admin
from .models import competition, prizes, submit, register

# Register your models here.
admin.site.register(competition)
admin.site.register(prizes)
admin.site.register(submit)
admin.site.register(register)
