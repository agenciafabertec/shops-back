from django.contrib import admin
from django.urls import path
from leads.views import submit_lead  # <-- importe a view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/submit/", submit_lead, name="submit_lead"),  # <-- ADICIONE ESTA LINHA
]
