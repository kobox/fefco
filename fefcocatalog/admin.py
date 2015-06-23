from django.contrib import admin

# Register your models here.
from .models import FefcoCategory

@admin.register(FefcoCategory)
class FefcoCategoryAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'slug', 'picture',)

    model = FefcoCategory