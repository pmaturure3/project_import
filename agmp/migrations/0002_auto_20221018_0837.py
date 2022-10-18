# Generated by Django 2.2.24 on 2022-10-18 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agmp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phenotypeagmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='variantagmp',
            name='phenotypeagmp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agmp.Phenotypeagmp'),
        ),
    ]
