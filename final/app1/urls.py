from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from app1 import views

urlpatterns = [

    path('voices/', views.voiceList.as_view()),

    path('voices/<int:pk>/', views.voiceDetail.as_view()),
    path('voices/musics/<msg>/', views.voiceplay),

]
