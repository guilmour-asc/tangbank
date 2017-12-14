from django.urls import include, path
from tangbank.core import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('caixa/', views.caixa, name='caixa'),
    path('conta/<pk>/', views.conta, name='conta'),
    path('teste/', views.teste, name='teste'),
]