from django.shortcuts import render,redirect
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
from .models import Link
# Create your views here.

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def scrape(request):
    url = 'https://hprera.nic.in/PublicDashboard'
    base_url = 'https://hprera.nic.in'

    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.text, 'html.parser')

    project_table = soup.find('div', {'class': 'tab-pane fade show active'})
    
    if project_table is None:
        print("Table not found")
        return render(request, 'myapp/result.html', {'data': []})
    
    projects = project_table.find_all('tr')[1:7]

    
    Link.objects.all().delete()

    for project in projects:
        rera_link = project.find('a')['href']
        detail_url = base_url + rera_link

        detail_page = requests.get(detail_url, verify=False)
        detail_soup = BeautifulSoup(detail_page.text, 'html.parser')

        try:
            gstin_no = detail_soup.find('span', id='lblGSTIN').text.strip()
        except AttributeError:
            gstin_no = None

        try:
            pan_no = detail_soup.find('span', id='lblPAN').text.strip()
        except AttributeError:
            pan_no = None

        try:
            name = detail_soup.find('span', id='lblPromoterName').text.strip()
        except AttributeError:
            name = None

        try:
            permanent_address = detail_soup.find('span', id='lblPromoterAddress').text.strip()
        except AttributeError:
            permanent_address = None

        print(f"Detail URL: {detail_url}")
        print(f"Name: {name}, GSTIN No: {gstin_no}, PAN No: {pan_no}, Permanent Address: {permanent_address}")

        Link.objects.create(
            address=detail_url,
            name=name,
            gstin_no=gstin_no,
            pan_no=pan_no,
            permanent_address=permanent_address
        )

    data = Link.objects.all()
    for link in data:
        print(f"Link: {link}")

    return render(request, 'myapp/result.html', {'data': data})