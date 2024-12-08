from django.db import models

class TypeOfOrder(models.Model):
    title = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)
    cost = models.FloatField()

    def __str__(self):
        return self.title

class History(models.Model):
    Length = models.FloatField(default=0)
    Width = models.FloatField(default=0)
    Height = models.FloatField(default=0)
    Number_of_pieces_per_box = models.IntegerField(default=0)
    Total_quantity = models.IntegerField(default=0)
    Box_weight = models.FloatField(default=0)
    Cost_per_piece = models.FloatField(default=0)

    Density = models.FloatField(default=0)
    Logistics_naked = models.FloatField(default=0)
    Logistics = models.FloatField(default=0)
    Insurance  = models.FloatField(default=0)
    Packaging = models.FloatField(default=0)
    Unloading_at_MSK = models.FloatField(default=0)
    Total_cost_per_unit = models.FloatField(default=0)

    Total_logistics_cost = models.FloatField(default=0)
    Total_Insurance = models.FloatField(default=0)
    Total_Packaging = models.FloatField(default=0)
    Total_Unloading = models.FloatField(default=0)
    Total_cost_of_the_lot = models.FloatField(default=0)

    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History {self.id}"
