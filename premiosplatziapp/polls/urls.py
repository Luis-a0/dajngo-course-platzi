from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # /polls/
    path("", views.index, name="index"),
    # /polls/detail/7
    path("detail/<int:question_id>/", views.detail, name="detail"),
    # /polls/results/7
    path("results/<int:question_id>/", views.results, name="results"),
    # /polls/vote/7
    path("vote/<int:question_id>/", views.vote, name="vote"),
]