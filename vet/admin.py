from django.contrib import admin
from . import models


class VetAdminArea(admin.AdminSite):
    """Vet admin panel"""

    site_header = "Vet Site Admin Area"

vet_admin_site = VetAdminArea(name="vetAdmin")

vet_admin_site.register(models.PetOwner)
admin.site.register(models.PetOwner)