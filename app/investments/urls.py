from django.urls import path


from . import views


urlpatterns = [
    path('', views.InvestmentListCreateAPIView.as_view(), name='investment-list'),
    path('<int:pk>/', views.InvestmentDetailAPIView.as_view(), name='investment-detail'),
]