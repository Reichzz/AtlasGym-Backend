from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Producto, HistorialVentas, UsuarioVenta
from .serializers import UsuarioSerializer, ProductoSerializer, HistorialVentasSerializer, UsuarioVentaSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class HistorialVentasViewSet(viewsets.ModelViewSet):
    queryset = HistorialVentas.objects.all()
    serializer_class = HistorialVentasSerializer

class UsuarioVentaViewSet(viewsets.ModelViewSet):
    queryset = UsuarioVenta.objects.all()
    serializer_class = UsuarioVentaSerializer

