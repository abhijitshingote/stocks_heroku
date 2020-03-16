from django.shortcuts import render
from stockdash.models import PriceHistory,Return1Day,Return30Day,TotalReturn
from django.http import JsonResponse,HttpResponse
import json
# Create your views here.

def index(request):
	gainers=TotalReturn.objects.using('stockdb').filter(marketcap__gt=10,return_1_day__gt=0).order_by('-return_1_day')[:10]
	losers=TotalReturn.objects.using('stockdb').filter(marketcap__gt=10,return_1_day__lt=0).order_by('return_1_day')[:10]
	return render(request,'stockdash/index.html',context={'gainers':gainers,'losers':losers})

def top_performers(request,sector):
	# if sector=='Financials':
	# 	sector='Financial Services'
	gainers=TotalReturn.objects.using('stockdb').filter(marketcap__gt=10,sector=sector,return_1_day__gt=0).order_by('-return_1_day')[:10]
	losers=TotalReturn.objects.using('stockdb').filter(marketcap__gt=10,sector=sector,return_1_day__lt=0).order_by('return_1_day')[:10]
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