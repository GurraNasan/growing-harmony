from . import views
from django.urls import path

urlpatterns = [
    path('', views.CategoriesList.as_view(), name='home')
]