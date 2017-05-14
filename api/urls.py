from django.conf.urls import url

from api.views import IndexView, SolversList

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^solvers/$', SolversList.as_view())
]
