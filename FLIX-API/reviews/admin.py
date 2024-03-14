from django.contrib import admin
from reviews.models import Review

@admin.register(Review)

class Reviewadmin(admin.ModelAdmin):
    list_display=('id','movie','stars','comment')
