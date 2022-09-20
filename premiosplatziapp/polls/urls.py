from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # /polls/
    path("", views.IndexView.as_view(), name="index"),
    # /polls/detail/7
    path("detail/<int:pk>/", views.DetailView.as_view(), name="detail"),
    # /polls/results/7
    path("results/<int:pk>/", views.ResultsView.as_view(), name="results"),
    # /polls/vote/7
    path("vote/<int:question_id>/", views.vote, name="vote"),
]