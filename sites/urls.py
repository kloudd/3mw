from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [

    path('sites/', views.SiteListView.as_view(), name='sites-list'),
    path('sites/<int:pk>/', views.SiteDetailView.as_view(), name='sites-detail'),
    path('summary/', views.SummaryView.as_view(), name='summary-sum'),
    path('summary-average/', views.SummaryAverageView.as_view(), name='summary-average'),
]
