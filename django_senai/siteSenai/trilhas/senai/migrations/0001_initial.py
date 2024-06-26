# Generated by Django 5.0.6 on 2024-05-22 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCurso', models.CharField(max_length=45)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tempo', models.IntegerField(help_text='Tempo de duração: ')),
                ('path', models.ImageField(upload_to='imagens/')),
            ],
        ),
    ]
