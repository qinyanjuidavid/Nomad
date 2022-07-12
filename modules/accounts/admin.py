from django.contrib import admin
from modules.accounts.models import Counties, User,Nomad,Administrator
from leaflet.admin import LeafletGeoAdmin
from django.contrib.auth.models import Group


admin.site.unregister(Group)
@admin.register(Counties)
class CountiesAdmin(LeafletGeoAdmin):
    search_fields=['name']
    list_display=('name','code_id','code','area')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_admin')
    list_filter = ('is_staff', 'is_admin')
    search_fields = ('username', 'email')
    ordering = ('-id',)
    # filter_horizontal = ('is_active', 'is_staff', 'is_admin')
@admin.register(Nomad)
class NomadAdmin(LeafletGeoAdmin):
    pass

admin.site.register(Administrator)