# Generated by Django 4.2.7 on 2023-11-20 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demanda', '0002_customuser_is_tecnico'),
    ]

    operations = [
        migrations.AddField(
            model_name='demanda',
            name='status',
            field=models.CharField(choices=[('AB', 'Aberta'), ('AT', 'Atendida')], default='AB', max_length=2),
        ),
    ]
