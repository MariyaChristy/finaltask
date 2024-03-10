from django.contrib import admin

# Register your models here.
from .models import CategoryMovie,Movie,Profile,MovieComment

admin.site.register(CategoryMovie)
admin.site.register(Movie)
admin.site.register(Profile)
admin.site.register(MovieComment)