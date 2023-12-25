from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from . import models, forms
from django.views import generic
from django.urls import reverse
from haystack.query import SearchQuerySet
from .models import CarAnnouncement
from .forms import CarSearchForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class CarListView(generic.ListView):
    template_name = 'demo-auto-services-products (1).html'
    model = models.CarAnnouncement

    def get_queryset(self):
        return self.model.objects.all()



class CarDetailView(generic.DetailView):
    template_name = "shop-product-sidebar-left.html"

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.CarAnnouncement, id = car_id)


@method_decorator(login_required, name='dispatch')
class CarCreateView(generic.CreateView):
    template_name = "start_mvp/car_create.html"
    model = models.CarAnnouncement
    form_class = forms.CarForm
    success_url = reverse_lazy('car_list')

    def form_valid(self, form):
        user = self.request.user

        form.instance.owner = user.customer
        # Redirect the user or show an error message
        # ...
        return super(CarCreateView, self).form_valid(form=form)

    # def user_cars(request):
    #     # Assuming the user is logged in
    #     user = request.user
    #
    #     # Query all cars owned by the logged-in user
    #     user_cars = CarAnnouncement.objects.filter(owner=user)

        # return render(request, 'user_cars_template.html', {'user_cars': user_cars})

class CarDeleteView(generic.DeleteView):
    model = CarAnnouncement
    template_name = 'start_mvp/confirm_delete.html'
    success_url = '/car_list/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(CarAnnouncement, id= car_id)


class CarUpdateView(generic.UpdateView):
    template_name = 'start_mvp/car_update.html'
    form_class = forms.CarForm
    success_url = 'car_list/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.CarAnnouncement, id=car_id)

    def form_valid(self, form):
        return super(CarUpdateView, self).form_valid(form=form)



class BaseView(generic.TemplateView):
    template_name = "demo-auto-services.html"


class AboutView(generic.TemplateView):
    template_name = "demo-auto-services-about-us.html"

class ContactView(generic.TemplateView):
    template_name = "demo-auto-services-contact.html"

# def search(request):
#     query = request.GET.get('q')
#     results = []
#
#     if query:
#         results = SearchQuerySet().models(CarAnnouncement).filter(content=query)
#     return render(request,'page-search-results.html', {'results' : results})


def search_results(request):
    query = request.GET.get('query', '')
    if query:
        announcements = CarAnnouncement.objects.filter(name_car__icontains=query)
    else:
        announcements = CarAnnouncement.objects.none()

    return render(request, 'page-search-results.html', {'announcements': announcements})



# def car_search_gpt(request):
#     form = CarSearchForm(request.GET)
#     cars = CarAnnouncement.objects.all()
#
#     if form.is_valid():
#         search_query = form.cleaned_data['search_query']
#         if search_query:
#             cars = cars.filter(name_car__icontains=search_query)
#
#     context = {
#         'form': form,
#         'cars': cars,
#     }
#
#     return render(request, 'start_mvp/car_search.html', context)

