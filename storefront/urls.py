from django.contrib import admin
from django.urls import path, include
from playapp import views   #  import your views properly
import debug_toolbar
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('__debug__/', include(debug_toolbar.urls)),
]


