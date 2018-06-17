from django.conf.urls import url,include
from apps.cosecha.views import Cosecha
app_name="cosecha"
urlpatterns = [
 url(r'cosecha',Cosecha.as_view(), name='plantilla_cosecha')
]