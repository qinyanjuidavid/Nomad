from django.db import models
from django.contrib.gis.db import models



class Incidence(models.Model):
    name=models.CharField(max_length=50)
    location=models.PointField(srid=4326)
    #objects=models.GeoManager()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='Incidences'
class Counties(models.Model):
    fid=models.FloatField()
    objectid=models.FloatField()
    code_id=models.FloatField()
    name=models.CharField(max_length=70)
    code=models.CharField(max_length=3)
    shape_leng=models.FloatField()
    shape_area=models.FloatField()
    area=models.FloatField()
    geom=models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Counties"
