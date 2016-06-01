from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from views import main_page

urlpatterns = [
    url(r'^$', main_page),
    url(r'^main/$', views.index, name='index'),
]
