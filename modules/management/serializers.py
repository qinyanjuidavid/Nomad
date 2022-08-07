from modules.accounts import User
from modules.accounts.models import Nomad
from rest_framework.serializers import ModelSerializer
from accounts.serializers import UserSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class NomadSerializer(GeoFeatureModelSerializer):
    user = UserSerializer(read_only=True)
    geo_field = "point"

    class Meta:
        model = Nomad
        fields = (
            "id",
            "user",
            "county",
            "bio",
            "gender",
            "date_of_birth",
            "timestamp",
            "profile_picture",
            "point",
        )
