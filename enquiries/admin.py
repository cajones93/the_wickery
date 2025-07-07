from django.contrib import admin
from .models import Enquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message_type', 'subject', 'timestamp', 'is_read')
    list_filter = ('message_type', 'is_read', 'timestamp')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('timestamp',)
    actions = ['mark_as_read', 'mark_as_unread']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, "Selected messages marked as read.")

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
        self.message_user(request, "Selected messages marked as unread.")
