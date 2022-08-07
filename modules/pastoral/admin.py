from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from pastoral.models import Service


@admin.register(Service)
class ServiceAdmin(LeafletGeoAdmin):
    search_fields = ["servicename"]
    list_display = ("service_name", "added_by", "location", "county", "publish")
    list_filter = ("publish", "county")
