from django.conf.urls import url
from . import views

urlpatterns = [
    url( 'view', views.table, name='table'),
    url( 'save', views.save_order, name='save_order'),
]