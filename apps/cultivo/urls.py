from django.conf.urls import url,include
from apps.cultivo.views import Index
app_name="cultivo"
urlpatterns = [
 url(r'inicio',Index.as_view(), name='plantilla_inicio'),
]