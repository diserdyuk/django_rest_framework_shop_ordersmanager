from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from ordermanager.models import Employee, Product, Order, Receipt
from ordermanager.serializers import EmployeeSerializer, ProductSerializer


def order_manager(request):
    return render(request, 'index.html', {'employee': Employee.objects.all()})


class EmployeeView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def order_app(request):
    return render(request, 'main_app.html')
    

