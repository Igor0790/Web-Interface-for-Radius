import json
import requests
from datetime import datetime

from django.db import transaction
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic
from django.views.generic.edit import DeletionMixin
from rest_framework import generics
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from rest_framework.response import Response
from apps.app_acl import forms
from apps.app_acl import models
from apps.app_acl.serializers import AclSerializer, AdgroupSerializer
from apps.app_users.models import AdminsRadiusModel
from apps.app_front.forms import DictionaryFindForm
from core.settings import MEDIA_URL
from apps.app_acl.utils import get_standart_mask
from utils.utils import send_log_to_graylog, send_post_in_ideco

@method_decorator(login_required, name='dispatch')
class TestView(generic.TemplateView):
    template_name = 'app_acp/test.html'
    #template_name = 'templates/app_acl/test.html'


url_for_ideco = 'https://10.50.74.17:8443/fwrules_importer/trigger_update'


class AddRuleFromFile(generics.GenericAPIView):

    serializer_class = AclSerializer
    queryset = models.Aclmodel.objects.all().order_by('name_acl')
    def get(self, request):
        path = r'C:\work\Репозитории\radius\Docker images\web-radius\web_radius\media\rules.txt'
        acl = models.Aclname.objects.filter(name='infrastructure_admin-vpn_acl').first()
        user = AdminsRadiusModel.objects.filter(username='igor.gubauydullin').first()

        data_list = []

        with open(path, 'r', encoding='utf-8') as csv_file:
            for row in csv_file:
                row_list = row.split(';')
                print(row_list)
                rule = row_list[1]
                src = row_list[2]

                mask = get_standart_mask(row_list[4])

                port = 'null'

                dst = row_list[3] + mask

                models.Aclmodel.objects.create(name_acl=acl, rule=rule,
                                               dst=dst, src=src, modified_by=user, port=port, proto='null')

        qs = models.Aclmodel.objects.all()
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)





class AclApiView(generics.GenericAPIView):
    """
    Данный VIEW предназначен для обращения со стороны внешней системы. После получаения GET в этот View
    в ответ будет отправлен json файл со всеми ACL. Это нужно для синхронизации с внешним FW.
    """
    serializer_class = AclSerializer
    queryset = models.Aclmodel.objects.all().order_by('id')

    def get(self, request, aclname):

        qs = models.Aclmodel.objects.filter(name_acl__name=aclname).order_by('id')
        serializer = self.serializer_class(qs, many=True)

        filename = f'{MEDIA_URL}json/{aclname}'

        with open(f'{filename}.json', 'w') as file:
            json.dump(serializer.data, file, indent=4)

        buf = open(filename + '.json', 'rb')

        data = f'time: {datetime.now()}, path: {request.path}, request_total: {request.META.get("COMPUTERNAME")}, ' \
               f'user: {request.user}, ip_address: {request.META.get("REMOTE_ADDR")}'
        #send_log_to_graylog(data)


        return FileResponse(buf, as_attachment=True)


class AdgroupApiView(generics.GenericAPIView):
    """
    Данный VIEW предназначен для обращения со стороны внешней системы. После получаения GET в этот View
    в ответ будет отправлен json файл со всеми ACL. Это нужно для синхронизации с внешним FW.
    """

    serializer_class = AdgroupSerializer
    queryset = models.Adgroupname.objects.all()

    def get(self, request):
        qs = self.get_queryset()
        serializer = self.serializer_class(qs, many=True)
        filename = f'{MEDIA_URL}json/adgroups'

        with open(f'{filename}.json', 'w') as file:
            json.dump(serializer.data, file, indent=4)

        file = open(f'{filename}.json', 'rb')

        data = f'time: {datetime.now()}, path: {request.path}, request_total: {request.META.get("COMPUTERNAME")}, ' \
               f'user: {request.user}, ip_address: {request.META.get("REMOTE_ADDR")}'
        #send_log_to_graylog(data)

        return FileResponse(file, as_attachment=True)

class AclIndexView(generic.TemplateView):
    """
    Главная страница!
    """
    template_name = 'app_acl/test.html'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['title'] = 'ACL MAIN PAGE'
        return con


