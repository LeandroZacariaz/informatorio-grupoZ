# Generated by Django 4.2.3 on 2023-12-19 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("noticias", "0002_comentario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comentario",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="noticia",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
