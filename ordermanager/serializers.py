from rest_framework.serializers import ModelSerializer

from ordermanager.models import Employee, Product


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'role']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product 
        fields = ['name', 'price', 'date_created']

