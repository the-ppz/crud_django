from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static 

app_name = "clientes_app"

urlpatterns = [
    path('', views.Inicio.as_view(), name='inicio'),
    path('nosotros', views.Nosotros.as_view(), name='nosotros'),
    
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
