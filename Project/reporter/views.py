from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from reporter.models import Incidence,Counties
from django.core.serializers import serialize


def Home(request):
    context={
    }
    return render(request,'reporter/home.html',context)
def County_datasets(request):
    counties=serialize('geojson',Counties.objects.all())
    context={

    }
    return HttpResponse(counties,content_type='json')
