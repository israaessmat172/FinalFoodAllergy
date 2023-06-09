# Generated by Django 4.1.8 on 2023-04-27 23:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="allergy",
            name="arabicName",
            field=models.CharField(max_length=500, verbose_name="Arabic name"),
        ),
        migrations.AlterField(
            model_name="allergy",
            name="englishName",
            field=models.CharField(max_length=500, verbose_name="English name"),
        ),
        migrations.AlterField(
            model_name="category",
            name="arabicName",
            field=models.CharField(max_length=500, verbose_name="Arabic name"),
        ),
        migrations.AlterField(
            model_name="category",
            name="englishName",
            field=models.CharField(max_length=500, verbose_name="English name"),
        ),
        migrations.AlterField(
            model_name="food",
            name="arabicName",
            field=models.CharField(max_length=500, verbose_name="Arabic name"),
        ),
        migrations.AlterField(
            model_name="food",
            name="englishName",
            field=models.CharField(max_length=500, verbose_name="English name"),
        ),
        migrations.AlterField(
            model_name="foodallergy",
            name="arabicDescription",
            field=models.CharField(max_length=500, verbose_name="Arabic description"),
        ),
        migrations.AlterField(
            model_name="foodallergy",
            name="arabicName",
            field=models.CharField(max_length=500, verbose_name="Arabic name"),
        ),
        migrations.AlterField(
            model_name="foodallergy",
            name="arabicProtection",
            field=models.CharField(max_length=500, verbose_name="Arabic protection"),
        ),
        migrations.AlterField(
            model_name="foodallergy",
            name="arabicSymptoms",
            field=models.CharField(max_length=500, verbose_name="Arabic symptoms"),
        ),
        migrations.AlterField(
            model_name="foodallergy",
            name="englishDescription",
            field=models.CharField(max_length=500, verbose_name="English description"),
        ),
        migrations.AlterField(
            model_name="foodallergy",
            name="englishName",
            field=models.CharField(max_length=500, verbose_name="English name"),
        ),
        migrations.AlterField(
            model_name="foodallergy",
            name="englishProtection",
            field=models.CharField(max_length=500, verbose_name="English protection"),
        ),
        migrations.AlterField(
            model_name="foodallergy",
            name="englishSymptoms",
            field=models.CharField(max_length=500, verbose_name="English symptoms"),
        ),
    ]
