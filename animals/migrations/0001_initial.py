# Generated by Django 4.0.6 on 2022-07-08 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
        ('characterisrics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.FloatField()),
                ('weight', models.FloatField()),
                ('sex', models.CharField(max_length=15)),
                ('characteristic', models.ManyToManyField(to='characterisrics.characteristic')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='groups.group')),
            ],
        ),
    ]
