from django.contrib import admin
from django.urls import path, include
from . import views
from .views import MenuItemsView, SingleMenuItemView, MenuViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'menu', MenuViewSet, basename='menu')

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]
