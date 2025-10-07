from django.db import models
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(default=timezone.now)

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    colaboradores = models.ManyToManyField(Usuario, related_name='proyectos_asignados')
    creador = models.ForeignKey(Usuario, related_name='proyectos_creados', on_delete=models.CASCADE, null=True)

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

class Tarea(models.Model):
    ESTADO_OPCIONES = [
        ('pen', 'Pendiente'),
        ('pro', 'Progreso'),
        ('com', 'Completada') 
    ]
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO_OPCIONES, default='pen')
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateField()
    hora_vencimiento = models.TimeField()
    creador = models.ForeignKey(Usuario, related_name='tareas_creadas', on_delete=models.CASCADE, null=True)
    proyecto = models.ForeignKey(Proyecto, related_name='tareas', on_delete=models.CASCADE, null=True)
    etiquetas = models.ManyToManyField(Etiqueta, related_name='tareas')
    
class Asignacion_tarea(models.Model):
    observaciones = models.TextField()
    fecha_asignacion = models.DateTimeField()
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, null=True)