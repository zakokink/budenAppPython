from django.contrib import admin
from .models import User, Uebungen, Training

admin.site.register(User)
admin.site.register(Uebungen)
admin.site.register(Training)