from django.db import models

# Create your models here


class Project(models.Model):
    project_number = models.CharField(max_length=4, unique=True)
    project_title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.project_number} - {self.project_title}'


class Category(models.Model):
    category_title = models.TextField(unique=True)

    def __str__(self):
        return f'{self.category_title}'


class FixingCategory(models.Model):
    fixing_category = models.CharField(max_length=75, unique=True)

    def __str__(self):
        return f'{self.fixing_category}'


class FixingMetric(models.Model):
    METRIC_SIZE_CHOICES = (
        ('M4', 'M4'),
        ('M6', 'M6'),
        ('M8', 'M8'),
        ('M10', 'M10'),
        ('M12', 'M12'),
    )
    metric_size = models.CharField(
        max_length=5,
        choices=METRIC_SIZE_CHOICES,
        unique=True)

    def __str__(self):
        return f'{self.metric_size}'

class Colour(models.Model):
    colour_title = models.TextField(unique=True)
    colour_ral = models.TextField(unique=True)

    def __str__(self):
        return f'{self.colour_title} - {self.colour_ral}'

class Part(models.Model):
    part_number = models.CharField(max_length=15, unique=True)
    part_title = models.CharField(max_length=255)
    part_category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='parts')
    part_project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.SET_NULL, related_name='parts')
    part_colour = models.ForeignKey(Colour, null=True, blank=True, on_delete=models.SET_NULL, related_name='parts')


    def __str__(self):
        return f'{self.part_number} - {self.part_title}'

class Fixing(models.Model):
    metric_length = models.IntegerField(null=True, blank=True)
    fixing_category = models.ForeignKey(FixingCategory, on_delete=models.SET_NULL,
                                        null=True, related_name='fixing')
    fixing_metric = models.ForeignKey(FixingMetric, on_delete=models.CASCADE, null=True, related_name='fixing')
    part = models.OneToOneField(Part, on_delete=models.CASCADE, null=True, related_name='fixing')