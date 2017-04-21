from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    # example: /polls/
    url(r'^$', views.index, name='index'),
    # example: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # example: /polls/5/results
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name='results'),
    # example: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name='vote'),
]
