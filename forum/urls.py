from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('forum/', views.CategoryList.as_view(), name='forum'),
    path('shop/', views.shop, name='shop'),
    path('<slug:slug>/', views.CategoryDetail.as_view(), name='category_detail'),
    path('<slug:category_slug>/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/add_post', views.AddPost, name='add_post'),
    path('edit/<post_id>', views.EditPost, name='edit_post'),
    path('delete/<post_id>', views.DeletePost, name='delete_post'),
    path('<slug:slug>/like', views.LikePost.as_view(), name='like_post')
]
