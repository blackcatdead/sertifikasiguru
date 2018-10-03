# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from sertifikasiguru.models import Guru, File
from sertifikasiguru.decorators import decoclient
from sertifikasiguru.forms import LoginClientForm
from sertifikasiguru.MyCustomBackend import MyCustomBackend
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def testdocx(request):
	template = loader.get_template('testdocx.html')
	context = {
		'page': 'Informasi',
		'data': 'Main',
	}

	if request.method == 'POST':
		f = open('media/test.docx', 'rb')
		document = Document(f)
		f.close()
		for p in document.paragraphs:
			if 'markng' in p.text or 'markig' in p.text or 'marknk' in p.text or 'markik' in p.text or 'marks' in p.text or 'marka' in p.text:
				inline = p.runs
				for i in range(len(inline)):
					if 'markng' in inline[i].text:
						text = inline[i].text.replace('markng', request.POST['nama_guru'])
						inline[i].text = text
					if 'markig' in inline[i].text:
						text = inline[i].text.replace('markig', request.POST['nip_guru'])
						inline[i].text = text
					if 'marknk' in inline[i].text:
						text = inline[i].text.replace('marknk', request.POST['nama_kepala'])
						inline[i].text = text
					if 'markik' in inline[i].text:
						text = inline[i].text.replace('markik', request.POST['nip_kepala'])
						inline[i].text = text
					if 'marks' in inline[i].text:
						text = inline[i].text.replace('marks', request.POST['sekolah'])
						inline[i].text = text
					if 'marka' in inline[i].text:
						text = inline[i].text.replace('marka', request.POST['alamat'])
						inline[i].text = text

		for table in document.tables:
			for row in table.rows:
				for cell in row.cells:
					for p in cell.paragraphs:
						if 'markng' in p.text or 'markig' in p.text or 'marknk' in p.text or 'markik' in p.text or 'marks' in p.text or 'marka' in p.text or 'ttdg' in p.text or 'ttdk' in p.text or 'markung' in p.text or 'markunk' in p.text:
							inline = p.runs
							for i in range(len(inline)):
								if 'markung' in inline[i].text:
									text = inline[i].text.replace('markung', request.POST['nama_guru'])
									inline[i].text = text
									inline[i].underline = True
								if 'markunk' in inline[i].text:
									text = inline[i].text.replace('markunk', request.POST['nama_kepala'])
									inline[i].text = text
									inline[i].underline = True
								if 'markng' in inline[i].text:
									text = inline[i].text.replace('markng', request.POST['nama_guru'])
									inline[i].text = text
								if 'markig' in inline[i].text:
									text = inline[i].text.replace('markig', request.POST['nip_guru'])
									inline[i].text = text
								if 'marknk' in inline[i].text:
									text = inline[i].text.replace('marknk', request.POST['nama_kepala'])
									inline[i].text = text
								if 'markik' in inline[i].text:
									text = inline[i].text.replace('markik', request.POST['nip_kepala'])
									inline[i].text = text
								if 'marks' in inline[i].text:
									text = inline[i].text.replace('marks', request.POST['sekolah'])
									inline[i].text = text
								if 'marka' in inline[i].text:
									text = inline[i].text.replace('marka', request.POST['alamat'])
									inline[i].text = text
								if 'ttdg' in inline[i].text:
									inline[i].text = ''
									inline[i].add_picture('media/ttd/ijazah_001.jpg')
								if 'ttdk' in inline[i].text:
									inline[i].text = ''
									inline[i].add_picture('media/ttd/ijazah_001.jpg')
								
		# paragraph = document.add_paragraph('Lorem ipsum dolor sit amet.')
		# run = paragraph.add_run()
		# # inline_shape = run.add_inline_picture('media/ttd/23.gif', MIME_type=None)
		# run.add_picture('media/ttd/23.gif')

		response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
		response['Content-Disposition'] = 'attachment; filename=download.docx'
		document.save(response)

		return response

	return HttpResponse(template.render(context, request))

from docx import Document
from docx.shared import Inches

def downloaddocx(request):
	document = Document()
	document.add_heading('Document Title', 0)

	response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
	response['Content-Disposition'] = 'attachment; filename=download.docx'
	document.save(response)

	return response

def readdocx(request):
	document = Document()
	document.add_heading('Document Title', 0)

	response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
	response['Content-Disposition'] = 'attachment; filename=download.docx'
	document.save(response)

	return response

def readwritedocx(request):
	document = Document()
	document.add_heading('Document Title', 0)

	response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
	response['Content-Disposition'] = 'attachment; filename=download.docx'
	document.save(response)

	return response

@decoclient
def dokumen(request):
	template = loader.get_template('client/v_dokumen.html')
	context = {
		'page': 'Dokumen',
		'client': Guru.objects.get(id_guru=request.session['client']),
    }
	return HttpResponse(template.render(context, request))

def login(request):
	template = loader.get_template('client/cl_login.html')
	if request.method == 'POST':
		form = LoginClientForm(request.POST)
		if form.is_valid():
			# form.save()
			mcb=MyCustomBackend()
			# if  mcb.authenticateadmin(form.cleaned_data.get('username'),form.cleaned_data.get('password')):
			client = mcb.authenticateclient(form.cleaned_data.get('email'),form.cleaned_data.get('password'))
			# client = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
			if  client:
				request.session['client'] = client.id_guru
				return redirect('dokumen')
			else:
				messages.error(request, 'Tidak bisa masuk')
				return redirect('masuk')
	else:
		form = LoginClientForm()
	
	# return render(request, 'login.html', {'form': form})
	return HttpResponse(template.render({'form': form}, request))

@decoclient
def logout(request):
	request.session.flush()
	return redirect('dokumen')