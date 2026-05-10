from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("electronics", "Electronics"),
        ("fashion", "Fashion"),
        ("books", "Books"),
    ]

    name = models.CharField(max_length=150)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class PricingRule(models.Model):
    RULE_TYPE_CHOICES = [
        ("percentage", "Percentage"),
        ("flat", "Flat"),
    ]

    name = models.CharField(max_length=150)
    rule_type = models.CharField(max_length=20, choices=RULE_TYPE_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    priority = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    category = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
