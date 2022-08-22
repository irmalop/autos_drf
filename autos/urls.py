from django.urls import path
from .views import MarcaCreateAPIView, MarcaListAPIView, AutoCreateAPIView, AutoListAPIView
urlpatterns = [
    path('marcas/create/', MarcaCreateAPIView.as_view(), name = 'create-marcas'),
    path('marcas/list/', MarcaListAPIView.as_view(), name = 'list-marcas'),
    path('autos/create/', AutoCreateAPIView.as_view(), name = 'create-autos'),
    path('autos/list/', AutoListAPIView.as_view(), name = 'list-autos'),
]