from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
