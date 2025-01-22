from django.contrib import admin

from movies.models import *

# Register your models here.
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Actor)