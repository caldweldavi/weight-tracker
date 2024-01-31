from django import template
from ..models import WeightRecord

register = template.Library()

@register.simple_tag
def total_records():
    return WeightRecord.objects.all().count()

@register.simple_tag
def latest_recorded_weight():
    return WeightRecord.objects.latest("date_recorded").weight

@register.simple_tag
def lowest_recorded_weight():
    return WeightRecord.objects.order_by("weight").first().weight

@register.simple_tag
def highest_recorded_weight():
    return WeightRecord.objects.order_by("-weight").first().weight

