from django.contrib import admin
from .models import Enquiry
@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('created_at','name','organisation','email','topic')
    list_filter = ('topic','created_at')
    search_fields = ('name','organisation','email','message')
    readonly_fields = ('created_at',)
