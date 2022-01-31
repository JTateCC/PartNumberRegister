from django.db import models

# Create your models here


class Project(models.Model):
    project_number = models.CharField(max_length=4)
    project_title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.project_number} - {self.project_title}'


class Category(models.Model):
    category_title = models.TextField()

    def __str__(self):
        return f'{self.category_title}'

class Fixing(Category):
    METRIC_SIZE_CHOICES = (
        ('M4','M4'),
        ('M6', 'M6'),
        ('M8', 'M8'),
        ('M10', 'M10'),
        ('M12', 'M12'),
    )

    fixing_type = models.TextField()
    metric_size = models.CharField(
        max_length=5,
        choices=METRIC_SIZE_CHOICES)
    metric_length = models.IntegerField()

class Part(models.Model):
    part_number = models.CharField(max_length=15)
    part_title = models.CharField(max_length=255)
    part_category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='categories')
    part_project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL, related_name='projects')

    def __str__(self):
        return f'{self.part_number} - {self.part_title}'
