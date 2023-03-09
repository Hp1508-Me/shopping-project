from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from rest_framework import viewsets
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer


@api_view(["GET"])
def get_available_items(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_previous_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_orders_in_duration(request, start_date, end_date):
    orders = Order.objects.filter(ordered_at__gte=start_date, ordered_at__lte=end_date)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