@method_decorator(login_required, name='dispatch')
class AdgroupnameView(generic.ListView):
    template_name = 'app_acl/adgroupname.html'
    model = models.Adgroupname
    context_object_name = 'data'
    queryset = models.Adgroupname.objects.all().order_by('id')

    def get_context_data(self, *, object_list=None, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'adgroup'
        con['title'] = 'Ad Group'
        con['count'] = self.model.objects.count()
        return con

    def post(self, request):



        for key, value in request.POST.items():
            print(f'{key}: {value}')
            ids = key

        try:
            with transaction.atomic():


                qs = models.Adgroupname.objects.filter(id=ids).first()
                qs_name = models.Aclname.objects.filter(id=qs.name_acl.id).first()
                qs_acl = models.Aclmodel.objects.filter(name_acl=qs.name_acl)

                qs_acl.delete()
                qs.delete()
                qs_name.delete()
        except:
            return HttpResponse('Что-то пошло не так. Просьба передать проблему разработчику.<br>'
                                'Губайдуллин Игорь <br>'
                                'Моб: 89162693969<br>'
                                'tg: @tairkaaa')

        send_post_in_ideco()

        return render(request, self.template_name, context={'data': models.Adgroupname.objects.all()})



@method_decorator(login_required, name='dispatch')
class AdgroupnameCreateView(generic.TemplateView):
    template_name = 'app_acl/add-form.html'
    model = models.Adgroupname
    context_object_name = 'data'
    success_url = '/acl/adgroup/'
    form_class = forms.AdgroupnameForm


    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['title'] = 'ASSOSIATIONS AD - ACL NAME'
        con['segment'] = 'adgroup'
        con['form'] = forms.AdgroupnameForm

        return con

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = AdminsRadiusModel.objects.filter(user_id=request.user.id).first()
            acl_name = models.Aclname(name=form.cleaned_data['name_acl'])
            acl_name.save()
            with transaction.atomic():

                self.model.objects.create(group_name=form.cleaned_data['group_name'], name_acl=acl_name,
                                          modified_by=user)

            send_post_in_ideco()

            return redirect(reverse('adgroup'))
        else:
            return render(request, self.template_name)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AclruleView(generic.ListView):
    template_name = 'app_acl/acl_list.html'
    model = models.Aclmodel
    context_object_name = 'data'
    queryset = models.Aclmodel.objects.all().order_by('name_acl')


    def get_context_data(self, *, object_list=None, **kwargs):
        con = super().get_context_data(object_list=None, **kwargs)
        con['aclnamemodel'] = models.Aclname.objects.all()
        con['segment'] = 'acl-rule'
        con['title'] = 'Acl'

        return con

    def get_queryset(self):
        word = self.request.GET.get('find_word')
        if word:
            return models.Aclmodel.objects.filter(name_acl__icontains=word).order_by('id')
        else:
            return models.Aclmodel.objects.all().order_by('name_acl')

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AclruleCreateView(generic.CreateView):
    template_name = 'app_acl/add-form.html'
    model = models.Aclmodel
    context_object_name = 'data'
    success_url = '/acl/acl-rule/'
    form_class = forms.AclmodelForm


    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'acl-rule'
        con['title'] = 'Acl'
        return con


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = AdminsRadiusModel.objects.filter(user_id=request.user.id).first()

            port = form.cleaned_data['port']
            protocol = form.cleaned_data['proto']

            if protocol == 'null':
                port = None
                protocol = None

            if port == 'any':
                port = None

            if protocol == 'icmp':
                port = '8/0'


            self.model.objects.create(src=form.cleaned_data['src'],
                                          dst=form.cleaned_data['dst'],
                                          name_acl=form.cleaned_data['name_acl'],
                                          port=port,
                                          modified_by=user,
                                          proto=protocol,
                                          description=form.cleaned_data['description'],
                                          rule=form.cleaned_data['rule'])

            send_post_in_ideco()

            return redirect(reverse('acl-rule'))
        else:
            return HttpResponse('Ошибка в форме!')


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AclruleUpdateView(generic.UpdateView, DeletionMixin):
    model = models.Aclmodel
    template_name = 'app_acl/update_record.html'
    form_class = forms.AclmodelForm
    success_url = '/acl/acl-rule/'

    def post(self, request, *args, **kwargs):
        if 'action_delete' in request.POST:
            return self.delete(request)

        form = forms.AclmodelForm(request.POST)
        if form.is_valid():
            record = models.Aclmodel.objects.filter(id=kwargs['pk']).first()

            port = form.cleaned_data['port']
            protocol = form.cleaned_data['proto']

            if protocol == 'null':
                port = None
                protocol = None

            if port == 'any':
                port = None

            if protocol == 'icmp':
                port = '8/0'

            record.proto = protocol
            record.src = form.cleaned_data['src']
            record.dst = form.cleaned_data['dst']
            record.description = form.cleaned_data['description']
            record.rule = form.cleaned_data['rule']
            record.port = port

            with transaction.atomic():
                record.save()

            send_post_in_ideco()

            return redirect(reverse('acl-rule'))
        else:
            return HttpResponse('Ошибка в форме!')



    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'acl-rule'
        con['title'] = 'Acl'
        return con

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class TestAclList(generic.TemplateView):
    context_object_name = 'data'
    template_name = 'app_acl/test.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        con = super().get_context_data(object_list=None, **kwargs)

        file_log = open('request.log')
        file_log.readline()
        con['data'] = file_log

        ideco_log = open('ideco_log.log')
        ideco_log.readline()
        con['ideco'] = ideco_log

        con['title'] = 'ACL'
        return con