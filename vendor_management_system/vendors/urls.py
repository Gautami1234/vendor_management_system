from django.urls import path
from .views import *

urlpatterns = [
    path('vendors/', VendorListCreateAPIView.as_view()),
    path('vendors/<int:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view()),
    path('purchase_orders/', PurchaseOrderListCreateAPIView.as_view()),
    path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view()),
    path('vendors/<int:pk>/performance/', VendorPerformanceRetrieveAPIView.as_view()),
]
