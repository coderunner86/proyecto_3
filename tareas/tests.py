from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Tarea

class TareaAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.lista_tareas_url = reverse('listar_tareas')
        self.crear_tarea_url = reverse('crear_tarea')
        self.tarea_valida_data = {
            'titulo': 'Tarea de prueba',
            'descripcion': 'Esta es una tarea de prueba.',
            'estado': 'pendiente'
        }
        self.tarea_invalida_data = {
            'descripcion': 'Esta es una tarea de prueba sin título.',
            'estado': 'Por hacer'
        }

    def test_listar_tareas(self):
        response = self.client.get(self.lista_tareas_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_crear_tarea(self):
        response = self.client.post(self.crear_tarea_url, self.tarea_valida_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tarea.objects.count(), 1)
        tarea = Tarea.objects.first()
        self.assertEqual(tarea.titulo, 'Tarea de prueba')
        self.assertEqual(tarea.descripcion, 'Esta es una tarea de prueba.')
        self.assertEqual(tarea.estado, 'pendiente')

    def test_crear_tarea_invalida(self):
        response = self.client.post(self.crear_tarea_url, self.tarea_invalida_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Tarea.objects.count(), 0)
