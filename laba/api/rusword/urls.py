from __future__ import unicode_literals
from django.conf.urls import url
from laba.api.rusword.rusword import RusDetail, RustList

urlpatterns = [
    url(r'(?P<pk>[0-9]+)/$', RusDetail.as_view()),
    url(r'$', RusList.as_view()),
]
