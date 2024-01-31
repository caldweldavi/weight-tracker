from requests import get
from django.shortcuts import render, redirect
from django.http import Http404
from .models import WeightRecord

def weight_record_list(request):
    weight_records = WeightRecord.objects.all()
    return render(request, 'tracker/weight_record/list.html', {'weight_records': weight_records})

def weight_record_detail(request, slug):
    try:
        weight_record = WeightRecord.objects.get(slug=slug)
    except WeightRecord.DoesNotExist:
        raise Http404("No Weight Record found!")
    return render(request, 'tracker/weight_record/detail.html', {'weight_record': weight_record})

def import_weight_records(request):
    if request.method == "POST":
        entries = fetch_libra_data("token")
        for entry in entries:
            WeightRecord.objects.create(**entry)
        return render(request, "tracker/weight_record/import.html")
    return render(request, "tracker/weight_record/import.html")

def fetch_libra_data(token):
    url = "https://api.libra-app.eu/values/weight"
    headers = {"Authorization": f"Bearer {token}"}
    response = get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    return [
        {"weight": entry["weight"], "body_fat": entry["body_fat"], "date_recorded": entry["date"][:10], "slug": entry["date"][:10]}
        for entry in data["values"]
    ]