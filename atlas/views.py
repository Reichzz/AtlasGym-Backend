from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, Producto, HistorialVentas, UsuarioVenta
from .serializers import UsuarioSerializer, ProductoSerializer, HistorialVentasSerializer, UsuarioVentaSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class LoginView(APIView):
    def post(self, request):
        nombre_usuario = request.data.get('nombre_usuario')
        clave = request.data.get('clave')
        try:
            usuario = Usuario.objects.get(nombre_usuario=nombre_usuario, clave=clave)
            if usuario:
                # Devuelve la información relevante del usuario
                data = UsuarioSerializer(usuario).data
                return Response(data, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({'message': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('id_producto')
    serializer_class = ProductoSerializer

class HistorialVentasViewSet(viewsets.ModelViewSet):
    queryset = HistorialVentas.objects.all()
    serializer_class = HistorialVentasSerializer

class UsuarioVentaViewSet(viewsets.ModelViewSet):
    queryset = UsuarioVenta.objects.all()
    serializer_class = UsuarioVentaSerializer

