from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('leads', '0012_auto_20210107_0851'),
    ]
    operations = [
        migrations.AddField(
            model_name='lead',
            name='converted_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
