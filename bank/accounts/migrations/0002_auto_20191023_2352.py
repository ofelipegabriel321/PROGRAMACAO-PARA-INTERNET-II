# Generated by Django 2.2.5 on 2019-10-24 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200)),
                ('balance', models.FloatField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('owner',),
            },
        ),
        migrations.DeleteModel(
            name='Accounts',
        ),
    ]