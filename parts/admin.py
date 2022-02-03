from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from parts.models import Part, Project, Category, Colour, FixingCategory, FixingMetric, Fixing

models = [Project, Category, Colour, FixingCategory, FixingMetric, Fixing]

for m in models:
    admin.site.register(m)

@admin.register(Part)
class PartAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    from_encoding = "utf-8-sig"
