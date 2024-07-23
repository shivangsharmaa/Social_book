from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('like-post', views.like_post, name='like-post'),
    path('profile/<str:pk>', views.profile, name='profile'), 
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search')
]
#user-password
""" 
1)admin-shivangadmin
2)ninad-kala
3)gourav-palti
4)yash-12
5)roy-123
6)lord_maitrey-maitrey
7)vivek-vivek 
8)shivang-shivang
9)himanshu-himanshu
"""