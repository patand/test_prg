from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    
    url(r'^', include('blog.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    #url(r'^accounts/login/$', auth_views.login),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^admin/', include(admin.site.urls)),
]
