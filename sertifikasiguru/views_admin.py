# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from sertifikasiguru.forms import LoginAdminForm, EditGuruForm, EditSekolahForm, EditKepalaForm, EditPaketForm, Multiuplodform, FileForm, EditOrderForm, AddOrderForm
from django.contrib.auth import authenticate
from django.contrib import messages
from sertifikasiguru.decorators import decoadmin
from django.contrib.auth.models import User
from sertifikasiguru.models import Guru, Order, Sekolah, Kepala, Paket, File, Order, DetailOrder
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers


from django.views.generic.edit import FormView
from sertifikasiguru.forms import FileFieldForm
@decoadmin
class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = '...'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

@decoadmin
def home(request):
	template = loader.get_template('admin/adm_base.html')
	context = {
		# 'page': 'Admin Home',
		'admin': User.objects.get(id=request.session['admin']),
    }
	return HttpResponse(template.render(context, request))

def login(request):
	template = loader.get_template('admin/adm_login.html')
	if request.method == 'POST':
		form = LoginAdminForm(request.POST)
		if form.is_valid():
			# form.save()
			# mcb=MyCustomBackend()
			# if  mcb.authenticateadmin(form.cleaned_data.get('username'),form.cleaned_data.get('password')):
			user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
			if  user:
				request.session['admin'] = user.id
				return redirect('admin')
			else:
				messages.error(request, 'Tidak bisa masuk')
				return redirect('adminmasuk')
	else:
		form = LoginAdminForm()
	
	# return render(request, 'login.html', {'form': form})
	return HttpResponse(template.render({'form': form}, request))

@decoadmin
def logout(request):
	request.session.flush()
	return redirect('admin')

@decoadmin
def guru(request):
	template = loader.get_template('admin/v_guru.html')
	context = {
		'page': 'Guru',
		'admin': User.objects.get(id=request.session['admin']),
    }
	return HttpResponse(template.render(context, request))

@decoadmin
def addguru(request):
	template = loader.get_template('admin/v_guru_edit.html')
	if request.method == 'POST':
		form = EditGuruForm(request.POST, request.FILES)
		if form.is_valid():
			ne = form.save(commit=False)
			ne.save()
			messages.success(request, 'Berhasil mendaftarkan Guru baru #'+str(ne.id_guru))
			return redirect('guru')
	else:
		form = EditGuruForm()
	return HttpResponse(template.render({'form': form,'page': 'Tambah Guru', 'admin': User.objects.get(id=request.session['admin'])}, request))


@decoadmin
def editguru(request):
	instance = get_object_or_404(Guru, id_guru=request.GET['id'])
	template = loader.get_template('admin/v_guru_edit.html')
	if request.method == 'POST':
		form = EditGuruForm(request.POST, request.FILES, instance=instance)
		if form.is_valid():
			form.save()
			messages.success(request, 'Berhasil merubah Guru #'+str(request.GET['id']))
			return redirect('guru')
	else:
		form = EditGuruForm(instance=instance)
	return HttpResponse(template.render({'form': form,'page': 'Ubah Guru', 'admin': User.objects.get(id=request.session['admin']), 'guru': instance}, request))


@decoadmin
def removeguru(request):
	instance = get_object_or_404(Guru, id_guru=request.GET['id'])
	template = loader.get_template('admin/v_guru_hapus.html')
	context = {'page': 'Hapus Guru', 'admin': User.objects.get(id=request.session['admin']), 'guru':instance}
	if request.method == 'POST':
		jaw = Order.objects.filter(guru=instance)
		jaw.delete()
		instance.delete()
		messages.success(request, 'Berhasil menghapus guru #'+str(request.POST['hapus']))
		return redirect('guru')
	else:
		return HttpResponse(template.render(context, request))


@decoadmin
def sekolah(request):
	template = loader.get_template('admin/v_sekolah.html')
	context = {
		'page': 'Sekolah',
		'admin': User.objects.get(id=request.session['admin']),
    }
	return HttpResponse(template.render(context, request))


@decoadmin
def addsekolah(request):
	template = loader.get_template('admin/v_sekolah_edit.html')
	if request.method == 'POST':
		form = EditSekolahForm(request.POST, request.FILES)
		if form.is_valid():
			ne = form.save(commit=False)
			ne.save()
			messages.success(request, 'Berhasil menambahkan Sekolah baru #'+str(ne.id_guru))
			return redirect('sekolah')
	else:
		form = EditSekolahForm()
	return HttpResponse(template.render({'form': form,'page': 'Tambah Sekolah', 'admin': User.objects.get(id=request.session['admin'])}, request))

