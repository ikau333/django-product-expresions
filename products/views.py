from django.db.models import Q, F
from .models import Product


def q_examples():
    first = Product.objects.filter(
        Q(price__gt=50) | Q(quantity__lt=10)
    )

    second = Product.objects.filter(
        Q(name__icontains="phone") & Q(price__range=(100, 500))
    )

    third = Product.objects.filter(
        ~Q(price__lt=200)
    )

    return first, second, third


def increase_prices():
    return Product.objects.update(price=F('price') + 10)


def expensive_products():
    return Product.objects.filter(price__gt=F('quantity'))


def increase_quantities():
    return Product.objects.update(quantity=F('quantity') + 1)
