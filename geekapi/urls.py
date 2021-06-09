from django.conf.urls import url

from geekapi import views

urlpatterns = [
    url(r"^api/person/$", views.PersonList),
   # url(r"^api/person/(?P<pk>[0-9]+)$", views.PersonDetail),
   # url(r"^api/person/email$", views.PersonEmail),



]
