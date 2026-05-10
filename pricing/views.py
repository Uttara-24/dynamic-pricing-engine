from rest_framework import generics
from .models import Product, PricingRule
from .serializers import ProductSerializer, PricingRuleSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PricingRuleListCreateView(generics.ListCreateAPIView):
    queryset = PricingRule.objects.all()
    serializer_class = PricingRuleSerializer
