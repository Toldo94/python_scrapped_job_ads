from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('python-org-ads', views.collect_ads, name='python_org_ads'),
]
