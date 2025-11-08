from django.db import models
from properties.models import Property
from django.contrib.auth.models import User  # if you want to track who booked

class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='bookings')
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # optional: link to user
    buyer_name = models.CharField(max_length=100)  # in case buyer is not a registered user
    scheduled_date = models.DateTimeField()
    message = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=[('pending','Pending'),('confirmed','Confirmed')],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.property.title} - {self.buyer_name} on {self.scheduled_date}"