@decoadmin
def editsekolah(request):
	instance = get_object_or_404(Sekolah, id_sekolah=request.GET['id'])
	template = loader.get_template('admin/v_sekolah_edit.html')
	if request.method == 'POST':
		form = EditSekolahForm(request.POST, request.FILES, instance=instance)
		if form.is_valid():
			form.save()
			messages.success(request, 'Berhasil merubah Sekolah #'+str(request.GET['id']))
			return redirect('sekolah')
	else:
		form = EditSekolahForm(instance=instance)
	return HttpResponse(template.render({'form': form,'page': 'Ubah Sekolah', 'admin': User.objects.get(id=request.session['admin']), 'sekolah': instance}, request))

@decoadmin
def removesekolah(request):
	instance = get_object_or_404(Sekolah, id_sekolah=request.GET['id'])
	template = loader.get_template('admin/v_sekolah_hapus.html')
	context = {'page': 'Hapus Sekolah', 'admin': User.objects.get(id=request.session['admin']), 'sekolah':instance}
	if request.method == 'POST':
		jaw = Kepala.objects.filter(sekolah=instance)
		jaw.delete()
		instance.delete()
		messages.success(request, 'Berhasil menghapus sekolah #'+str(request.POST['hapus']))
		return redirect('sekolah')
	else:
		return HttpResponse(template.render(context, request))


@decoadmin
def kepala(request):
	template = loader.get_template('admin/v_kepala.html')
	context = {
		'page': 'Kepala',
		'admin': User.objects.get(id=request.session['admin']),
    }
	return HttpResponse(template.render(context, request))

@decoadmin
def addkepala(request):
	template = loader.get_template('admin/v_kepala_edit.html')
	if request.method == 'POST':
		form = EditKepalaForm(request.POST, request.FILES)
		if form.is_valid():
			ne = form.save(commit=False)
			ne.save()
			messages.success(request, 'Berhasil menambahkan Kepala baru #'+str(ne.id_kepala))
			return redirect('kepala')
	else:
		form = EditKepalaForm()
	return HttpResponse(template.render({'form': form,'page': 'Tambah Kepala', 'admin': User.objects.get(id=request.session['admin'])}, request))

@decoadmin
def editkepala(request):
	instance = get_object_or_404(Kepala, id_kepala=request.GET['id'])
	template = loader.get_template('admin/v_kepala_edit.html')
	if request.method == 'POST':
		form = EditKepalaForm(request.POST, request.FILES, instance=instance)
		if form.is_valid():
			form.save()
			messages.success(request, 'Berhasil merubah Kepala #'+str(request.GET['id']))
			return redirect('kepala')
	else:
		form = EditKepalaForm(instance=instance)
	return HttpResponse(template.render({'form': form,'page': 'Ubah Kepala', 'admin': User.objects.get(id=request.session['admin']), 'sekolah': instance}, request))

@decoadmin
def removekepala(request):
	instance = get_object_or_404(Kepala, id_kepala=request.GET['id'])
	template = loader.get_template('admin/v_kepala_hapus.html')
	context = {'page': 'Hapus Kepala', 'admin': User.objects.get(id=request.session['admin']), 'kepala':instance}
	if request.method == 'POST':
		instance.delete()
		messages.success(request, 'Berhasil menghapus kepala #'+str(request.POST['hapus']))
		return redirect('kepala')
	else:
		return HttpResponse(template.render(context, request))


@decoadmin
def paket(request):
	template = loader.get_template('admin/v_paket.html')
	context = {
		'page': 'Paket',
		'admin': User.objects.get(id=request.session['admin']),
    }
	return HttpResponse(template.render(context, request))

@decoadmin
def addpaket(request):
	template = loader.get_template('admin/v_paket_edit.html')
	if request.method == 'POST':
		form = EditPaketForm(request.POST, request.FILES)
		if form.is_valid():
			ne = form.save(commit=False)
			ne.save()
			messages.success(request, 'Berhasil menambahkan Paket baru #'+str(ne.id_kepala))
			return redirect('paket')
	else:
		form = EditPaketForm()
	return HttpResponse(template.render({'form': form,'page': 'Tambah Paket', 'admin': User.objects.get(id=request.session['admin'])}, request))

