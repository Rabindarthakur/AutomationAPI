# Generated by Django 3.2 on 2022-07-04 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_alter_fileupload_document_alter_pdetail_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d1', models.TextField(max_length=255)),
                ('d2', models.TextField(max_length=255)),
            ],
        ),
    ]