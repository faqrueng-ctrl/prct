from datetime import datetime, timezone

from django.db import migrations


DEMO_DATE = datetime(2026, 5, 19, 16, 37, tzinfo=timezone.utc)


def create_demo_record(apps, schema_editor):
    DataRecord = apps.get_model('yadro', 'DataRecord')
    DataRecord.objects.get_or_create(
        pk=2,
        defaults={
            'title': 'adadadad',
            'category': 'asdads',
            'status': 'делается',
            'priority': 'первый',
            'description': '',
            'is_active': True,
        },
    )
    DataRecord.objects.filter(pk=2).update(created_at=DEMO_DATE, updated_at=DEMO_DATE)


def remove_demo_record(apps, schema_editor):
    DataRecord = apps.get_model('yadro', 'DataRecord')
    DataRecord.objects.filter(pk=2, title='adadadad', category='asdads').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('yadro', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_demo_record, remove_demo_record),
    ]
