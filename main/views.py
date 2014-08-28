from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexVista(request):
	if request.session.get('autenticado', 0) == 0:
		return render(request, 'autenticacion/loginview.html', { })

	if request.session.get('autenticado', 0) == 1:
		return render(request, 'main/recepcionView.html',{})

def ver_calendario(request):
	return HttpResponse('[{ "date": "2014-08-01 17:30:00", "type": "Cita", "title": "Cita medicina general", "description": "", "url": "" }]')
	
def ver_fecha(request):
	if request.method == 'POST':
		fecha = request.POST.get('fecha', 0)
		#return render(request, 'main/verfecha.html', {'fecha':fecha})
		return HttpResponse(fecha)