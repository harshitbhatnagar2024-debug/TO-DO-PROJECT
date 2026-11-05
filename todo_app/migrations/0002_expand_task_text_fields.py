from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo_table",
            name="title",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="todo_table",
            name="description",
            field=models.TextField(max_length=1000),
        ),
    ]
