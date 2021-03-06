from django.conf.urls import url
from .views import (
    workshop_list,
    workshop_details,
    workshop_create,
    WorkshopUpdate,
    WorkshopToggleActive,
    WorkshopAction,
    workshop_feedback_view,
    workshop_update_volunteer,
    workshop_accept_as_volunteer,
    workshop_opt_out_as_volunteer)


urlpatterns = [
    url(r'^$', workshop_list, name="workshop_list"),
    url(r'^(?P<pk>\d+)/$', workshop_details, name="workshop_detail"),
    url(r'^create/$', workshop_create, name="workshop_create"),
    url(r'^update/(?P<pk>\d+)/$',
        WorkshopUpdate.as_view(), name="workshop_update"),
    url(r'^(?P<pk>\d+)/(?P<action>active|deactive)/$',
        WorkshopToggleActive.as_view(), name="workshop_toggle"),
    url(r'^(?P<pk>\d+)/(?P<action>accept|reject|hold|publish|decline)/$',
        WorkshopAction.as_view(), name="workshop_action"),
    url(r'^feedback/(?P<pk>\d+)/$',
        workshop_feedback_view, name="workshop_feedback"),
    url(r'^update-volunteer/(?P<pk>\d+)$',
        workshop_update_volunteer, name="workshop_update_volunteer"),
    url(r'^workshop-opt-in-as-volunteer/(?P<pk>\d+)$',
        workshop_accept_as_volunteer, name="workshop_opt_in_volunteer"),
    url(r'^workshop-opt-out-as-volunteer/(?P<pk>\d+)$',
        workshop_opt_out_as_volunteer, name="workshop_opt_out_volunteer"),
]
