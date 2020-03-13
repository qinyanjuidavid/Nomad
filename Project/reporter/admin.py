from django.contrib import admin
from reporter.models import Incidence,Counties
from leaflet.admin import LeafletGeoAdmin


class IncidenceAdmin(LeafletGeoAdmin):
    search_fields=['name']
    list_display=('name','location')
admin.site.register(Incidence,IncidenceAdmin)

class CountiesAdmin(LeafletGeoAdmin):
    list_display=('name','code')

admin.site.register(Counties,CountiesAdmin)
