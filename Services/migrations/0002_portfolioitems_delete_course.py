# Generated by Django 5.1.6 on 2025-03-11 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('link_image', models.ImageField(upload_to='portfolio_ImageLink')),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='Portfolio_Items/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
