# Generated by Django 4.0.5 on 2022-06-06 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_usuario_ciudad'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='ciudad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.ciudad'),
        ),
    ]
