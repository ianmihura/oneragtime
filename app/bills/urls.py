from django.urls import path


from . import views


urlpatterns = [
    path('', views.BillListAPIView.as_view(), name='bill-list'),
    path('investor/<int:pk>/', views.BillInvetsorAPIView.as_view(), name='bill-investor-list'),
    path('<int:pk>/', views.BillDetailAPIView.as_view(), name='bill-detail'),
]