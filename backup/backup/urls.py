from django.conf.urls import patterns, include, url
from django.contrib import admin
from backuptest.views import form,search,showdata, sitecrawl
from backuptest.models import post, Sitescrawled
admin.autodiscover()
admin.site.register(post)
admin.site.register(Sitescrawled)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',form),
    url(r'^update/',showdata),
    url(r'sites/',sitecrawl),
    
    
   # url(r'^$',crawledsites),
    
    url(r'^search/$',search),
)
