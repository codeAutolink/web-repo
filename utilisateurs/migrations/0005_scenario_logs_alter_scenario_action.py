# Generated by Django 4.1.12 on 2023-10-23 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateurs', '0004_alter_scenario_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='logs',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='action',
            field=models.TextField(),
        ),
    ]