@decoadmin
def editpaket(request):
	instance = get_object_or_404(Paket, id_paket=request.GET['id'])
	template = loader.get_template('admin/v_paket_edit.html')
	if request.method == 'POST':
		form = EditPaketForm(request.POST, request.FILES, instance=instance)
		if form.is_valid():
			form.save()
			messages.success(request, 'Berhasil merubah Paket #'+str(request.GET['id']))
			return redirect('paket')
	else:
		form = EditPaketForm(instance=instance)
	return HttpResponse(template.render({'form': form,'page': 'Ubah Paket', 'admin': User.objects.get(id=request.session['admin']), 'paket': instance}, request))

@decoadmin
def removepaket(request):
	instance = get_object_or_404(Paket, id_paket=request.GET['id'])
	template = loader.get_template('admin/v_paket_hapus.html')
	context = {'page': 'Hapus Paket', 'admin': User.objects.get(id=request.session['admin']), 'paket':instance}
	if request.method == 'POST':
		instance.delete()
		messages.success(request, 'Berhasil menghapus Paket #'+str(request.POST['hapus']))
		return redirect('paket')
	else:
		return HttpResponse(template.render(context, request))

@decoadmin
def detailpaket(request):
	instance = get_object_or_404(Paket, id_paket=request.GET['id'])
	template = loader.get_template('admin/v_paket_detail.html')
	if request.method == 'POST':
		form = Multiuplodform(request.FILES)
		if form.is_valid():
			# ne = form.save(commit=False)
			# ne.save()
			# messages.success(request, 'Berhasil menambahkan Detail baru #'+str(ne.id_file))
			print(request.FILES)
			return redirect('paket')
	else:
		form = FileFieldForm()
	return HttpResponse(template.render({'form': form,'page': 'Detail Paket', 'admin': User.objects.get(id=request.session['admin']), 'files': File.objects.all().order_by('-id_file'), 'paket': instance}, request))


@decoadmin
def order(request):
	template = loader.get_template('admin/v_order.html')
	context = {
		'page': 'Order',
		'admin': User.objects.get(id=request.session['admin']),
    }
	return HttpResponse(template.render(context, request))

@decoadmin
def addorder(request):
	template = loader.get_template('admin/v_order_edit.html')
	if request.method == 'POST':
		form = AddOrderForm(request.POST, request.FILES)
		if form.is_valid():
			ne = form.save(commit=False)
			ne.kepala=Kepala.objects.filter(sekolah=Sekolah.objects.get(id_sekolah=ne.sekolah.id_sekolah)).order_by('-id_kepala')[0]
			ne.save()
			files = File.objects.filter(paket = ne.paket)
			for f in files:
				do = DetailOrder(file=f, order=ne, status=1)
				do.save()
			messages.success(request, 'Berhasil menambahkan Order baru #'+str(ne.id_order))
			return redirect('order')
	else:
		form = AddOrderForm()
	return HttpResponse(template.render({'form': form,'page': 'Tambah Order', 'admin': User.objects.get(id=request.session['admin'])}, request))

@decoadmin
def editorder(request):
	instance = get_object_or_404(Order, id_order=request.GET['id'])
	template = loader.get_template('admin/v_order_edit.html')
	if request.method == 'POST':
		form = EditOrderForm(request.POST, request.FILES, instance=instance)
		if form.is_valid():
			form.save()
			messages.success(request, 'Berhasil merubah Order #'+str(request.GET['id']))
			return redirect('order')
	else:
		form = EditOrderForm(instance=instance)
	return HttpResponse(template.render({'form': form,'page': 'Ubah Order', 'admin': User.objects.get(id=request.session['admin']), 'order': instance}, request))

@decoadmin
def removeorder(request):
	instance = get_object_or_404(Order, id_order=request.GET['id'])
	template = loader.get_template('admin/v_order_hapus.html')
	context = {'page': 'Hapus Order', 'admin': User.objects.get(id=request.session['admin']), 'order':instance}
	if request.method == 'POST':
		instance.delete()
		messages.success(request, 'Berhasil menghapus Order #'+str(request.POST['hapus']))
		return redirect('order')
	else:
		return HttpResponse(template.render(context, request))

