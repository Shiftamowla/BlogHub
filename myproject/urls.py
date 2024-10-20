from django.contrib import admin
from django.urls import path
from myproject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base, name='base'),
    path('', loginpage, name='loginpage'),
    path('password_change', password_change, name='password_change'),
    path('registerpage/', registerpage, name='registerpage'),
    path('logoutpage/', logoutpage, name='logoutpage'),
    path('post/', post, name='post'),
    path('Profile/', Profile, name='Profile'),
    path('postview/<int:id>', postview, name='postview'),
    path('search/', search, name='search'),
    path('addpost/', addpost, name='addpost'),
    path('editpost/<int:id>', editpost, name='editpost'),
    path('deletepost/<int:id>', deletepost, name='deletepost'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
