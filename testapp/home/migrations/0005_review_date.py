# Generated by Django 2.0.13 on 2019-04-01 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_paginationpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='last_review_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='next_review_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
