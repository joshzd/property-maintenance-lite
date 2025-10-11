from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Property, WorkOrder, WorkOrderEvent
from .serializers import (
    PropertySerializer,
    WorkOrderEventSerializer,
    WorkOrderSerializer,
)


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all().order_by("-created_at")
    serializer_class = PropertySerializer


class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.select_related("property").order_by("-created_at")
    serializer_class = WorkOrderSerializer

    @action(detail=True, methods=["post"])
    def assign(self, request, pk=None):
        order = self.get_object()
        assignee = request.data.get("assignee")
        order.assignee = assignee
        order.status = "assigned"
        order.save()
        WorkOrderEvent.objects.create(
            work_order=order,
            event_type="status_changed",
            detail=f"Assigned to {assignee}",
        )
        return Response({"status": "assigned", "assignee": assignee})

    @action(detail=True, methods=["post"])
    def transition(self, request, pk=None):
        order = self.get_object()
        new_status = request.data.get("status")
        if new_status not in dict(WorkOrder.STATUSES):
            return Response(
                {"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST
            )
        old_status = order.status
        order.status = new_status
        order.save()
        WorkOrderEvent.objects.create(
            work_order=order,
            event_type="status_changed",
            detail=f"{old_status} -> {new_status}",
        )
        return Response({"status": new_status})

    @action(detail=True, methods=["post"])
    def note(self, request, pk=None):
        order = self.get_object()
        detail = request.data.get("detail", "")
        WorkOrderEvent.objects.create(
            work_order=order, event_type="note_added", detail=detail
        )
        return Response({"note_added": detail})


class WorkOrderEventViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = WorkOrderEventSerializer

    def get_queryset(self):
        qs = WorkOrderEvent.objects.select_related("work_order").order_by("-created_at")
        work_order_id = self.request.query_params.get("work_order")
        if work_order_id:
            qs = qs.filter(work_order_id=work_order_id)
        return qs
