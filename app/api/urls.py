from django.conf.urls import url
# from .views import StepsCreateView, StepsDetailsView
from . import views

urlpatterns = [
    url(
        r'^api/v1/steps/$',
        views.get_post_steps,
        name='get_post_steps'
    ),
    url(
        r'^api/v1/steps/(?P<pk>[0-9]+)/$',
        views.get_delete_update_step,
        name='get_delete_update_step'
    ),
]
