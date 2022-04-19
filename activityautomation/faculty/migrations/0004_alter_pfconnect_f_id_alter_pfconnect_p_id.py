# Generated by Django 4.0.4 on 2022-04-16 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0003_pfconnect_alter_publications_p_doi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pfconnect',
            name='F_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.faculty'),
        ),
        migrations.AlterField(
            model_name='pfconnect',
            name='P_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.publications'),
        ),
    ]
