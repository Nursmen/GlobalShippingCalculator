# Generated by Django 5.1.4 on 2024-12-08 12:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("calcitself", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="history",
            name="Packaging_Regular",
        ),
        migrations.RemoveField(
            model_name="history",
            name="Unloading",
        ),
        migrations.AddField(
            model_name="history",
            name="Total_Insurance",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="history",
            name="Total_Packaging",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="history",
            name="Total_Unloading",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="history",
            name="Box_weight",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="history",
            name="Cost_per_piece",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="history",
            name="Density",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="history",
            name="Height",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="history",
            name="Insurance",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="history",
            name="Length",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="history",
            name="Logistics",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="history",
            name="Logistics_naked",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="history",
            name="Number_of_pieces_per_box",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="history",
            name="Packaging",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="history",
            name="Total_cost_of_the_lot",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="history",
            name="Total_cost_per_unit",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="history",
            name="Total_logistics_cost",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="history",
            name="Total_quantity",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="history",
            name="Unloading_at_MSK",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="history",
            name="Width",
            field=models.FloatField(default=0),
        ),
    ]