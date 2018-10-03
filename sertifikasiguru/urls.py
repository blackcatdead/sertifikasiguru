"""sertifikasiguru URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sertifikasiguru import views as piuw
from sertifikasiguru import views_admin as adm
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^$', piuw.dokumen, name='dokumen'),
    url(r'^masuk/?', piuw.login, name='masuk'),
    url(r'^keluar/?', piuw.logout, name='keluar'),
    url(r'^test$', piuw.testdocx, name='testdocx'),
    url(r'^downloaddocx/', piuw.downloaddocx, name='downloaddocx'),
    url(r'^readdocx/', piuw.readdocx, name='readdocx'),
    url(r'^readwritedocx/', piuw.readwritedocx, name='readwritedocx'),

    path('admin2/guru/', adm.guru, name='guru'),
    path('admin2/tambahguru/', adm.addguru, name='tambahguru'),
    path('admin2/ubahguru/', adm.editguru, name='ubahguru'),
    path('admin2/hapusguru/', adm.removeguru, name='hapusguru'),

     path('admin2/subject/', adm.subject, name='subject'),
    path('admin2/tambahsubject/', adm.addsubject, name='tambahsubject'),
    path('admin2/ubahsubject/', adm.editsubject, name='ubahsubject'),
    path('admin2/hapussubject/', adm.removesubject, name='hapussubject'),

    path('admin2/sekolah/', adm.sekolah, name='sekolah'),
    path('admin2/tambahsekolah/', adm.addsekolah, name='tambahsekolah'),
    path('admin2/ubahgsekolah/', adm.editsekolah, name='ubahsekolah'),
    path('admin2/hapussekolah/', adm.removesekolah, name='hapussekolah'),

    path('admin2/kepala/', adm.kepala, name='kepala'),
    path('admin2/tambahkepala/', adm.addkepala, name='tambahkepala'),
    path('admin2/ubahkepala/', adm.editkepala, name='ubahkepala'),
    path('admin2/hapuskepala/', adm.removekepala, name='hapuskepala'),

    path('admin2/paket/', adm.paket, name='paket'),
    path('admin2/tampahpaket/', adm.addpaket, name='tambahpaket'),
    path('admin2/ubahpaket/', adm.editpaket, name='ubahpaket'),
    path('admin2/hapuspaket/', adm.removepaket, name='hapuspaket'),
    path('admin2/detailpaket/', adm.detailpaket, name='detailpaket'),

    path('admin2/order/', adm.order, name='order'),
    path('admin2/tampahorder/', adm.addorder, name='tambahorder'),
    path('admin2/ubahorder/', adm.editorder, name='ubahorder'),
    path('admin2/hapusorder/', adm.removeorder, name='hapusorder'),
    path('admin2/detailorder/', adm.detailorder, name='detailorder'),

    path('admin2/hapusfile/', adm.removefile, name='hapusfile'),

	path('admin2/', adm.home, name='admin'),
	path('adminmasuk/', adm.login, name='adminmasuk'),
	path('adminkeluar/', adm.logout, name='adminkeluar'),

    path('ajax/table_guru/', adm.table_guru, name='table_guru'),
    path('ajax/table_subject/', adm.table_subject, name='table_subject'),
    path('ajax/table_sekolah/', adm.table_sekolah, name='table_sekolah'),
    path('ajax/table_kepala/', adm.table_kepala, name='table_kepala'),
    path('ajax/table_paket/', adm.table_paket, name='table_paket'),
    path('ajax/table_order/', adm.table_order, name='table_order'),
    path('ajax/basicupload/', adm.basicupload, name='basicupload'),
    path('ajax/xfilename/', adm.xfilename, name='xfilename'),

    # path('admin2/hapusfile/', adm.removeAllfilePaket, name='downloadsemuafilepaket'),
    path('admin2/hapussemuafilepaket/', adm.removeAllfilePaket, name='hapussemuafilepaket'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)