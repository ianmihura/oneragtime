from django.urls import path


from . import views


urlpatterns = [
    path('', views.CashcallListAPIView.as_view(), name='cashcall-list'),
    path('create/<int:investor_id>', views.CashcallCreateAPIView.as_view(),
         name='cashcall-create'),
    path('<int:pk>/', views.CashcallDetailAPIView.as_view(), name='cashcall-detail'),
    path('<int:pk>/status', views.CashcallStatusAPIView.as_view(),
         name='cashcall-status'),
]
