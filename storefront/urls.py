from django.contrib import admin
from django.urls import path, include
from playapp import views   #  import your views properly
import debug_toolbar
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('', include('playapp.urls')),  # connect playapp
    path("buy/<int:shoe_id>/", views.buy_shoe, name="buy"),
    path('order/<int:product_id>/', views.order_view, name='order_view'),
]

# ✅ This part registers the Django Debug Toolbar URLs correctly
if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns += [
            path('__debug__/', include('debug_toolbar.urls')),
        ]
    except ImportError:
        pass
    
