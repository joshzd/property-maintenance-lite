from rest_framework import serializers

from .models import Property, WorkOrder, WorkOrderEvent


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"


class WorkOrderEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrderEvent
        fields = "__all__"


class WorkOrderSerializer(serializers.ModelSerializer):
    events = WorkOrderEventSerializer(many=True, read_only=True)

    class Meta:
        model = WorkOrder
        fields = "__all__"
