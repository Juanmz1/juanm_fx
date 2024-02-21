# Generated by Django 5.0.1 on 2024-02-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_personaldetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=200, verbose_name='Amount')),
                ('card_code', models.CharField(max_length=200, verbose_name='Card Code')),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
