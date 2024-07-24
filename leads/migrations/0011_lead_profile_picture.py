from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('leads', '0010_auto_20201217_2139'),
    ]
    operations = [
        migrations.AddField(
            model_name='lead',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
