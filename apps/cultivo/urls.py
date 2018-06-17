from django.conf.urls import url,include
from apps.cultivo.views import Index, Cultivo
app_name="cultivo"
urlpatterns = [
 url(r'^',Index.as_view(), name='plantilla_inicio_vacio'),
 url(r'inicio',Index.as_view(), name='plantilla_inicio'),
 url(r'cultivo',Cultivo.as_view(), name='plantilla_cultivo')
]