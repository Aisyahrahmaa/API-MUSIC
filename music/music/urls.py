from django.contrib import admin
from django.urls import path, include
from rest_framework import routers 
from api import views

router = routers.DefaultRouter()
router.register(r'album', views.AlbumViewSet)
router.register(r'song', views.SongViewSet)
router.register(r'review',views.ReviewViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('admin/', admin.site.urls),
    
]
