from django.shortcuts import render
from stockdash.models import PriceHistory,Return1Day,Return30Day
from django.http import JsonResponse,HttpResponse
import json
# Create your views here.

def index(request):
	gainers=Return1Day.objects.using('stockdb').filter(marketcap__gt=10,return_percentage__gt=0).order_by('-return_percentage')[:10]
	losers=Return1Day.objects.using('stockdb').filter(marketcap__gt=10,return_percentage__lt=0).order_by('return_percentage')[:10]
	return render(request,'stockdash/index.html',context={'gainers':gainers,'losers':losers})

def top_performers(request,sector):
	# if sector=='Financials':
	# 	sector='Financial Services'
	gainers=Return1Day.objects.using('stockdb').filter(marketcap__gt=10,sector=sector,return_percentage__gt=0).order_by('-return_percentage')[:10]
	losers=Return1Day.objects.using('stockdb').filter(marketcap__gt=10,sector=sector,return_percentage__lt=0).order_by('return_percentage')[:10]
	return render(request,'stockdash/index.html',context={'gainers':gainers,'losers':losers})

def somefunction(request):
	data={'message':'Your request was pretty successful'}
	# print(HttpResponse(
 #            json.dumps(data),
 #            content_type="application/json"
 #        ))
	# return HttpResponse(
 #            json.dumps(data),
 #            content_type="application/json"
#        )
	if request.is_ajax():
		return HttpResponse(
		json.dumps(data),
		content_type="application/json"
		)

def huh(request):
	# return HttpResponse("Get out")
	print('HUHUHU')
	return render(request,'stockdash/huh.html')