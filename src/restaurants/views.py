from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import RestaurantLocation

class RestaurantListView(ListView):
    # in list views, the object variable (for use in the template)
    #... is always object_list
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
            Q(category__iexact=slug)
            | Q(category__icontains=slug)
            )
        else:
            queryset=RestaurantLocation.objects.all()
        return queryset

class RestaurantDetailView(DetailView):
    # in detail views, the object variable (for use in the template)
    #... is always object
    queryset = RestaurantLocation.objects.all()

    def get_object(self, *args, **kwargs):
        rest_id = self.kwargs.get("rest_id")
        obj = get_object_or_404(RestaurantLocation, id=rest_id) # or pk=rest_id
        return obj
