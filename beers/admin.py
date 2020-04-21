from django.contrib import admin
from .models import Beer

# Register your models here.
class BeerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',            {'fields': ['name']}),
        ('Brewer',          {'fields': ['brewer']}),
        ('Date',            {'fields': ['date']}),
        ('Price',           {'fields': ['price']}),
        ('Serving_Type',    {'fields': ['serving_type']}),
        ('Rating',          {'fields': ['rating']}),
        ('Description',     {'fields': ['description']}),
    ]

admin.site.register(Beer, BeerAdmin)
