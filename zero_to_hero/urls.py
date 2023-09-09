
from django.contrib import admin
from django.urls import path
from userview.views import indexview, loginview


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",indexview),
    path("login", loginview)
]
