from django.contrib import admin
from django.urls import path, include

from search import views
from rest_framework import routers

router = routers.DefaultRouter()

# En el router vamos añadiendo los endpoints a los viewsets
router.register('peliculas', views.PeliculaViewSet)

urlpatterns = [
  path('api/v1/', include(router.urls)),
  path('admin/', admin.site.urls),
]