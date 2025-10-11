from django.db import models


# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=200)
    address_line1 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class WorkOrder(models.Model):
    PRIORITIES = [("low", "Low"), ("normal", "Normal"), ("high", "High")]
    STATUSES = [
        ("new", "New"),
        ("assigned", "Assigned"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
        ("canceled", "Canceled"),
    ]
    property = models.ForeignKey(
        Property, on_delete=models.CASCADE, related_name="workorders"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITIES, default="normal")
    status = models.CharField(max_length=20, choices=STATUSES, default="new")
    assignee = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.status})"


class WorkOrderEvent(models.Model):
    TYPES = [("status_changed", "Status Changed"), ("note_added", "Note Added")]
    work_order = models.ForeignKey(
        WorkOrder, on_delete=models.CASCADE, related_name="events"
    )
    event_type = models.CharField(max_length=50, choices=TYPES)
    detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_type} on {self.work_order_id}"
