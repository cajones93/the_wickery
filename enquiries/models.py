from django.db import models


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    MESSAGE_TYPES = (
        ('enquiry', 'General Enquiry'),
        ('bulk', 'Bulk Order Enquiry'),
        ('problem', 'Report a Problem'),
        ('other', 'Other'),
    )
    message_type = models.CharField(max_length=20, choices=MESSAGE_TYPES, default='enquiry')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Enquiries"
        ordering = ['-timestamp']

    def __str__(self):
        return f"Message from {self.name} ({self.email}) - {self.message_type} on {self.timestamp}"
