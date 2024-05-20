from .models import Tarea
from rest_framework import viewsets, status
from .serializers import TareaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    
@api_view(['GET'])
def listar_tareas(request):
    tareas = Tarea.objects.all()
    serializer = TareaSerializer(tareas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crear_tarea_api(request):
    if request.method == 'POST':
        serializer = TareaSerializer(data=request.data)
        if serializer.is_valid():
            titulo = request.data.get('titulo')
            descripcion = request.data.get('descripcion')
            estado = request.data.get('estado')
            
            # Validacion de campos no nulos
            if not titulo or not descripcion:
                return Response({"error": "Los campos 'titulo' y 'descripcion' son obligatorios."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Validacion de campos permitidos
            ESTADOS_PERMITIDOS = ['pendiente', 'en progreso', 'completada']
            if estado and estado.lower() not in ESTADOS_PERMITIDOS:
                return Response({"error": "El campo 'estado' debe ser 'pendiente', 'en progreso' o 'completada'."}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def eliminar_tarea_api(request, tarea_id):
    try:
        tarea = Tarea.objects.get(pk=tarea_id)
    except Tarea.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    tarea.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def ver_tarea_api(request, tarea_id):
    try:
        tarea = Tarea.objects.get(pk=tarea_id)
    except Tarea.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TareaSerializer(tarea)
    return Response(serializer.data)

@api_view(['PUT'])
def editar_tarea_api(request, tarea_id):
    try:
        tarea = Tarea.objects.get(pk=tarea_id)
    except Tarea.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = TareaSerializer(tarea, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
