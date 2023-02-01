from unicodedata import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    porfolioDash,
    porfolioDetail,
    porfolioCreated,
    porfolioUpdate,
    ReportePersonasExcel,
    porfolioSearch,
    listar_cliente
)

app_name = 'porfolio'
urlpatterns = [
    path('', porfolioDash.as_view(), name='dash'),
    path('list/', listar_cliente, name='list'),
    path('<slug:pk>', porfolioDetail.as_view(), name='detail'),
    path('nuevo/', porfolioCreated.as_view(), name='new'),
    path('editar/<slug:pk>', porfolioUpdate.as_view(), name='edit'),
    path('reporte_personas_excel/',ReportePersonasExcel.as_view(), name="reporte_personas_excel"),
    path('busqueda/', porfolioSearch.as_view(), name='searchs'),

]