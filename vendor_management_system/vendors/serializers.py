# vendors/serializers.py
from rest_framework import serializers
from .models import Vendor, PurchaseOrder, HistoricalPerformance

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class HistoricalPerformanceSerializer(serializers.ModelSerializer): 
    # vendor_code = serializers.CharField(source='vendor.vendor_code')
    vendor = VendorSerializer() 
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'
