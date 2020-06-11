from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='index'),
    # path(r'^$', views.index, name='index'),
    path(r'topics/', views.topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # edit
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]

app_name = 'learning_logs'

