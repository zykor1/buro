# -*- coding: utf-8 *-*
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from forms import DeudorForm, BuscarCurpForm, BuscarNombreForm
from models import Deudor



def  index(request):
	return render_to_response('index/index.html',  context_instance=RequestContext(request))

@login_required(login_url='/login')
def institutoIndex(request):
    deudores = Deudor.objects.filter(institucion=request.user)
    return render_to_response('deudores/index.html', {'deudores': deudores}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def nuevoDeudor(request):
    if request.method=='POST':
        formulario = DeudorForm(request.POST)
        if formulario.is_valid():
            aux = formulario.save(commit=False)
            aux.institucion = request.user
            aux.save()
            return HttpResponseRedirect('/instituto')
    else:
    	formulario = DeudorForm()
    return render_to_response('deudores/nuevo.html', {'formulario':formulario}, context_instance=RequestContext(request))


def editarDeudor(request, id_deudor):
    deudor = Deudor.objects.get(pk=id_deudor)
    if request.method == 'POST':
        formulario = DeudorForm(request.POST, instance=deudor) # El instance para instanciar la info
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/instituto')
    else:
        formulario = DeudorForm(instance=deudor)
    return render_to_response('deudores/nuevo.html', \
        {'formulario':formulario }, context_instance=RequestContext(request))


def eliminarDeudor(request, id_deudor):
    deudor = Deudor.objects.get(pk=id_deudor)
    deudor.delete()
    return HttpResponseRedirect('/instituto')



def buscadorIndex(request):
    return render_to_response('buscador/index.html', \
                    context_instance=RequestContext(request))

def buscarDeudorCurp(request):
    if request.method == 'POST':
        formulario = BuscarCurpForm(request.POST)
        if formulario.is_valid():
            CURP = formulario.cleaned_data['CURP']
            deudor = Deudor.objects.filter(CURP=CURP)
            if deudor.count() > 0 :
                return render_to_response('buscador/resultados.html', \
                    {'deudores':deudor }, context_instance=RequestContext(request))
            else:
                mensaje = 'No se encontro ningun profesor o alumno con el CURP: %s' % CURP
                return render_to_response('buscador/resultados.html', \
                    {'mensaje':mensaje }, context_instance=RequestContext(request))

    else:
        formulario = BuscarCurpForm()
    return render_to_response('buscador/buscadorCurp.html', \
        {'formulario':formulario }, context_instance=RequestContext(request))


def buscarDeudorNombre(request):
    if request.method == 'POST':
        formulario = BuscarNombreForm(request.POST)
        if formulario.is_valid():
            tipo0 = formulario.cleaned_data['tipo']
            tipo1 = tipo0
            tipo1 = dict(formulario.fields['tipo'].choices)[tipo1]
            nombre1 = formulario.cleaned_data['nombre']
            apepat1 = formulario.cleaned_data['apepat']
            apemat1 = formulario.cleaned_data['apemat']
            fecha = formulario.cleaned_data['fecha_nacimiento']
            deudor = Deudor.objects.filter(\
                Q(Q(nombre=nombre1) & Q(tipo=tipo0) & Q(apepat=apepat1) & Q(apemat=apemat1) & Q(fecha_nacimiento=fecha))\
                | Q(Q(nombre=nombre1) & Q(tipo=tipo0) & Q(fecha_nacimiento=fecha) & Q(apepat=apepat1)) \
                | Q(Q(nombre=nombre1) & Q(tipo=tipo0) & Q(fecha_nacimiento=fecha) & Q(apemat=apemat1)) \
                | Q(Q(nombre=nombre1) & Q(tipo=tipo0) & Q(apepat=apepat1)) \
                | Q(Q(nombre=nombre1) & Q(tipo=tipo0) & Q(apemat=apemat1)) \
                )
            if deudor.count() > 0 :
                return render_to_response('buscador/resultados.html', \
                    {'deudores':deudor }, context_instance=RequestContext(request))
            else:
                mensaje = 'No se encontro al %s con nombre %s %s %s. Verifica tus datos e intentalo de nuevo.' % (tipo1, nombre1, apepat1, apemat1)
                return render_to_response('buscador/resultados.html', \
                    {'mensaje':mensaje }, context_instance=RequestContext(request))

    else:
        formulario = BuscarNombreForm()
    return render_to_response('buscador/buscadorNombre.html', \
        {'formulario':formulario }, context_instance=RequestContext(request))
