# Generated by Django 4.0.4 on 2022-04-22 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coach_name', models.CharField(max_length=100)),
                ('coach_surname', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=20)),
                ('mail', models.EmailField(db_index=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Dancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dancer_name', models.CharField(max_length=50)),
                ('dancer_surname', models.CharField(max_length=50)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dance_Info.club')),
                ('coach', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dance_Info.coach')),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='coach',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dance_Info.coach'),
        ),
    ]
