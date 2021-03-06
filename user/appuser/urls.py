from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('appusers/', views.appuser_list, name='appusers-list'),
    path('appusers/<int:user_id>/', views.appuser_detail, name='appuser-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)