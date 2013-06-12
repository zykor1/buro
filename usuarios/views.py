#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext #se agrega para poder utilizar la ruta de los archivos estatic se debe poner en todas las funciones
from django.shortcuts import redirect


from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import Group
from django.contrib.auth.models import User


from forms import SignupForm


def nuevoUserView(request):
	if request.method == 'POST':
		formulario = SignupForm(request.POST)
		if formulario.is_valid():
			username = formulario.cleaned_data['username']
			password = formulario.cleaned_data['password']
			email = formulario.cleaned_data['email']
			new_user = User.objects.create_user(username, email ,password)
			new_user.is_active=True
			new_user.is_staff=False
			new_user.is_superuser=False
			new_user.first_name=formulario.cleaned_data['first_name']
			new_user.save()
			return HttpResponseRedirect('/')
	else:
		mensaje ="Los datos no son validos"
		formulario =SignupForm()
	return render_to_response('usuarios/registro.html',{'formulario': formulario }, \
			context_instance=RequestContext(request))


def login(request):
	print 'hola'
	if request.user.is_authenticated():
		print 'hola'
		return redirect('/')
	else:
		username = request.POST['username']
		password = request.POST['password']
		print 'hola'
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('/')
			else:
				return render_to_response('usuarios/login.html', \
					context_instance=RequestContext(request))
		else:
			return render_to_response('usuarios/login.html', \
				context_instance=RequestContext(request))


@login_required(login_url='/login')
def cerrarSesion(request):
    logout(request)
    return HttpResponseRedirect('/')