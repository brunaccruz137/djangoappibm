# Generated by Django 3.1.3 on 2022-08-29 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.TextField()),
                ('is_correct', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choices', models.ManyToManyField(to='onlinecourse.Choice')),
                ('enrollment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.enrollment')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('grade', models.IntegerField()),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.lesson')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question'),
        ),
    ]
