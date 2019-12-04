from __future__ import unicode_literals
from django.conf.urls import url
from laba.api.user.user import UserDetail, UserList, current_user

urlpatterns = [
    url(r'(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'$', UserList.as_view()),
]
