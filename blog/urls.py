"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import registration, activation, user_login, user_logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('registration/', registration, name='registration'),
    path('login/', user_login , name='login'),
    path('logout/', user_logout , name='logout'),
    path('activation/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activation, name='activate'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


