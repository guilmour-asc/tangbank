from django.urls import include, path, re_path
from tangbank.core import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('caixa/', views.caixa, name='caixa'),
    re_path(r'^conta/(?P<pk>\d+)/(?P<option>[a-z0-9-_/.]*)/$', views.conta, name='conta'),
    path('teste/', views.teste, name='teste'),
]