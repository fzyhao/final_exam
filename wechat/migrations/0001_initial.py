# Generated by Django 2.1.2 on 2018-12-10 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('sex', models.CharField(max_length=10, null=True, verbose_name='sex')),
                ('created_at', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='G_msg_config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('gid', models.IntegerField(primary_key=True, serialize=False)),
                ('gname', models.CharField(max_length=20)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('num_of_group', models.IntegerField()),
                ('master_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Group_msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.IntegerField()),
                ('content', models.CharField(max_length=500)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('form_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_id_GM', to=settings.AUTH_USER_MODEL)),
                ('gid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gid_GM', to='wechat.Group')),
            ],
        ),
        migrations.CreateModel(
            name='One_to_one_msg_record',
            fields=[
                ('mid', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=500)),
                ('form_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_id_O2O', to=settings.AUTH_USER_MODEL)),
                ('to_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_id_O2O', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_realation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_id_UR', to=settings.AUTH_USER_MODEL)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uid_UR', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='g_msg_config',
            name='gid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gid_GMC', to='wechat.Group'),
        ),
        migrations.AddField(
            model_name='g_msg_config',
            name='last_read_msg_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='last_read_msg_id', to='wechat.Group_msg'),
        ),
        migrations.AddField(
            model_name='g_msg_config',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uid_GMC', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='user_realation',
            unique_together={('uid', 'friend_id')},
        ),
        migrations.AlterUniqueTogether(
            name='group_msg',
            unique_together={('mid', 'gid')},
        ),
        migrations.AlterUniqueTogether(
            name='g_msg_config',
            unique_together={('uid', 'gid')},
        ),
    ]