from django.contrib import admin
from .models import Bulding, BuldingImage, RequestBulding
from django.utils.html import format_html

# Register your models here.

admin.site.register(RequestBulding)

class BuildingImageInline(admin.TabularInline):
    model = BuldingImage
    extra = 0
    readonly_fields = ('image_preview',)
    
    def image_preview(self, obj):
        return format_html('<img src="{url}" width="200" height="200" />'.format(url=obj.image.url))
    
    image_preview.short_description = 'Preview'

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('type', 'price', 'area', 'location', 'rooms', 'notes')
    list_editable = ('price', 'area', 'location', 'rooms', 'notes')
    list_filter = ('type',)
    ordering = ('type',)

    inlines = [BuildingImageInline,]

admin.site.register(Bulding, BuildingAdmin)

class BuildingImageAdmin(admin.ModelAdmin):
    list_display = ('building', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return format_html('<img src="{url}" width="200" height="200" />'.format(url=obj.image.url))

    image_preview.short_description = 'Preview'

admin.site.register(BuldingImage, BuildingImageAdmin)
