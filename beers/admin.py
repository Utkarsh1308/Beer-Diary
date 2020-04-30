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
        ('Alcohol',         {'fields': ['alcohol']}),
        ('Hoppy',           {'fields': ['hoppy']}),
        ('Floral',          {'fields': ['floral']}),
        ('Herbal',          {'fields': ['herbal']}),
        ('Spicy',           {'fields': ['spicy']}),
        ('Malty',           {'fields': ['malty']}),
        ('Burnt',           {'fields': ['burnt']}),
        ('Sweet',           {'fields': ['sweet']}),
        ('Sour',            {'fields': ['sour']}),
        ('Bitter',          {'fields': ['bitter']}),
        ('Dry',             {'fields': ['dry']}),
        ('Linger',          {'fields': ['linger']}),
        ('ABV',             {'fields': ['abv']}),
        ('IBU',             {'fields': ['ibu']}),
    ]

admin.site.register(Beer, BeerAdmin)
