from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, TextInput, NumberInput, EmailInput, Select, PasswordInput, FileInput, ImageField, ClearableFileInput
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from sertifikasiguru.models import Guru, Kepala, Sekolah, Paket, Photo, File, Order

class LoginAdminForm(forms.Form):
    username = forms.CharField(label='user', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'blank': True}))
    password = forms.CharField(label='lock', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'blank': True}))

class LoginClientForm(forms.Form):
    email = forms.EmailField(label='envelope', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'blank': True}))
    password = forms.CharField(label='lock', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'blank': True}))

class EditGuruForm(ModelForm):
    class Meta:
        model = Guru
        fields = ['guru', 'nip_guru', 'sekolah', 'email', 'hp', 'password', 'status', 'ttd_guru']
        widgets = {
            'guru': TextInput(attrs={'class': 'form-control', 'placeholder': '*Guru', 'autocomplete': 'off'}),
            'nip_guru': TextInput(attrs={'class': 'form-control text_type_number', 'placeholder': '*NIP', 'autocomplete': 'off'}),
            'sekolah': Select(attrs={'class': 'form-control', 'placeholder': '*Sekolah', 'autocomplete': 'off'}),
            'email': EmailInput(attrs={'class': 'form-control ', 'placeholder': '*Email', 'autocomplete': 'off'}),
            'hp': TextInput(attrs={'class': 'form-control ', 'placeholder': '*Nomor Hp', 'autocomplete': 'off'}),
            'password': TextInput(attrs={'class': 'form-control ', 'placeholder': '*Password', 'autocomplete': 'off'}),
            'status': Select(attrs={'class': 'form-control', 'placeholder': '*Status', 'autocomplete': 'off'}),
        }

class EditSekolahForm(ModelForm):
    class Meta:
        model = Sekolah
        fields = ['sekolah', 'alamat', 'status']
        widgets = {
            'sekolah': TextInput(attrs={'class': 'form-control', 'placeholder': '*Sekolah', 'autocomplete': 'off'}),
            'alamat': TextInput(attrs={'class': 'form-control', 'placeholder': '*Alamat', 'autocomplete': 'off'}),
            'status': Select(attrs={'class': 'form-control', 'placeholder': '*Status', 'autocomplete': 'off'}),
        }

class EditKepalaForm(ModelForm):
    class Meta:
        model = Kepala
        fields = ['kepala', 'nip_kepala', 'sekolah', 'status', 'ttd_kepala']
        widgets = {
            'kepala': TextInput(attrs={'class': 'form-control', 'placeholder': '*Kepala', 'autocomplete': 'off'}),
            'nip_kepala': TextInput(attrs={'class': 'form-control text_type_number', 'placeholder': '*NIP', 'autocomplete': 'off'}),
            'sekolah': Select(attrs={'class': 'form-control', 'placeholder': '*Sekolah', 'autocomplete': 'off'}),
            'status': Select(attrs={'class': 'form-control', 'placeholder': '*Status', 'autocomplete': 'off'}),
        }

class EditPaketForm(ModelForm):
    class Meta:
        model = Paket
        fields = ['paket', 'grade', 'year', 'semester', 'matapelajaran', 'status']
        widgets = {
            'paket': TextInput(attrs={'class': 'form-control', 'placeholder': '*Paket', 'autocomplete': 'off'}),
            'grade': Select(attrs={'class': 'form-control', 'placeholder': '*Grade', 'autocomplete': 'off'}),
            'year': Select(attrs={'class': 'form-control', 'placeholder': '*Year', 'autocomplete': 'off'}),
            'semester': Select(attrs={'class': 'form-control', 'placeholder': '*semester', 'autocomplete': 'off'}),
            'matapelajaran': Select(attrs={'class': 'form-control', 'placeholder': '*Mata Pelajaran', 'autocomplete': 'off'}),
            'status': Select(attrs={'class': 'form-control', 'placeholder': '*Status', 'autocomplete': 'off'}),
        }	

class EditOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['guru', 'sekolah', 'kepala', 'paket', 'status']
        widgets = {
            'guru': Select(attrs={'class': 'form-control', 'placeholder': '*Guru', 'autocomplete': 'off'}),
            'sekolah': Select(attrs={'class': 'form-control', 'placeholder': '*Sekolah', 'autocomplete': 'off'}),
            'kepala': Select(attrs={'class': 'form-control', 'placeholder': '*Kepala', 'autocomplete': 'off'}),
            'paket': Select(attrs={'class': 'form-control', 'placeholder': '*Paket', 'autocomplete': 'off'}),
            'status': Select(attrs={'class': 'form-control', 'placeholder': '*Status', 'autocomplete': 'off'}),
        }

class AddOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['guru', 'sekolah', 'paket', 'status']
        widgets = {
            'guru': Select(attrs={'class': 'form-control', 'placeholder': '*Guru', 'autocomplete': 'off'}),
            'sekolah': Select(attrs={'class': 'form-control', 'placeholder': '*Sekolah', 'autocomplete': 'off'}),
            'paket': Select(attrs={'class': 'form-control', 'placeholder': '*Paket', 'autocomplete': 'off'}),
            'status': Select(attrs={'class': 'form-control', 'placeholder': '*Status', 'autocomplete': 'off'}),
        }  

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file', )

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file', )

class FileFieldForm(ModelForm):
    class Meta:
        model = File
        fields = ['file']
        widgets = {
            'file': FileInput(attrs={'multiple': True}),
        }

class Multiuplodform(forms.Form):
    password = forms.FileField(label='asdasd', widget=forms.FileInput(attrs={'multiple': True}))
