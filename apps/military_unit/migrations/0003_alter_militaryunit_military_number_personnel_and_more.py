# Generated by Django 4.0.4 on 2022-05-10 13:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_reasontype_alter_premiumgrid_tariff_category_and_more'),
        ('military_unit', '0002_alter_militaryunit_options_alter_person_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='militaryunit',
            name='military_number',
            field=models.CharField(max_length=50, verbose_name='Identifier'),
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('assigned_salary', models.PositiveIntegerField()),
                ('military_registration_specialty', models.CharField(max_length=255)),
                ('military_rank_by_personnel', models.CharField(max_length=255)),
                ('military_rank_factually', models.CharField(max_length=255)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personnel', to='military_unit.person')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personnel', to='general.position', verbose_name='Position')),
                ('tariff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personnel', to='general.tariffgrid', verbose_name='Tariff')),
            ],
            options={
                'verbose_name': 'Personnel',
                'verbose_name_plural': 'Personnel',
            },
        ),
        migrations.CreateModel(
            name='MilitaryUnitInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('commander_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Commander name')),
                ('chief_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Chief name')),
                ('military_unit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='military_unit_info', to='military_unit.militaryunit', verbose_name='Military Unit')),
            ],
            options={
                'verbose_name': 'Military Unit Info',
                'verbose_name_plural': 'Military Units Info',
            },
        ),
    ]
