from django.urls import path
from .views import MainPageView, ProfileStatsView, ProfileSearchView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('search/<str:battle_tag>/', ProfileSearchView.as_view(), name='profile_search'),
    path('search/<str:battle_tag>/stats/', ProfileStatsView.as_view(), name='profile_stats'),
]
