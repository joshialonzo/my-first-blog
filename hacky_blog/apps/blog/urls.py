from django.conf.urls import url
from . import views

# https://docs.djangoproject.com/en/1.8/topics/http/urls/
urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]