# Generated by Django 3.2.4 on 2021-07-01 05:47

from django.db import migrations, models
import django.db.models.deletion
import myapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStampModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=128)),
                ('name', models.CharField(max_length=10)),
                ('nickname', models.CharField(max_length=20)),
                ('point', models.IntegerField(default=0)),
                ('level', models.CharField(default=0, max_length=10)),
                ('password', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service_upload',
            fields=[
                ('timestampmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='myapp.timestampmodel')),
                ('s_id', models.IntegerField(default=myapp.models.Service_upload.number, primary_key=True, serialize=False, unique=True)),
                ('category', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('service', models.TextField()),
                ('evalu1', models.IntegerField(choices=[(1, 'commercial'), (2, 'public interest'), (3, 'creativity')])),
                ('evalu2', models.IntegerField(choices=[(1, 'commercial'), (2, 'public interest'), (3, 'creativity')])),
                ('evalu3', models.IntegerField(choices=[(1, 'commercial'), (2, 'public interest'), (3, 'creativity')])),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user', verbose_name='작성자')),
            ],
            bases=('myapp.timestampmodel',),
        ),
        migrations.CreateModel(
            name='Service_evalu_upload',
            fields=[
                ('timestampmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='myapp.timestampmodel')),
                ('e_id', models.IntegerField(default=myapp.models.Service_evalu_upload.number, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('grade1', models.FloatField(default=0.0)),
                ('grade2', models.FloatField(default=0.0)),
                ('grade3', models.FloatField(default=0.0)),
                ('service_upload_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.service_upload')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user', verbose_name='작성자')),
            ],
            bases=('myapp.timestampmodel',),
        ),
        migrations.CreateModel(
            name='Service_evalu_comment',
            fields=[
                ('timestampmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='myapp.timestampmodel')),
                ('c_id', models.IntegerField(default=myapp.models.Service_evalu_comment.number, primary_key=True, serialize=False, unique=True)),
                ('content', models.TextField()),
                ('service_evalu_upload_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s_evalu_comment', to='myapp.service_evalu_upload', verbose_name='Service_upload')),
                ('service_upload_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.service_upload', verbose_name='Service')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user', verbose_name='작성자')),
            ],
            bases=('myapp.timestampmodel',),
        ),
        migrations.CreateModel(
            name='Idea_upload',
            fields=[
                ('timestampmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='myapp.timestampmodel')),
                ('i_id', models.IntegerField(default=myapp.models.Idea_upload.number, primary_key=True, serialize=False, unique=True)),
                ('category', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user', verbose_name='작성자')),
            ],
            bases=('myapp.timestampmodel',),
        ),
        migrations.CreateModel(
            name='Idea_evalu_comment',
            fields=[
                ('timestampmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='myapp.timestampmodel')),
                ('c_id', models.IntegerField(default=myapp.models.Idea_evalu_comment.number, primary_key=True, serialize=False, unique=True)),
                ('content', models.TextField()),
                ('idea_upload_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='myapp.idea_upload', verbose_name='원글')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user', verbose_name='작성자')),
            ],
            bases=('myapp.timestampmodel',),
        ),
    ]