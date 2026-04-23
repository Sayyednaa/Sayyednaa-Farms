from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100) # e.g., Poultry, Fish, Cattle
    icon = models.CharField(max_length=50, default='fa-paw')

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Breed(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='breeds')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.category.name} - {self.name}"

class Livestock(models.Model):
    STATUS_CHOICES = [
        ('Healthy', 'Healthy'),
        ('Sick', 'Sick'),
        ('In Quarantine', 'In Quarantine'),
        ('Sold', 'Sold'),
        ('Deceased', 'Deceased'),
    ]

    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=50, unique=True, help_text="Tag ID or Name")
    location = models.CharField(max_length=100, help_text="Pen, Tank, or Shed Number")
    date_of_birth = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Healthy')
    weight = models.FloatField(help_text="in kg", null=True, blank=True)
    health_notes = models.TextField(blank=True)
    image = models.ImageField(upload_to='livestock/', null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Livestock"

    def __str__(self):
        return f"{self.identifier} ({self.breed.name})"

class HealthRecord(models.Model):
    livestock = models.ForeignKey(Livestock, on_delete=models.CASCADE, related_name='health_records')
    date = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    veterinarian = models.CharField(max_length=100, blank=True)
    next_checkup = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Record for {self.livestock.identifier} on {self.date}"
