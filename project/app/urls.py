from django.contrib import admin
from django.urls import path
from .views import base
from .views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',base,name="base"),
    path('home/',home,name="home")
]
