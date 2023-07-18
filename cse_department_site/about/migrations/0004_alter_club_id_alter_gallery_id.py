
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_message_alter_club_id_alter_gallery_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
