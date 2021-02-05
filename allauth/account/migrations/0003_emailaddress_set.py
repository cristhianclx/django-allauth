# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_email_max_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emailaddress_set', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
