from django.db import models
from django.contrib.gis.db import models as gis_models
from modules.accounts.models import TrackingModel, Administrator, Counties
from django.utils.translation import gettext as _


class Service(TrackingModel):
    service_choice = (
        ("grazing", "grazing"),
        ("borehole", "borehole"),
        ("health service", "health service"),
        ("vetinary officer", "vetinary officer"),
        ("grazing area", "grazing area"),
    )
    service_name = models.CharField(
        _("service name"), choices=service_choice, max_length=100
    )
    service_description = models.TextField(_("description"))
    added_by = models.ForeignKey(Administrator, on_delete=models.CASCADE)
    location = gis_models.MultiPolygonField(srid=4326)
    county = models.ForeignKey(Counties, on_delete=models.DO_NOTHING)
    photos = models.ImageField(null=True, upload_to="photos/")
    publish = models.BooleanField(_("publish"), default=False)

    def __str__(self):
        return f"{self.service_name}({self.county})"

    class Meta:
        verbose_name_plural = "Services"
