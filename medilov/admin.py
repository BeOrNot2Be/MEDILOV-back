from django.contrib import admin
from .models import Photo, Gallery, GalleryTopic, AboutUnit, Service
from .forms import AboutUnitForm

class AboutUnitAdmin(admin.ModelAdmin):
    form = AboutUnitForm
    fieldsets = (
        (None, {
            'fields': ('title', 'short_description', 'phrase','url', 'color', 'parent')
            }),
        )

admin.site.register(AboutUnit, AboutUnitAdmin)
admin.site.register(Photo)
admin.site.register(Gallery)
admin.site.register(GalleryTopic)
admin.site.register(Service)