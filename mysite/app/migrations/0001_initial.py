# Generated by Django 4.0.3 on 2022-05-14 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='タイトル')),
                ('sub_title', models.CharField(blank=True, max_length=100, null=True, verbose_name='サブタイトル')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='名前')),
                ('introduction', models.CharField(blank=True, max_length=100, null=True, verbose_name='自己紹介')),
                ('top_image', models.ImageField(upload_to='images', verbose_name='トップ画像')),
                ('sub_image', models.ImageField(upload_to='images', verbose_name='サブ画像')),
            ],
        ),
    ]
