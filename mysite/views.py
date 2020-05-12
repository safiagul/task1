from django.http import HttpResponse
import requests
from django.shortcuts import render
from ipware import get_client_ip


def index(request):
  return render(request, 'index.html')


def sdsu_image(request):
  return render(request, 'sdsu.html')


def ip_api(request):
  ip_address_value = get_client_ip(request)[0]
  response = requests.get("http://ip-api.com/json/{}".format(ip_address_value))
  location = response.json()
  regionName_value = location.get("regionName")
  city_value = location.get("city")
  data = {"ip_address_key": ip_address_value,"city_key":city_value,"regionName_key": regionName_value}
  
  return render(request, 'ip_api.html', context = data)


def headings(request):
  return render(request, "headings.html")


def bold_italic(request):
  return render(request, "bold_italic.html")


def unordered_list(request):
  return render(request, "unordered_list.html")


def simple_table(request):
  return render(request, "simple_table.html")

