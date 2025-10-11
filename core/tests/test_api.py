import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from core.models import Property, WorkOrder, WorkOrderEvent

pytestmark = pytest.mark.django_db


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def property_obj(db):
    return Property.objects.create(
        name="Sunset Apartments",
        address_line1="101 Main St",
        city="Rapid City",
        state="SD",
        postal_code="57701",
    )


@pytest.fixture
def work_order(db, property_obj):
    return WorkOrder.objects.create(
        property=property_obj,
        title="Leaky faucet",
        description="Fix kitchen sink",
        priority="high",
    )


def test_create_property(client):
    url = reverse("property-list")
    data = {"name": "Hillside", "city": "RC", "state": "SD", "postal_code": "57701"}
    resp = client.post(url, data, format="json")
    assert resp.status_code == 201
    assert resp.data["name"] == "Hillside"


def test_create_workorder(client, property_obj):
    url = reverse("workorder-list")
    data = {
        "property": property_obj.id,
        "title": "Replace air filter",
        "description": "Tenant reports odor",
    }
    resp = client.post(url, data, format="json")
    assert resp.status_code == 201
    assert resp.data["title"] == "Replace air filter"


def test_assign_action(client, work_order):
    url = reverse("workorder-assign", args=[work_order.id])
    resp = client.post(url, {"assignee": "Rapid Plumbing LLC"}, format="json")
    work_order.refresh_from_db()
    assert resp.status_code == 200
    assert work_order.assignee == "Rapid Plumbing LLC"
    assert WorkOrderEvent.objects.count() == 1


def test_transition_action(client, work_order):
    url = reverse("workorder-transition", args=[work_order.id])
    resp = client.post(url, {"status": "in_progress"}, format="json")
    work_order.refresh_from_db()
    assert resp.status_code == 200
    assert work_order.status == "in_progress"


def test_note_action(client, work_order):
    url = reverse("workorder-note", args=[work_order.id])
    resp = client.post(url, {"detail": "Ordered replacement part"}, format="json")
    assert resp.status_code == 200
    assert WorkOrderEvent.objects.filter(event_type="note_added").exists()
