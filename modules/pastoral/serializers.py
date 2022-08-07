from rest_framework.serializers import ModelSerializer
from modules.pastoral.models import Service
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class ServiceSerializer(GeoFeatureModelSerializer):
    geo_field = "location"

    class Meta:
        model = Service
        fields = (
            "id",
            "service_name",
            "service_description",
            "added_by",
            "location",
            "county",
            "photos",
            "publish",
        )
        read_only_fields = ("id",)
