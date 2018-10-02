from sertifikasiguru.models import Guru
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class MyCustomBackend:
	def authenticateclient(self, email=None, password=None):
		try:
			client = Guru.objects.get(email=email, password=password)
			if client:
				return client
			else:
				return None
		except Guru.DoesNotExist:
			return None

	def get_client(self, id):
		try:
			return Guru.objects.get(id_guru=id)
		except Guru.DoesNotExist:
			return None

