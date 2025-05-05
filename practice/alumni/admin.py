from django.contrib import admin


# Register your models here.
from .models import *
from .views import alumni_association

admin.site.register(Alumni)


@admin.register(Alumni_Association)
class Alumni_AssociationAdmin(admin.ModelAdmin):
    list_display = ('title', 'pdf_file')
    search_fields = ('title',)
    list_filter = ('title',)
