# Generated by Django 4.0.4 on 2022-05-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0013_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fileupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choose_file', models.FileField(upload_to='documents')),
            ],
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]