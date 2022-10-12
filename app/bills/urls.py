from django.urls import path


from . import views


urlpatterns = [
    path('', views.BillListAPIView.as_view(), name='bill-list'),
    path('create-all/', views.BillCreateAPIView.as_view(), name='bill-create'),
    path('<int:pk>/', views.BillInvestorAPIView.as_view(), name='bill-investor'),
]
