# Generated by Django 3.1.3 on 2022-07-15 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entiretyflag', models.BooleanField()),
                ('partflag', models.IntegerField()),
                ('smiles', models.CharField(max_length=200)),
                ('reactionAtoms', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Queries2', to='testapp.compound')),
                ('reactant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Queries1', to='testapp.compound')),
            ],
        ),
    ]
