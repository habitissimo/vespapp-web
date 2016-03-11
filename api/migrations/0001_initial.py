# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=128, verbose_name='Título')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
        ),
        migrations.CreateModel(
            name='ExpertComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=512, verbose_name='Comentario')),
                ('is_valid', models.NullBooleanField(verbose_name='Avistamiento válido')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expert_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nombre')),
                ('lat', models.FloatField(verbose_name='Latitud')),
                ('lng', models.FloatField(verbose_name='Longitud')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='sightings/')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Título')),
                ('question_type', models.IntegerField(verbose_name='Tipo de pregunta')),
                ('sighting_type', models.IntegerField(verbose_name='Tipo de avistamiento')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activa')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
        ),
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(verbose_name='Latitud')),
                ('lng', models.FloatField(verbose_name='Longitud')),
                ('status', models.IntegerField(default=0, verbose_name='Estado')),
                ('free_text', models.CharField(max_length=512, verbose_name='Texto sobre localización')),
                ('type', models.IntegerField(verbose_name='Tipo de avistamiento')),
                ('public', models.BooleanField(default=False, verbose_name='Publico')),
                ('is_valid', models.NullBooleanField(default=None, verbose_name='Avistamiento válido')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('answers', models.ManyToManyField(blank=True, default=None, related_name='sightings', to='api.Answer')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sightings', to='api.Location', verbose_name='Localización')),
                ('moderator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='moderated_sightings', to=settings.AUTH_USER_MODEL, verbose_name='Moderador')),
                ('reported_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reported_sightings', to=settings.AUTH_USER_MODEL, verbose_name='Reportado por')),
            ],
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=512, verbose_name='Comentario')),
                ('moderated', models.BooleanField(default=False, verbose_name='Moderado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('sighting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='api.Sighting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='picture',
            name='sighting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='api.Sighting'),
        ),
        migrations.AddField(
            model_name='expertcomment',
            name='sighting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expert_comments', to='api.Sighting'),
        ),
        migrations.AddField(
            model_name='expertcomment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expert_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='default_answer', to='api.Question'),
        ),
    ]
