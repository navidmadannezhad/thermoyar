# Generated by Django 3.1.5 on 2021-01-12 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tabels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sub_cold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField(max_length=5)),
                ('pres', models.FloatField(max_length=5)),
                ('vol', models.FloatField(max_length=8)),
                ('eng', models.FloatField(max_length=8)),
                ('antal', models.FloatField(max_length=8)),
                ('ant', models.FloatField(max_length=8)),
                ('material_n', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tabels.material')),
                ('state_n', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tabels.state')),
            ],
        ),
    ]
