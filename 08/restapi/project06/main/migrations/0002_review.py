# Generated by Django 4.0.3 on 2022-08-05 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='main.movie')),
            ],
        ),
    ]