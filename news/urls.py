from django.urls import path

from news import views


urlpatterns = [
    path('top-headlines/', views.TopNewsHeadlinesView.as_view()),
    path('search/', views.SearchArticlesView.as_view()),
]
