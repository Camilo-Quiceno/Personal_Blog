# Generated by Django 3.0.5 on 2020-04-11 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='category',
            old_name='nombre_categoria',
            new_name='category_name',
        ),
        migrations.CreateModel(
            name='Post_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Post')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Tag')),
            ],
        ),
    ]