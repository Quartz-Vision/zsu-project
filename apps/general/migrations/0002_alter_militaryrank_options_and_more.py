# Generated by Django 4.0.4 on 2022-04-29 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='militaryrank',
            options={'verbose_name': 'Military Rank', 'verbose_name_plural': 'Military Ranks'},
        ),
        migrations.AlterModelOptions(
            name='militaryspecialization',
            options={'verbose_name': 'Military Specialization', 'verbose_name_plural': 'Military Specializations'},
        ),
        migrations.AlterModelOptions(
            name='paymenttype',
            options={'verbose_name': 'Payment Type', 'verbose_name_plural': 'Payment Types'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'verbose_name': 'Position', 'verbose_name_plural': 'Positions'},
        ),
        migrations.AlterModelOptions(
            name='premiumgrid',
            options={'verbose_name': 'Premium Grid', 'verbose_name_plural': 'Premium Grid'},
        ),
        migrations.AlterModelOptions(
            name='tariffcategory',
            options={'verbose_name': 'Tariff Category', 'verbose_name_plural': 'Tariff Categories'},
        ),
        migrations.AlterModelOptions(
            name='tariffgrid',
            options={'verbose_name': 'Tariff Grid', 'verbose_name_plural': 'Tariff Grid'},
        ),
        migrations.AlterModelOptions(
            name='wacationtype',
            options={'verbose_name': 'Wacation Type', 'verbose_name_plural': 'Wacation Types'},
        ),
        migrations.AlterField(
            model_name='militaryrank',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='militaryspecialization',
            name='identifier',
            field=models.IntegerField(verbose_name='Identifier'),
        ),
        migrations.AlterField(
            model_name='militaryspecialization',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='paymenttype',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='premiumgrid',
            name='premium',
            field=models.PositiveIntegerField(verbose_name='Premium'),
        ),
        migrations.AlterField(
            model_name='premiumgrid',
            name='tariff_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.tariffcategory', verbose_name='Tariff Category'),
        ),
        migrations.AlterField(
            model_name='tariffcategory',
            name='identifier',
            field=models.CharField(max_length=255, verbose_name='Identifier'),
        ),
        migrations.AlterField(
            model_name='tariffgrid',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.position', verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='tariffgrid',
            name='salary',
            field=models.PositiveIntegerField(verbose_name='Salary'),
        ),
        migrations.AlterField(
            model_name='tariffgrid',
            name='tariff_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.tariffcategory', verbose_name='Tariff Category'),
        ),
        migrations.AlterField(
            model_name='wacationtype',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
    ]