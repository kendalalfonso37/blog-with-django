from django.conf.urls import url
from .views import EntradaListView, EntradaDetailView

urlpatterns = [
	url(r'^(?P<slug>[-\w]+)/$', EntradaDetailView.as_view(), name='entrada-detalle'),
	url(r'^$', EntradaListView.as_view(), name='entrada-listar'),
]