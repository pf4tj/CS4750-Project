# Generated by Django 2.1.1 on 2018-11-29 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FFDB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='league_team',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='FFDB.Team'),
        ),
    ]
