from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('user/', user, name='user'),
    path('page/', page, name='page'),
    path('post/', post, name='post'),
    path('song/', song, name='song'),
]
