from django.conf.urls import patterns

urlpatterns = patterns('flatpage_views.views',
    (r'^list/', 'list'),                
    (r'^(?P<url>.*)$', 'flatpage'),
)