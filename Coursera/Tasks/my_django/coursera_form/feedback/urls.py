from django.urls import path

from . import views

urlpatterns = [
    path('add', views.FeedbackCreateView.as_view(), name='feedback-create'),
    path('', views.FeedbackListView.as_view(), name='feedback-list'),
    # path('', views.SchemaView.as_view()),
    # path('', views.MarshView.as_view()),
]