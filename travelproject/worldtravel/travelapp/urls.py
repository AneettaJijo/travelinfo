from . import views
from django.urls import path

urlpatterns = [

    path('',views.travelling,name="travelling")
]