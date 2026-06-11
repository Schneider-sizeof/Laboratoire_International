from django.contrib import admin
from .models import Service, Testimonial, Booking, TeamMember, GalleryImage, BusinessHour


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name_fr', 'category', 'price', 'duration_minutes', 'is_featured', 'order')
    list_filter = ('category', 'is_featured')
    search_fields = ('name', 'name_fr', 'description', 'description_fr')
    ordering = ('order', 'name')
    list_editable = ('order', 'is_featured', 'price')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'rating', 'date', 'is_featured')
    list_filter = ('rating', 'is_featured')
    search_fields = ('client_name', 'text', 'text_fr')
    ordering = ('-date',)
    list_editable = ('is_featured',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'service', 'preferred_date', 'preferred_time', 'status', 'created_at')
    list_filter = ('status', 'service', 'preferred_date')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    ordering = ('-created_at',)
    list_editable = ('status',)
    readonly_fields = ('created_at',)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role_fr', 'order')
    search_fields = ('name', 'role', 'role_fr')
    ordering = ('order',)
    list_editable = ('order',)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('caption_fr', 'order')
    search_fields = ('caption', 'caption_fr')
    ordering = ('order',)
    list_editable = ('order',)


@admin.register(BusinessHour)
class BusinessHourAdmin(admin.ModelAdmin):
    list_display = ('get_day_display_name', 'open_time', 'close_time', 'is_closed')
    list_filter = ('is_closed',)
    ordering = ('day',)
    list_editable = ('open_time', 'close_time', 'is_closed')

    @admin.display(description='Jour')
    def get_day_display_name(self, obj):
        return obj.get_day_display()