@decoadmin
def detailorder(request):
	instance = get_object_or_404(Order, id_order=request.GET['id'])
	template = loader.get_template('admin/v_order_detail.html')
	if request.method == 'POST':
		form = Multiuplodform(request.FILES)
		if form.is_valid():
			# ne = form.save(commit=False)
			# ne.save()
			# messages.success(request, 'Berhasil menambahkan Detail baru #'+str(ne.id_file))
			print(request.FILES)
			return redirect('order')
	else:
		form = FileFieldForm()
	return HttpResponse(template.render({'form': form,'page': 'Detail Order', 'admin': User.objects.get(id=request.session['admin']), 'files': DetailOrder.objects.filter(order = instance).order_by('-id_detailorder'), 'order': instance}, request))


@csrf_exempt
@decoadmin
def table_guru(request):
	response_data = {}

	ord= '-id_guru'
	if request.POST.get("sort[id]", ""):
		ord= '-id_guru' if request.POST.get("sort[id]", "")=='desc' else 'id_guru'
	elif request.POST.get("sort[guru]", ""):
		ord= '-guru' if request.POST.get("sort[guru]", "")=='desc' else 'guru'
	elif request.POST.get("sort[nip_guru]", ""):
		ord= '-nip_guru' if request.POST.get("sort[nip_guru]", "")=='desc' else 'nip_guru'
	elif request.POST.get("sort[email]", ""):
		ord= '-email' if request.POST.get("sort[email]", "")=='desc' else 'email'
	elif request.POST.get("sort[hp]", ""):
		ord= '-hp' if request.POST.get("sort[hp]", "")=='desc' else 'hp'
	elif request.POST.get("sort[status]", ""):
		ord= '-status' if request.POST.get("sort[status]", "")=='desc' else 'status'

	data_posts= Guru.objects.filter(guru__icontains=request.POST.get("searchPhrase", "")).all().order_by(ord) 
	response_data['total'] = data_posts.count()
	current= (int(request.POST.get("current", "1"))*int(request.POST.get("rowCount", "10")))-int(request.POST.get("rowCount", "10"))
	rowcount=  (str(response_data['total']) if request.POST.get("rowCount", "10") == '-1' else current+int(request.POST.get("rowCount", "10")))
	response_data['current'] = int(request.POST.get("current", "0"))
	response_data['rowCount'] = int(request.POST.get("rowCount", "10"))

	data = serializers.serialize("python", data_posts[int(current) : int(rowcount)])
	rows=[]
	rowscount=0
	
	for x in data:
		dt={}
		dt['id']=x['pk']
		dt['guru']=x['fields']['guru']
		dt['nip_guru']=x['fields']['nip_guru']
		dt['email']=x['fields']['email']
		dt['hp']=x['fields']['hp']
		clas2= 'blue' if x['fields']['status']==1 else 'danger'
		dt['status']='<span class="badge bg-'+clas2+'">'+('Active' if x['fields']['status']==1 else 'Deactive')+'</span>'

		rows.append(dt)
		rowscount += 1
		pass
	response_data['rows']=rows
	return JsonResponse(response_data, safe=False)

@csrf_exempt
@decoadmin
def table_sekolah(request):
	response_data = {}

	ord= '-id_sekolah'
	if request.POST.get("sort[id]", ""):
		ord= '-id_sekolah' if request.POST.get("sort[id]", "")=='desc' else 'id_sekolah'
	elif request.POST.get("sort[sekolah]", ""):
		ord= '-sekolah' if request.POST.get("sort[sekolah]", "")=='desc' else 'sekolah'
	elif request.POST.get("sort[status]", ""):
		ord= '-status' if request.POST.get("sort[status]", "")=='desc' else 'status'

	data_posts= Sekolah.objects.filter(sekolah__icontains=request.POST.get("searchPhrase", "")).all().order_by(ord) 
	response_data['total'] = data_posts.count()
	current= (int(request.POST.get("current", "1"))*int(request.POST.get("rowCount", "10")))-int(request.POST.get("rowCount", "10"))
	rowcount=  (str(response_data['total']) if request.POST.get("rowCount", "10") == '-1' else current+int(request.POST.get("rowCount", "10")))
	response_data['current'] = int(request.POST.get("current", "0"))
	response_data['rowCount'] = int(request.POST.get("rowCount", "10"))

	data = serializers.serialize("python", data_posts[int(current) : int(rowcount)])
	rows=[]
	rowscount=0
	
	for x in data:
		dt={}
		dt['id']=x['pk']
		dt['sekolah']=x['fields']['sekolah']
		clas2= 'blue' if x['fields']['status']==1 else 'danger'
		dt['status']='<span class="badge bg-'+clas2+'">'+('Active' if x['fields']['status']==1 else 'Deactive')+'</span>'

		rows.append(dt)
		rowscount += 1
		pass
	response_data['rows']=rows
	return JsonResponse(response_data, safe=False)


