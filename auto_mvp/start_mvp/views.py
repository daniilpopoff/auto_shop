from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from . import models, forms
from django.views import generic
from django.urls import reverse
# Create your views here.



class CarListView(generic.ListView):
    template_name = 'demo-auto-services-products.html'
    model = models.CarAnnouncement

    def get_queryset(self):
        return self.model.objects.all()



class CarDetailView(generic.DetailView):
    template_name = "start_mvp/car_detail.html"

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.CarAnnouncement, id = car_id)



class CarCreateView(generic.CreateView):
    template_name = "start_mvp/car_create.html"
    model = models.CarAnnouncement
    form_class = forms.CarForm
    success_url = '/car_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CarCreateView, self).form_valid(form=form)


class CarDeleteView(generic.DeleteView):
    template_name = 'start_mvp/confirm_delete.html'
    success_url = '/car_list/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')


class CarUpdateView(generic.UpdateView):
    template_name = 'start_mvp/car_update.html'
    form_class = forms.CarForm
    success_url = '/car_list/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.CarAnnouncement, id=car_id)

    def form_valid(self, form):
        return super(CarUpdateView, self).form_valid(form=form)



class BaseView(generic.TemplateView):
    template_name = "demo-auto-services.html"
