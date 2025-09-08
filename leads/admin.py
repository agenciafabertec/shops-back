from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "ts", "ip")
    search_fields = ("name", "email", "phone", "ip")
    list_filter = ("ts",)
