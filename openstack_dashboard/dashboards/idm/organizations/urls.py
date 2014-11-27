from django.conf.urls import patterns
from django.conf.urls import url

from openstack_dashboard.dashboards.idm.organizations import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create/$', views.CreateOrganizationView.as_view(), name='create'),
    url(r'^(?P<organization_id>[^/]+)/$', views.DetailOrganizationView.as_view(), name='detail'), 
    url(r'^(?P<organization_id>[^/]+)/edit/$', views.MultiFormView.as_view(), name='edit'), 
    url(r'^(?P<organization_id>[^/]+)/edit/info/$', views.InfoFormView.as_view(), name='info'),
    url(r'^(?P<organization_id>[^/]+)/edit/contact/$', views.ContactFormView.as_view(), name='contact'),
    url(r'^(?P<organization_id>[^/]+)/edit/avatar/$', views.AvatarFormView.as_view(), name='avatar'),
    url(r'^(?P<organization_id>[^/]+)/edit/cancel/$', views.CancelFormView.as_view(), name='cancel'),
)