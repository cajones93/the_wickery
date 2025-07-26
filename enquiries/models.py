from django.db import models


class Enquiry(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(max_length=500, blank=False, null=False)
    MESSAGE_TYPES = (
        ('enquiry', 'General Enquiry'),
        ('bulk', 'Bulk Order Enquiry'),
        ('problem', 'Report a Problem'),
        ('other', 'Other'),
    )
    message_type = models.CharField(max_length=20, choices=MESSAGE_TYPES, default='enquiry')
    order_number = models.CharField(max_length=32, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Enquiries"
        ordering = ['-timestamp']

    def __str__(self):
        return f"Message from {self.name} ({self.email}) - {self.message_type} on {self.timestamp}"
