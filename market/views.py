from django.shortcuts import render
import json, requests
from requests.exceptions import HTTPError


# Create your views here.

##pk_
##https://iexcloud.io/docs/api/



def home(request):
    api_key= ''
    proxies = {
        "http": "http://192.168.191.242:8080",
        "https": "http://192.168.191.242:8080",
     }

    if request.method == 'GET':
        try:
            api_data = requests.get("https://cloud.iexapis.com/stable/stock/fb/quote?token="+api_key,proxies=proxies)
            api_data.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')   
        
        
        try:
            api = json.loads(api_data.content)
        except Exception as e:
            api = "Error 404"
            return render(request,'error.html', {"api": api})
   
        serrching_data = { 
            "Symbol": api['symbol'],
            "Company Name": api['companyName'],  
            "Primary Exchange": api['primaryExchange'], 
            "Latest Stock Price": api['latestPrice'],
            "Latest Time": api['latestTime'],
            "Previous Close": api['previousClose'],
            "Change": api['change'],
            "Change Percent": api['changePercent'],
            "Week 52 High": api['week52High'],
            "Week 52 Low": api['week52Low'],
            "Market Capital": api['marketCap'] }

        return render(request,'home.html', {"api_data": serrching_data, "api": api})

    if request.method == 'POST':
        company = request.POST['company'].lower()
        try:
            api_data = requests.get("https://cloud.iexapis.com/stable/stock/"+company+"/quote?token="+api_key,proxies=proxies)
            api_data.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')   
        
        
        try:
            api = json.loads(api_data.content)
        except Exception as e:
            api = "Error 404 the searched term " + company + " not found"
            return render(request,'error.html', {"api": api})
        
        serrching_data = { 
            "Symbol": api['symbol'],
            "Company Name": api['companyName'],  
            "Primary Exchange": api['primaryExchange'], 
            "Latest Stock Price": api['latestPrice'],
            "Latest Time": api['latestTime'],
            "Previous Close": api['previousClose'],
            "Change": api['change'],
            "Change Percent": api['changePercent'],
            "Week 52 High": api['week52High'],
            "Week 52 Low": api['week52Low'],
            "Market Capital": api['marketCap'] }

        return render(request,'home.html', {"api_data": serrching_data, "api": api})

        

def about(request):
    return render(request,'about.html', {})


def error(request):
    return render(request,'error.html', {})