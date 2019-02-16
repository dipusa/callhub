# Generated by Django 2.0.1 on 2019-02-15 11:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('series', models.CharField(max_length=252)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
