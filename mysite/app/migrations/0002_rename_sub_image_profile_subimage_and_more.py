# Generated by Django 4.0.3 on 2022-05-15 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='sub_image',
            new_name='subimage',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='sub_title',
            new_name='subtitle',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='top_image',
            new_name='topimage',
        ),
        migrations.AddField(
            model_name='profile',
            name='github',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='github'),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='instagram'),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='linkedin'),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='twitter'),
        ),
    ]
