# Generated by Django 5.1.5 on 2025-01-23 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.URLField()),
                ('nome', models.CharField(max_length=50)),
                ('defesa', models.IntegerField()),
                ('ataque', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cards',
        ),
    ]
