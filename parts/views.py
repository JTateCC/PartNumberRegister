from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from parts.models import Part, Project
from parts.forms import PartForm


# Part CRUD Views

class PartListView(ListView):
    model = Part


class PartDetailView(DetailView):
    model = Part


class PartCreateView(CreateView):
    model = Part
    fields = ['part_number',
              'part_title',
              'part_category',
              'part_project']

    def get_success_url(self):
        return reverse('parts:detail', kwargs={'pk': self.object.pk})


class PartUpdateView(UpdateView):
    model = Part
    fields = '__all__'
    template_name = 'parts/part_form.html'

    def get_success_url(self):
        return reverse('parts:detail', args=[self.kwargs['pk']])


class PartFormView(FormView):
    form_class = PartForm
    template_name = 'parts/part_form.html'
    success_url = "/thanks"


# Project CRUD Views

class ProjectListView(ListView):
    model = Project

class ProjectDetailView(DetailView):
    model = Project

class ProjectCreateView(CreateView):
    model = Project
    fields = ['project_number',
              'project_title',
              ]

    def get_success_url(self):
        return reverse('parts:project_detail', kwargs={'pk': self.object.pk})