@csrf_exempt
@decoadmin
def table_kepala(request):
	d_sekolah = {}
	for sek in Sekolah.objects.all():
			d_sekolah[sek.id_sekolah]= sek.sekolah
	

	response_data = {}

	ord= '-id_kepala'
	if request.POST.get("sort[id]", ""):
		ord= '-id_kepala' if request.POST.get("sort[id]", "")=='desc' else 'id_kepala'
	elif request.POST.get("sort[kepala]", ""):
		ord= '-kepala' if request.POST.get("sort[kepala]", "")=='desc' else 'kepala'
	elif request.POST.get("sort[nip_kepala]", ""):
		ord= '-nip_kepala' if request.POST.get("sort[nip_kepala]", "")=='desc' else 'nip_kepala'
	elif request.POST.get("sort[status]", ""):
		ord= '-status' if request.POST.get("sort[status]", "")=='desc' else 'status'

	data_posts= Kepala.objects.filter(kepala__icontains=request.POST.get("searchPhrase", "")).all().order_by(ord) 
	response_data['total'] = data_posts.count()
	current= (int(request.POST.get("current", "1"))*int(request.POST.get("rowCount", "10")))-int(request.POST.get("rowCount", "10"))
	rowcount=  (str(response_data['total']) if request.POST.get("rowCount", "10") == '-1' else current+int(request.POST.get("rowCount", "10")))
	response_data['current'] = int(request.POST.get("current", "0"))
	response_data['rowCount'] = int(request.POST.get("rowCount", "10"))

	data = serializers.serialize("python", data_posts[int(current) : int(rowcount)])
	rows=[]
	rowscount=0
	
	for x in data:
		dt={}
		dt['id']=x['pk']
		dt['kepala']=x['fields']['kepala']
		dt['sekolah']= d_sekolah[x['fields']['sekolah']] if x['fields']['sekolah'] else '-' 
		dt['nip_kepala']=x['fields']['nip_kepala']
		clas2= 'blue' if x['fields']['status']==1 else 'danger'
		dt['status']='<span class="badge bg-'+clas2+'">'+('Active' if x['fields']['status']==1 else 'Deactive')+'</span>'

		rows.append(dt)
		rowscount += 1
		pass
	response_data['rows']=rows
	return JsonResponse(response_data, safe=False)

@csrf_exempt
@decoadmin
def table_paket(request):
	response_data = {}

	ord= '-id_paket'
	if request.POST.get("sort[id]", ""):
		ord= '-id_paket' if request.POST.get("sort[id]", "")=='desc' else 'id_paket'
	elif request.POST.get("sort[paket]", ""):
		ord= '-paket' if request.POST.get("sort[paket]", "")=='desc' else 'paket'
	elif request.POST.get("sort[status]", ""):
		ord= '-status' if request.POST.get("sort[status]", "")=='desc' else 'status'

	data_posts= Paket.objects.filter(paket__icontains=request.POST.get("searchPhrase", "")).all().order_by(ord) 
	response_data['total'] = data_posts.count()
	current= (int(request.POST.get("current", "1"))*int(request.POST.get("rowCount", "10")))-int(request.POST.get("rowCount", "10"))
	rowcount=  (str(response_data['total']) if request.POST.get("rowCount", "10") == '-1' else current+int(request.POST.get("rowCount", "10")))
	response_data['current'] = int(request.POST.get("current", "0"))
	response_data['rowCount'] = int(request.POST.get("rowCount", "10"))

	data = serializers.serialize("python", data_posts[int(current) : int(rowcount)])
	rows=[]
	rowscount=0
	
	for x in data:
		dt={}
		dt['id']=x['pk']
		dt['paket']=x['fields']['paket']
		clas2= 'blue' if x['fields']['status']==1 else 'danger'
		dt['status']='<span class="badge bg-'+clas2+'">'+('Active' if x['fields']['status']==1 else 'Deactive')+'</span>'

		rows.append(dt)
		rowscount += 1
		pass
	response_data['rows']=rows
	return JsonResponse(response_data, safe=False)

