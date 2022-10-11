from django.urls import path


from . import views


urlpatterns = [
    path('', views.InvestorListCreateAPIView.as_view(), name='investor-list'),
    path('<int:pk>/', views.InvestorDetailAPIView.as_view(), name='investor-detail'),
]