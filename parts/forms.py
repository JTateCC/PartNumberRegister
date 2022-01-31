from django import forms
from parts.models import Part, Project, Category

class PartForm(forms.ModelForm):

    class Meta:
        model = Part
        fields = ['part_number',
                  'part_title',
                  'part_category',
                  'part_project',
                  ]
