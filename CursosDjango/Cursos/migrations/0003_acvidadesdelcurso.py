# Generated by Django 4.0.5 on 2022-07-01 13:17

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0002_alter_cursos_options_cursos_imagen_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcvidadesdelCurso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='clave')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Registrado')),
                ('actividad', ckeditor.fields.RichTextField(verbose_name='Comentario')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cursos.cursos', verbose_name='Materia')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
                'ordering': ['-created'],
            },
        ),
    ]
