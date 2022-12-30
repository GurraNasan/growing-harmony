from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('forum/', views.CategoryList.as_view(), name='forum'),
    path('<slug:slug>/', views.CategoryDetail.as_view(), name='category_detail'),
    path('contact/', views.contact, name='contact'),
]