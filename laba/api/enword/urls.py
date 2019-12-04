from __future__ import unicode_literals
from django.conf.urls import url
from laba.api.enword.enword import EnDetail, EnList

urlpatterns = [
    url(r'(?P<pk>[0-9]+)/$', EnDetail.as_view()),
    url(r'$', EnList.as_view()),
]
