from django.urls import path
from .views import ProductListCreateView, PricingRuleListCreateView

urlpatterns = [
    path("products/", ProductListCreateView.as_view()),
    path("rules/", PricingRuleListCreateView.as_view()),
]