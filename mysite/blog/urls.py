from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'post/(?P<slug>[\w-]+)/$', views.PostDetail.as_view(), name='post_detail'),
    url('', views.PostList.as_view(), name='home')
]
