from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('forum/', views.CategoryList.as_view(), name='forum'),
    path('<slug:slug>/', views.CategoryDetail.as_view(), name='category_detail'),
    path('<slug:slug>/add_post/', views.AddPost, name='add_post'),
]