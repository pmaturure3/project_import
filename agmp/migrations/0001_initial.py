# Generated by Django 2.2.24 on 2022-10-18 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drugagmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_id', models.CharField(blank=True, max_length=50, null=True)),
                ('drug_bank_id', models.CharField(blank=True, max_length=50, null=True)),
                ('drug_name', models.CharField(blank=True, max_length=50, null=True)),
                ('indication', models.CharField(blank=True, max_length=50, null=True)),
                ('iupac_name_seq', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Geneagmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chromosome', models.CharField(blank=True, max_length=50, null=True)),
                ('function', models.CharField(blank=True, max_length=50, null=True)),
                ('gene_name', models.CharField(blank=True, max_length=50, null=True)),
                ('uniprot', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Studyagmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_ac', models.CharField(blank=True, max_length=50, null=True)),
                ('publication_id', models.CharField(blank=True, max_length=50, null=True)),
                ('publication_type', models.CharField(blank=True, max_length=50, null=True)),
                ('publication_year', models.CharField(blank=True, max_length=50, null=True)),
                ('study_type', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variantagmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allele', models.CharField(blank=True, max_length=50, null=True)),
                ('source_db', models.CharField(blank=True, max_length=50, null=True)),
                ('drugagmp', models.ForeignKey(blank=True, default='DRUG0', null=True, on_delete=django.db.models.deletion.CASCADE, to='agmp.Drugagmp')),
                ('geneagmp', models.ForeignKey(blank=True, default='GENE0', null=True, on_delete=django.db.models.deletion.CASCADE, to='agmp.Geneagmp')),
                ('studyagmp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agmp.Studyagmp')),
            ],
        ),
    ]
