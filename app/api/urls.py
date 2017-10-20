from django.conf.urls import url
from .views import StepsCreateView, StepsDetailsView

urlpatterns = [
    url(r'^steps/$', StepsCreateView.as_view(), name='create'),
    url(r'^steps/(?P<pk>[0-9]+)/$', StepsDetailsView.as_view(), name='details'),
]
