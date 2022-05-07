from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from search import views

urlpatterns = [
    path('api/', views.client_list), 
    path('api/<pk>/', views.client_detail)  
]

urlpatterns = format_suffix_patterns(urlpatterns)