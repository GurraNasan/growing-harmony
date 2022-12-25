from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('forum/', views.CategoriesList.as_view(), name='forum'),
    path('contact', views.contact, name='contact')
]