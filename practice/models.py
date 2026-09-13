from django.db import models
class Enquiry(models.Model):
    name = models.CharField(max_length=160)
    organisation = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    topic = models.CharField(max_length=180, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self): return f'{self.name} — {self.topic or "General enquiry"}'
