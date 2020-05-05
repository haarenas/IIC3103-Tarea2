from django.shortcuts import render
#from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.shortcuts import redirect
#from rest_framework import permissions
#from . serializers import UserSerializer, GroupSerializer
from . models import Hamburguesa, Ingrediente
from . serializers import hamburguesaSerializer, ingredienteSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

""" from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status """

class hamburgesaList(APIView):
    def get(self, request, pk=None):
        if pk:
            if pk.isdigit():
                pk = int(pk)
            else:
                return Response({'Message': 'id invalido', 'Status': 400}, status=400)
            
            if Hamburguesa.objects.filter(pk=pk).exists():
                hamburguesas = Hamburguesa.objects.get(pk=pk)
                serializer = hamburguesaSerializer(hamburguesas)
                for inx2, ingr in enumerate(serializer.data['ingredientes']):
                    serializer.data['ingredientes'][inx2] = {"path": f"https://burger-service-api.herokuapp.com/ingrediente/{ingr}"}
                return Response(serializer.data, status=200)
            else:
                return Response({'Message': f'Hamburguesa con id {pk} no existe','Status': 404}, status=404)
        else:
            hamburguesas = Hamburguesa.objects.all()
            serializer = hamburguesaSerializer(hamburguesas, many=True)
            for inx,burger in enumerate(serializer.data):
                for inx2, ingr in enumerate(burger['ingredientes']):
                    serializer.data[inx]['ingredientes'][inx2] = {"path": f"https://burger-service-api.herokuapp.com/ingrediente/{ingr}"}
            return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = hamburguesaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({'Message': 'Input invalido', 'Status': 400, 'Body': serializer.errors}, status=400)

    def delete(self, request, pk=None):
        if pk:
            if pk.isdigit():
                pk = int(pk)
            else:
                return Response({'Message': 'id invalido', 'Status': 400}, status=400)
            
            if Hamburguesa.objects.filter(pk=pk).exists():
                hamburguesas = Hamburguesa.objects.get(pk=pk)
                hamburguesas.delete()
                return Response({'Message': 'Hamburguesa eliminada', 'Status': 200}, status=200)
            else:
                return Response({'Message': 'Hamburguesa inexistente','Status': 404}, status=404)
        else:
            return Response({'Message': 'id invalido', 'Status': 400}, status=400)
        
    
    def patch(self, request, pk=None):
        if pk:
            if pk.isdigit():
                pk = int(pk)
            else:
                return Response({'Message': 'id invalido', 'Status': 400}, status=400)
            
            if Hamburguesa.objects.filter(pk=pk).exists():
                hamburguesas = Hamburguesa.objects.get(pk=pk)
                serializer = hamburguesaSerializer(hamburguesas, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    for inx2, ingr in enumerate(serializer.data['ingredientes']):
                        serializer.data['ingredientes'][inx2] = {"path": f"https://burger-service-api.herokuapp.com/ingrediente/{ingr}"}
                    return Response(serializer.data, status=200)
                else:
                    return Response({'Message': 'El parametro no se puede modificar', 'Status': 400}, status=400)
            else:
                return Response({'Message': 'Hamburguesa inexistente','Status': 404}, status=404)
            
        else:
            return Response({'Message': 'id invalido', 'Status': 400}, status=400)


class ingredienteList(APIView):
    def get(self, request, pk=None):
        if pk:
            if pk.isdigit():
                pk = int(pk)
            else:
                return Response({'Message': 'id invalido', 'Status': 400}, status=400)
            if Ingrediente.objects.filter(pk=pk).exists():
                ingredientes = Ingrediente.objects.get(pk=pk)
                serializer = ingredienteSerializer(ingredientes)
                return Response(serializer.data, status=200)
            else:
                return Response({'Message': 'Ingrediente inexistente', 'Status': 404}, status=404)
        else:
            ingredientes = Ingrediente.objects.all()
            serializer = ingredienteSerializer(ingredientes, many=True)
            return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = ingredienteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({'Message': 'Input invalido', 'Status': 400, 'Body': serializer.errors}, status=400)

    def delete(self, request, pk=None):
        if pk:
            if pk.isdigit():
                pk = int(pk)
            else:
                return Response({'Message': 'id invalido', 'Status': 400}, status=400)
            
            hamburguesas = Hamburguesa.objects.filter(ingredientes = pk)
            serializer = hamburguesaSerializer(hamburguesas, many=True)
            
            if serializer.data:
                return Response({'Message': 'Ingrediente no se puede borrar, se encuentra presente en una o mas hamburguesas', 'Status': 409}, status=409)
                
            ingrediente = Ingrediente.objects.filter(pk = pk)
            ingrediente.delete()
            return Response({'Message': 'Ingrediente eliminado', 'Status': 200}, status=200)

        else:
            return Response({'Message': 'id invalido', 'Status': 400}, status=400)
        


class hamburgesaIngrediente(APIView):
    def get(self, request, pk=None, pk2=None):
        if pk:
            if pk.isdigit():
                pk = int(pk)
            else:
                return Response({'Message': 'id invalido', 'Status': 400}, status=400)
            
            if Hamburguesa.objects.filter(pk=pk).exists():
                hamburguesas = Hamburguesa.objects.get(pk=pk)
                serializer = hamburguesaSerializer(hamburguesas)
                for inx2, ingr in enumerate(serializer.data['ingredientes']):
                    serializer.data['ingredientes'][inx2] = {"path": f"https://burger-service-api.herokuapp.com/ingrediente/{ingr}"}
                return Response(serializer.data, status=200)
            else:
                return Response({'Message': f'Hamburguesa con id {pk} no existe','Status': 404}, status=404)
        else:
            hamburguesas = Hamburguesa.objects.all()
            serializer = hamburguesaSerializer(hamburguesas, many=True)
            return Response(serializer.data, status=200)
    
    def put(self, request, pk=None, pk2=None):
        if not pk or not pk.isdigit():
            return Response({'Message': 'id de hamburguesa invalido', 'Status': 400}, status=400)

        if not pk2 or not pk2.isdigit():
            return Response({'Message': 'id de ingrediente invalido', 'Status': 400}, status=400)

        pk = int(pk)
        pk2 = int(pk2)

        if not Hamburguesa.objects.filter(pk=pk).exists():
            return Response({'Message': 'Hamburguesa inexistente','Status': 404}, status=404)

        if not Ingrediente.objects.filter(pk=pk2).exists():
            return Response({'Message': 'Ingrediente inexistente','Status': 404}, status=404)

        hamburguesa = Hamburguesa.objects.get(pk=pk)
        ingrediente = Ingrediente.objects.get(pk=pk2)

        if Hamburguesa.objects.filter(ingredientes = pk2, pk = pk):
            return Response({'Message': 'Hamburguesa ya contiene el ingrediente','Status': 400}, status=400)

        hamburguesa.ingredientes.add(ingrediente)

        hamburguesa.save()

        return Response({'Message': 'Ingrediente agregado','Status': 201}, status=201)

    def delete(self, request, pk=None, pk2=None):
        if not pk or not pk.isdigit():
            return Response({'Message': 'id de hamburguesa invalido', 'Status': 400}, status=400)

        if not pk2 or not pk2.isdigit():
            return Response({'Message': 'id de ingrediente invalido', 'Status': 400}, status=400)

        pk = int(pk)
        pk2 = int(pk2)

        if not Hamburguesa.objects.filter(pk=pk).exists():
            return Response({'Message': 'Hamburguesa inexistente','Status': 404}, status=404)

        if not Ingrediente.objects.filter(pk=pk2).exists():
            return Response({'Message': 'Ingrediente inexistente en la hamburguesa','Status': 404}, status=404)

        hamburguesa = Hamburguesa.objects.get(pk=pk)
        ingrediente = Ingrediente.objects.get(pk=pk2)
        
        if not Hamburguesa.objects.filter(ingredientes = pk2):
            return Response({'Message': 'Ingrediente inexistente en la hamburguesa','Status': 404}, status=404)

        hamburguesa.ingredientes.remove(ingrediente)

        hamburguesa.save()

        return Response({'Message': 'Ingrediente retirado','Status': 200}, status=200)



