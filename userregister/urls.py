from django.conf.urls import url
from . import views

app_name="userregister"
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^new/$', views.new, name='new'),
	url(r'^update/$', views.update, name="update"),
	url(r'^(?P<user_id>[0-9]+)/delete/$', views.delete, name="delete"),
	url(r'^save/$', views.save, name='save'),
]