from __future__ import unicode_literals
from django.conf.urls import url
from polls.api.user.user import UserDetail, UserList

urlpatterns = [
    url(r'(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'$', UserList.as_view()),
]
