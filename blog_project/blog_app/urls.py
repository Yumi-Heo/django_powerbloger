from django.urls import path
from . import views


urlpatterns = [
    path('', views.board, name='board'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('write/', views.write, name='write'),
    path('post/<int:post_id>/', views.post, name='post'), 
    path('find_password/', views.find_password, name='find_password'),
    path('new_password/', views.new_password, name='new_password'),
    path('search/', views.search_view, name='search'),
    path('save_temporary_post/', views.save_temporary_post, name='save_temporary_post'),
    path('temporary_posts/', views.temporary_posts, name='temporary_posts'),
    path('load_temporary_post/<int:temp_post_id>/', views.load_temporary_post, name='load_temporary_post'),
]
