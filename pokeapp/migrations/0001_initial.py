# Generated by Django 5.1.5 on 2025-01-23 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.URLField()),
                ('nome', models.CharField(max_length=50)),
                ('defesa', models.IntegerField(max_length=4)),
                ('ataque', models.IntegerField(max_length=4)),
                ('hp', models.IntegerField(max_length=4)),
                ('descricao', models.TextField()),
            ],
        ),
    ]
