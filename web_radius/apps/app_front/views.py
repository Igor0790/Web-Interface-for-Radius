from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.edit import DeletionMixin

from apps.app_base import models
from apps.app_front.forms import RadcheckForm, NasFormModel, RadhuntgroupForm, RadreplyForm, RadusergroupForm, \
    RadgroupcheckForm, RadgroupreplyForm, DictionaryFindForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class FirstDataFromSQLView(generic.TemplateView):
    template_name = 'front/get_data.html'
    model = models.Nas
    queryset = models.Nas.objects.all()


    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'nas'
        con['data'] = models.Nas.objects.all()
        con['count'] = models.Nas.objects.count()
        return con


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NasCreateView(generic.CreateView):
    model = models.Nas
    context_object_name = 'data'
    template_name = 'front/add-form.html'
    queryset = models.Nas.objects.all()
    form_class = NasFormModel
    success_url = '/front/nas/'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['title'] = 'Nas'
        return con

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NasUpdateView(generic.UpdateView, DeletionMixin):
    model = models.Nas
    template_name = 'front/update_record.html'
    queryset = models.Nas.objects.all()
    form_class = NasFormModel
    success_url = '/front/nas/'

    def post(self, request, *args, **kwargs):
        if 'action_delete' in request.POST:
            return self.delete(request)
        else:
            return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'nas'
        return con



