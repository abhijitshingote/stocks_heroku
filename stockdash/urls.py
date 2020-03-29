from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [ 

	path('',views.index     ,name='index'),
	path('somefunction/',views.somefunction,name='somefunction'),
	path('huh/',views.huh),
	path('symbol/<slug:symbol>/',views.stockpage,name='stockpage'),
	path('<slug:sector>/',views.top_performers,name='top_performers'),
]
