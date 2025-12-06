from . import views
from django.urls import path

urlpatterns = [
    path('post/<int:post_id>/', views.post_details, name='post_details'),
    path('user/<str:user_name>/', views.user_profile, name='user_profile'),
    path('post/<int:year>/<int:month>/', views.post_by_year, name='post_by_year'), # dynamic url by path 
    path('article/<int:year>/<int:month>/', views.article_details, name='article_details'), # dynamic url by kwargs
]