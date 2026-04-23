from django.db import models

class CropType(models.Model):
    name = models.CharField(max_length=100) # e.g., Mango, Lemon
    icon = models.CharField(max_length=50, default='fa-leaf')

    def __str__(self):
        return self.name

class Variety(models.Model):
    crop_type = models.ForeignKey(CropType, on_delete=models.CASCADE, related_name='varieties')
    name = models.CharField(max_length=100) # e.g., Sindhri, Chaunsa
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Varieties"

    def __str__(self):
        return f"{self.crop_type.name} - {self.name}"

class Plantation(models.Model):
    STATUS_CHOICES = [
        ('Growing', 'Growing'),
        ('Harvesting', 'Harvesting'),
        ('Dormant', 'Dormant'),
        ('Problem Detected', 'Problem Detected'),
    ]

    variety = models.ForeignKey(Variety, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, help_text="Field Name or Section ID")
    planting_date = models.DateField()
    number_of_plants = models.IntegerField()
    expected_harvest_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Growing')
    soil_condition = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.variety.name} at {self.location}"

class Harvest(models.Model):
    plantation = models.ForeignKey(Plantation, on_delete=models.CASCADE, related_name='harvests')
    date = models.DateField()
    quantity = models.FloatField(help_text="in kg")
    quality = models.CharField(max_length=50, choices=[('Grade A', 'Grade A'), ('Grade B', 'Grade B'), ('Grade C', 'Grade C')], default='Grade A')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Harvest of {self.plantation} on {self.date}"
