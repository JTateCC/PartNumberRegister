from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView, DeleteView
from parts.models import Part, Project, Category, Colour
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
              'part_project',
              'part_colour',]

    def get_success_url(self):
        return reverse('parts:part_detail', kwargs={'pk': self.object.pk})


class PartUpdateView(UpdateView):
    model = Part
    fields = '__all__'
    template_name = 'parts/part_form.html'

    def get_success_url(self):
        return reverse('parts:detail', kwargs={'pk': self.object.pk})


class PartFormView(FormView):
    form_class = PartForm
    template_name = 'parts/part_form.html'
    success_url = "/thanks"


class PartDeleteView(DeleteView):
    model = Part

    def get_success_url(self):
        return reverse('parts:part_list')

# Project CRUD Views


class ProjectListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    fields = '__all__'

    def get_success_url(self):
        return reverse('parts:project_detail', kwargs={'pk': self.object.pk})


class ProjectUpdateView(UpdateView):
    model = Project
    fields = '__all__'
    template_name = 'parts/project_form.html'

    def get_success_url(self):
        return reverse('parts:project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    model = Project

    def get_success_url(self):
        return reverse('parts:project_list')

# Category CRUD Views


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'

    def get_success_url(self):
        return reverse('parts:category_detail', kwargs={'pk': self.object.pk})


class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'parts/category_form.html'

    def get_success_url(self):
        return reverse('parts:category_detail', kwargs={'pk': self.object.pk})


class CategoryDeleteView(DeleteView):
    model = Category

    def get_success_url(self):
        return reverse('parts:category_list')


# Colour CRUD Views

class ColourListView(ListView):
    model = Colour


class ColourDetailView(DetailView):
    model = Colour


class ColourCreateView(CreateView):
    model = Colour
    fields = '__all__'

    def get_success_url(self):
        return reverse('parts:part_list')


class ColourDeleteView(DeleteView):
    model = Colour

    def get_success_url(self):
        return reverse('parts:colour_list')