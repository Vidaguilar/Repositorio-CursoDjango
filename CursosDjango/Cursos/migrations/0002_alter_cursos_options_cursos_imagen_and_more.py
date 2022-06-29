# Generated by Django 4.0.5 on 2022-06-29 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cursos',
            options={'ordering': ['created'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AddField(
            model_name='cursos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='Materia',
            field=models.CharField(max_length=12, verbose_name='Mat'),
        ),
    ]