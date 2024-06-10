from rest_framework import serializers
from .models import Usuario, Producto, HistorialVentas, UsuarioVenta

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class HistorialVentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialVentas
        fields = '__all__'

class UsuarioVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioVenta
        fields = '__all__'