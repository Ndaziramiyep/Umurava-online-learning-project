# Generated by Django 3.1.1 on 2020-09-09 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_title', models.CharField(max_length=50, verbose_name='Topic Title')),
                ('topic_slug', models.SlugField(max_length=55, verbose_name='Topic Slug')),
                ('topic_description', models.TextField(blank=True, null=True, verbose_name='Topic Description')),
                ('topic_image', models.ImageField(blank=True, null=True, upload_to='topics/')),
                ('topic_is_active', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=10, verbose_name='Is Active?')),
                ('topic_created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('topic_updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('meta_topic_title', models.CharField(blank=True, max_length=60, null=True, verbose_name='SEO Topic Title (60 Characters Long)')),
                ('meta_topic_keywords', models.TextField(blank=True, null=True, verbose_name='SEO Topic Keywords, Separated by Commas')),
                ('meta_topic_description', models.TextField(blank=True, null=True, verbose_name='SEO Topic Description (160 characters long)')),
            ],
        ),
    ]