from django.db import migrations

def crear_categorias(apps, schema_editor):
    Categoria = apps.get_model('recetas', 'Categoria')
    categorias = ['Desayuno', 'Almuerzo', 'Cena', 'Postre', 'Snack']
    for nombre in categorias:
        Categoria.objects.get_or_create(nombre=nombre)

class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(crear_categorias),
    ]
