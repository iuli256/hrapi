# Generated by Django 4.0 on 2022-02-26 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=100, null=True)),
                ('last_name', models.CharField(default=None, max_length=100, null=True)),
                ('email', models.CharField(default=None, max_length=100, null=True)),
                ('gender', models.CharField(default=None, max_length=1, null=True)),
                ('date_of_birth', models.DateField(default=None, null=True)),
                ('industry', models.CharField(default=None, max_length=100, null=True)),
                ('salary', models.DecimalField(decimal_places=2, default=None, max_digits=12, null=True)),
                ('years_of_experience', models.IntegerField(default=None, null=True)),
            ],
        ),
    ]