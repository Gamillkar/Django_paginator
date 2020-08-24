import csv
import math
from urllib.parse import urlencode
from django.shortcuts import  redirect, render
from django.urls import reverse
from app.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    bus_stations_list = []
    with open(BUS_STATION_CSV, newline='') as file:
        data_bus = list(csv.DictReader(file))
        current_page = int(request.GET.get('page', 1))
        top_el_page = current_page * 10
        first_el_page = top_el_page - 10

        if current_page > 1 :
            prev_page = urlencode({'page': current_page - 1})
            prev_page =  f'bus_stations?{prev_page}'
        else:
            prev_page = None

        if current_page < math.ceil(len(data_bus)/10):
            next_page = urlencode({'page': current_page + 1})
            next_page = f'bus_stations?{next_page}'
        elif current_page == math.ceil(len(data_bus)/10):
            next_page = None
        elif current_page > math.ceil(len(data_bus)/10):
            next_page = None
            top_el_page = math.ceil(len(data_bus)/10)
            first_el_page = top_el_page - 10
            current_page = math.ceil(len(data_bus)/10)

        for row in data_bus[first_el_page:top_el_page]:
            element = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}
            bus_stations_list.append(element)
        context = {
            'bus_stations': bus_stations_list,
            'current_page': current_page,
            'prev_page_url': prev_page,
            'next_page_url': next_page,
        }

    return render(request, 'index.html', context=context)



