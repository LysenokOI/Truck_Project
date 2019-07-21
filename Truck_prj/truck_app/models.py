from django.db import models


# Create your models here.
class TruckModel(models.Model):
    truck_model = models.CharField(
        max_length=30,
        verbose_name="name of truck model")
    truck_capacity = models.IntegerField(
        default=100,
        verbose_name="cargo capacity of the truck")

    def __str__(self):
        return self.truck_model


class TruckWork(models.Model):
    truck_work = models.ForeignKey(
        TruckModel,
        verbose_name="working truck",
        on_delete=models.CASCADE)
    cargo_weight = models.IntegerField(
        default=100,
        verbose_name="cargo weight")
    truck_id = models.CharField(
        max_length=30,
        verbose_name="truck id",
        unique=True)

    def truck_overweight(self):
        if self.cargo_weight > self.truck_work.truck_capacity:
            truck_overweight = (self.cargo_weight - self.truck_work.truck_capacity)/self.truck_work.truck_capacity*100
            self.truck_overweight = truck_overweight
        else:
            self.truck_overweight = 0
        return round(self.truck_overweight, 0.1)

    def __str__(self):
        return "{} truck with id: {}".format(self.truck_work, self.truck_id)
