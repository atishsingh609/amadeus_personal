from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.name


class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    items = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
