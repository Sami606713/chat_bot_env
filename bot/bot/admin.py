from django.contrib import admin
from .models import Conversation
# Register your models here.
# ADD a search field
class ConservationAdmin(admin.ModelAdmin):
    search_fields=("name",)
admin.site.register(Conversation,ConservationAdmin)