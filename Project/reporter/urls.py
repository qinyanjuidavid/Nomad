from django.urls import path
from reporter import views
app_name='reporter'

urlpatterns=[
path('',views.Home,name='home'),
path('county/',views.County_datasets,name='county')
]
