from unicodedata import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    porfolioDash,
    porfolioList,
    porfolioDetail,
    porfolioCreated,
    porfolioUpdate,
    porfolioDetele,
    ReportePersonasExcel,
    porfolioSearch
)

app_name = 'porfolio'
urlpatterns = [
    path('', porfolioDash.as_view(template_name = 'cliente_dash.html'), name='dash'),
    path('list/', porfolioList.as_view(), name='list'),
    path('(?P<pk>\d+)', porfolioDetail.as_view(), name='detail'),
    path('nuevo/', porfolioCreated.as_view(), name='new'),
    path('editar/(?P<pk>\d+)', porfolioUpdate.as_view(), name='edit'),
    path('borrar/(?P<pk>\d+)', porfolioDetele.as_view(), name='delete'),
    path('reporte_personas_excel/',ReportePersonasExcel.as_view(), name="reporte_personas_excel"),
    path('busqueda/', porfolioSearch.as_view(template_name = 'client_search.html'), name='search'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)