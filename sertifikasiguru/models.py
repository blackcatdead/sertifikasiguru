from __future__ import unicode_literals

from django.db import models
from django.contrib.humanize.templatetags.humanize import naturalday, naturaltime
from django.utils import timezone
from datetime import datetime, timedelta

class Sekolah(models.Model):
	id_sekolah= models.AutoField(primary_key=True)
	sekolah= models.CharField(max_length=100, null=False, default=None)
	alamat= models.CharField(max_length=200, null=False, default=None)
	telp= models.CharField(max_length=100, null=False, default=None)
	email= models.CharField(max_length=100, null=False, default=None)
	alamat= models.CharField(max_length=200, null=False, default=None)
	jenj= (
        (0, 'None'),
        (1, 'SD'),
        (2, 'SMP'),
        (3, 'SMA'),
    )
	jenjang= models.IntegerField(choices=jenj, null=False, default=1)
	st= (
        (0, 'Deactive'),
        (1, 'Active'),
    )
	status= models.IntegerField(choices=st, null=False, default=1)

	def __str__(self):
		return self.sekolah

class Kepala(models.Model):
	id_kepala= models.AutoField(primary_key=True)
	sekolah= models.ForeignKey(Sekolah, on_delete=models.SET_NULL,null=True)
	kepala= models.CharField(max_length=100, null=False, default=None)
	nip_kepala= models.CharField(max_length=100, null=False, default=None)
	hp= models.CharField(max_length=100, null=False, default=None)
	email= models.CharField(max_length=100, null=False, default=None)
	alamat= models.CharField(max_length=200, null=False, default=None)
	ttd_kepala= models.ImageField(blank=True, null=True, upload_to='ttd')
	st= (
        (0, 'Deactive'),
        (1, 'Active'),
    )
	status= models.IntegerField(choices=st, null=False, default=1)
	def __str__(self):
		return self.kepala

class Guru(models.Model):
	id_guru= models.AutoField(primary_key=True)
	# sekolah= models.ForeignKey(Sekolah, on_delete=models.SET_NULL,null=True)
	guru= models.CharField(max_length=100, null=False, default=None)
	hp= models.CharField(max_length=100, null=False, default=None)
	email= models.CharField(max_length=100, null=False, default=None)
	alamat= models.CharField(max_length=200, null=False, default=None)
	password= models.CharField(max_length=50, null=False, default=None)
	nip_guru= models.CharField(max_length=100, null=False, default=None)
	ttd_guru= models.ImageField(blank=True, null=True, upload_to='ttd')
	st= (
        (0, 'Deactive'),
        (1, 'Active'),
    )
	status= models.IntegerField(choices=st, null=False, default=1)

	def __str__(self):
		return self.guru

class Subject(models.Model):
	id_subject= models.AutoField(primary_key=True)
	subject= models.CharField(max_length=100, null=False, default=None)

	def __str__(self):
		return self.subject

class Paket(models.Model):
	id_paket= models.AutoField(primary_key=True)
	paket= models.CharField(max_length=100, null=False, default=None)

	GRADE_CHOICES = []
	for r in range(1, 13):
	    GRADE_CHOICES.append((r,r))
	grade= models.IntegerField(('grade'), choices=GRADE_CHOICES, default=None)
	subject= models.ForeignKey(Subject, on_delete=models.SET_NULL,null=True)
	YEAR_CHOICES = []
	for r in range((datetime.now().year-5), (datetime.now().year+5)):
	    YEAR_CHOICES.append((r,r))

	year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.now().year)
	sem= (
        (1, 'Ganjil'),
        (2, 'Genap')
    )
	semester= models.IntegerField(choices=sem, null=False, default=None)
	st= (
        (0, 'Deactive'),
        (1, 'Active'),
    )
	status= models.IntegerField(choices=st, null=False, default=1)
	def __str__(self):
		return str(self.id_paket) +' - '+ str(self.grade) +' - '+ str(self.subject) +' - '+ str(self.year) +' - '+ str(self.semester)


class File(models.Model):
	id_file= models.AutoField(primary_key=True)
	paket= models.ForeignKey(Paket, on_delete=models.SET_NULL,null=True)
	file = models.FileField(upload_to='files')
	filename= models.CharField(max_length=100, null=True, default=None)
	
	def __str__(self):
		return str(self.paket) + ' - '+ str(self.filename)

class Order(models.Model):
	id_order= models.AutoField(primary_key=True)
	guru= models.ForeignKey(Guru, on_delete=models.SET_NULL,null=True)
	paket= models.ForeignKey(Paket, on_delete=models.SET_NULL,null=True)
	kepala= models.ForeignKey(Kepala, on_delete=models.SET_NULL,null=True)
	sekolah= models.ForeignKey(Sekolah, on_delete=models.SET_NULL,null=True)
	st= (
        (0, 'Deactive'),
        (1, 'Active'),
    )
	status= models.IntegerField(choices=st, null=False, default=1)

class DetailOrder(models.Model):
	id_detailorder= models.AutoField(primary_key=True)
	order= models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
	file= models.ForeignKey(File, on_delete=models.SET_NULL,null=True)
	st= (
        (0, 'None'),
        (1, 'Waiting'),
        (2, 'Done'),
        (3, 'Failed'),
    )
	status= models.IntegerField(choices=st, null=False, default=None)
	processed= models.CharField(max_length=100, null=True, default=None)

class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
# class Field(models.Model):
# 	file= models.ForeignKey(File, on_delete=models.SET_NULL,null=True)
# 	sem= (
#         (1, 'Guru'),
#         (2, '2'),
#         (3, '2'),
#         (4, '2'),
#     )
# 	semester= models.IntegerField(choices=sem, null=False, default=None)

