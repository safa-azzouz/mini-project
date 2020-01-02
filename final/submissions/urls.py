from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from submissions import views

urlpatterns = [

    path('submissions/', views.submissionsList.as_view()),

    path('submissions/<int:pk>/', views.submissionsDetail.as_view()),


]