@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadactView(generic.ListView):
    model = models.Radacct
    context_object_name = 'data'
    template_name = 'front/radact.html'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'radact'
        con['count'] = models.Radacct.objects.count()
        return con


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadhuntgroupView(generic.ListView):
    model = models.Radhuntgroup
    context_object_name = 'data'
    template_name = 'front/radhuntgroup.html'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'radhuntgroup'
        con['count'] = models.Radhuntgroup.objects.count()
        return con

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadhuntgroupCreateView(generic.CreateView):
    model = models.Radhuntgroup
    template_name = 'front/add-form.html'
    queryset = models.Radhuntgroup.objects.all()
    context_object_name = 'data'
    form_class = RadhuntgroupForm
    success_url = '/front/radhuntgroup/'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'radhuntgroup'
        con['title'] = 'Radhuntgroup'
        return con

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadhuntgroupUpdateView(generic.UpdateView, DeletionMixin):
    model = models.Radhuntgroup
    template_name = 'front/update_record.html'
    form_class = RadhuntgroupForm
    success_url = '/front/radhuntgroup/'

    def post(self, request, *args, **kwargs):
        if 'action_delete' in request.POST:
            return self.delete(request)
        else:
            return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'radhuntgroup'
        return con

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadcheckView(generic.ListView):
    model = models.Radcheck
    template_name = 'front/radcheck.html'
    queryset = models.Radcheck.objects.all()
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'radcheck'
        con['count'] = self.model.objects.count()
        return con


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadcheckCreateView(generic.CreateView):
    model = models.Radcheck
    template_name = 'front/add-form.html'
    queryset = models.Radcheck.objects.all()
    context_object_name = 'data'
    form_class = RadcheckForm
    success_url = '/front/radcheck/'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'radcheck'
        con['title'] = 'Rad check'
        return con

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadcheckUpdateView(generic.UpdateView, DeletionMixin):
    model = models.Radcheck
    template_name = 'front/update_record.html'
    form_class = RadcheckForm
    success_url = '/front/radcheck/'

    def post(self, request, *args, **kwargs):
        if 'action_delete' in request.POST:
            return self.delete(request)
        else:
            return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'radcheck'
        con['title'] = 'RadCheck'
        return con

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadreplyView(generic.ListView):
    model = models.Radreply
    template_name = 'front/radreply.html'
    queryset = models.Radreply.objects.all()
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'radreply'
        con['title'] = 'RadReply'
        con['count'] = self.model.objects.count()
        return con
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadreplyCreateView(generic.CreateView):
    model = models.Radreply
    template_name = 'front/add-form.html'
    queryset = models.Radreply.objects.all()
    context_object_name = 'data'
    form_class = RadreplyForm
    success_url = '/front/radreply/'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'radreply'
        con['title'] = 'RadReply'
        return con

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadreplyUpdateView(generic.UpdateView, DeletionMixin):
    model = models.Radreply
    template_name = 'front/update_record.html'
    form_class = RadreplyForm
    success_url = '/front/radreply/'

    def post(self, request, *args, **kwargs):
        if 'action_delete' in request.POST:
            return self.delete(request)
        else:
            return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'radreply'
        return con

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadusergroupView(generic.ListView):
    model = models.Radusergroup
    template_name = 'front/radusergroup.html'
    queryset = models.Radusergroup.objects.order_by('id').all()
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'radusergroup'
        con['title'] = "RadUserGroup"
        con['count'] = self.model.objects.count()
        return con
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadusergroupCreateView(generic.CreateView):
    model = models.Radusergroup
    template_name = 'front/add-form.html'
    queryset = models.Radusergroup.objects.all()
    context_object_name = 'data'
    form_class = RadusergroupForm
    success_url = '/front/radusergroup/'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'radusergroup'
        con['title'] = "RadUserGroup"
        return con
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadusergroupUpdateView(generic.UpdateView, DeletionMixin):
    model = models.Radusergroup
    template_name = 'front/update_record.html'
    form_class = RadusergroupForm
    success_url = '/front/radusergroup/'

    def post(self, request, *args, **kwargs):
        if 'action_delete' in request.POST:
            return self.delete(request)
        else:
            return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'radusergroup'
        return con

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadgroupcheckView(generic.ListView):
    model = models.Radgroupcheck
    template_name = 'front/radgroupcheck.html'
    queryset = models.Radgroupcheck.objects.all()
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = '1'
        con['count'] = self.model.objects.count()
        return con

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadgroupcheckCreateView(generic.CreateView):
    model = models.Radgroupcheck
    template_name = 'front/add-form.html'
    queryset = models.Radgroupcheck.objects.all()
    context_object_name = 'data'
    form_class = RadgroupcheckForm
    success_url = '/front/radgroupcheck/'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = '1'
        return con

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadgroupcheckUpdateView(generic.UpdateView, DeletionMixin):
    model = models.Radgroupcheck
    template_name = 'front/update_record.html'
    form_class = RadgroupcheckForm
    success_url = '/front/radgroupcheck/'

    def post(self, request, *args, **kwargs):
        if 'action_delete' in request.POST:
            return self.delete(request)
        else:
            return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['rad'] = '1'
        return con

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadgroupreplyView(generic.ListView):
    model = models.Radgroupreply
    template_name = 'front/radgroupreply.html'
    queryset = models.Radgroupreply.objects.all()
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = '2'
        con['count'] = self.model.objects.count()
        return con
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadgroupreplyCreateView(generic.CreateView):
    model = models.Radgroupreply
    template_name = 'front/add-form.html'
    queryset = models.Radgroupreply.objects.order_by('id').all()
    context_object_name = 'data'
    form_class = RadgroupreplyForm
    success_url = '/front/radgroupreply/'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = '2'
        return con
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadgroupreplyUpdateView(generic.UpdateView, DeletionMixin):
    model = models.Radgroupreply
    template_name = 'front/update_record.html'
    form_class = RadgroupreplyForm
    success_url = '/front/radgroupreply/'

    def post(self, request, *args, **kwargs):
        if 'action_delete' in request.POST:
            return self.delete(request)
        else:
            return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = '2'
        return con

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class IndexView(generic.TemplateView):
    template_name = 'front/index.html'

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RadpostauthView(generic.ListView):
    model = models.Radpostauth
    template_name = 'front/radpostauth.html'
    queryset = models.Radpostauth.objects.all()
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['segment'] = 'radpostauth'
        con['count'] = self.model.objects.count()
        return con

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DictionaryView(generic.TemplateView):
    model = models.Dictionary
    template_name = 'front/dictionary.html'
    queryset = models.Dictionary.objects.all()
    context_object_name = 'data'

    def get_context_data(self, *, object_list=None, **kwargs):
        con = super().get_context_data(**kwargs)
        con['find_form'] = DictionaryFindForm
        con['segment'] = 'dictionary'
        con['data'] = models.Dictionary.objects.all()
        con['title'] = 'Dictionary'
        con['count'] = self.model.objects.count()

        return con


    def post(self, request):
        word = request.POST.get('find_word')

        if not word:
            return redirect(reverse('dictionary'))

        qs = self.model.objects.filter(attribute__icontains=word)
        if not qs:
            qs = self.model.objects.filter(vendor__icontains=word)

        return render(request, self.template_name, context={'data': qs, 'segment': 'dictionary'})