@csrf_exempt
@decoadmin
def table_order(request):
	d_kepala = {}
	for kep in Kepala.objects.all():
		d_kepala[kep.id_kepala]= kep.kepala

	d_sekolah = {}
	for sek in Sekolah.objects.all():
		d_sekolah[sek.id_sekolah]= sek.sekolah

	d_paket = {}
	for pak in Paket.objects.all():
		d_paket[pak.id_paket]= pak.paket

	d_guru = {}
	for gur in Guru.objects.all():
		d_guru[gur.id_guru]= gur.guru

	response_data = {}

	ord= '-id_order'
	if request.POST.get("sort[id]", ""):
		ord= '-id_order' if request.POST.get("sort[id]", "")=='desc' else 'id_order'
	elif request.POST.get("sort[guru]", ""):
		ord= '-guru' if request.POST.get("sort[guru]", "")=='desc' else 'guru'
	elif request.POST.get("sort[sekolah]", ""):
		ord= '-sekolah' if request.POST.get("sort[sekolah]", "")=='desc' else 'sekolah'
	elif request.POST.get("sort[kepala]", ""):
		ord= '-kepala' if request.POST.get("sort[kepala]", "")=='desc' else 'kepala'
	elif request.POST.get("sort[kepala]", ""):
		ord= '-paket' if request.POST.get("sort[paket]", "")=='desc' else 'paket'
	elif request.POST.get("sort[status]", ""):
		ord= '-status' if request.POST.get("sort[status]", "")=='desc' else 'status'

	data_posts= Order.objects.filter(guru__guru__icontains=request.POST.get("searchPhrase", "")).all().order_by(ord) 
	response_data['total'] = data_posts.count()
	current= (int(request.POST.get("current", "1"))*int(request.POST.get("rowCount", "10")))-int(request.POST.get("rowCount", "10"))
	rowcount=  (str(response_data['total']) if request.POST.get("rowCount", "10") == '-1' else current+int(request.POST.get("rowCount", "10")))
	response_data['current'] = int(request.POST.get("current", "0"))
	response_data['rowCount'] = int(request.POST.get("rowCount", "10"))

	data = serializers.serialize("python", data_posts[int(current) : int(rowcount)])
	rows=[]
	rowscount=0
	
	for x in data:
		dt={}
		dt['id']=x['pk']
		dt['guru']= d_guru[x['fields']['guru']] if x['fields']['guru'] else '-' 
		dt['kepala']= d_kepala[x['fields']['kepala']] if x['fields']['kepala'] else '-' 
		dt['sekolah']= d_sekolah[x['fields']['sekolah']] if x['fields']['sekolah'] else '-' 
		dt['paket']= d_paket[x['fields']['paket']] if x['fields']['paket'] else '-' 
		clas2= 'blue' if x['fields']['status']==1 else 'danger'
		dt['status']='<span class="badge bg-'+clas2+'">'+('Active' if x['fields']['status']==1 else 'Deactive')+'</span>'

		rows.append(dt)
		rowscount += 1
		pass
	response_data['rows']=rows
	return JsonResponse(response_data, safe=False)

@csrf_exempt
@decoadmin
def basicupload(request):
	id_pa = request.GET.get('id_paket')
	form = FileForm(request.POST, request.FILES)
	if form.is_valid():
		f = form.save(commit=False)
		f.paket=Paket.objects.get(id_paket=id_pa)
		f.save()
		data = {'is_valid': True, 'name': f.filename, 'url': f.file.url, 'id_file': f.id_file}
	else:
	    data = {'is_valid': False}
	return JsonResponse(data)

@csrf_exempt
@decoadmin
def xfilename(request):
	response_data = {}

	if request.method == 'POST':
		if 'filename' in request.POST.get("name"):
			f = File.objects.get(id_file=request.POST.get("pk"))
			f.filename=request.POST.get("value")
			f.save()
			print(f)

	return JsonResponse(response_data)

from django.urls import reverse
from django.http import HttpResponseRedirect
def removefile(request):
	instance = get_object_or_404(File, id_file=request.GET['id'])
	if request.method == 'GET':
		instance.delete()
		return HttpResponseRedirect(reverse('detailpaket') + '?id='+request.GET['id_paket'])
	else:
		return HttpResponseRedirect(reverse('detailpaket') + '?id='+request.GET['id_paket'])


def removeAllfilePaket(request):
	# instance = get_object_or_404(File, id_paket=request.GET['id'])
	if request.method == 'GET':
		File.objects.filter(paket=Paket.objects.get(id_paket=request.GET['id'])).delete()
		return HttpResponseRedirect(reverse('detailpaket') + '?id='+request.GET['id_paket'])
	else:
		return HttpResponseRedirect(reverse('detailpaket') + '?id='+request.GET['id_paket'])