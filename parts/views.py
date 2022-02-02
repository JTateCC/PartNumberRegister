from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView, DeleteView
from parts.models import Part, Project, Category, Colour
from parts.forms import PartForm
# Base Home page View


# Part CRUD Views

class PartListView(LoginRequiredMixin, ListView):
    model = Part


class PartDetailView(LoginRequiredMixin, DetailView):
    model = Part


class PartCreateView(LoginRequiredMixin, CreateView):
    model = Part
    fields = ['part_number',
              'part_title',
              'part_category',
              'part_project',
              'part_colour',]

    def get_success_url(self):
        return reverse('parts:part_detail', kwargs={'pk': self.object.pk})


class PartUpdateView(LoginRequiredMixin, UpdateView):
    model = Part
    fields = '__all__'
    template_name = 'parts/part_form.html'

    def get_success_url(self):
        return reverse('parts:detail', kwargs={'pk': self.object.pk})


class PartFormView(LoginRequiredMixin, FormView):
    form_class = PartForm
    template_name = 'parts/part_form.html'
    success_url = "/thanks"


class PartDeleteView(LoginRequiredMixin, DeleteView):
    model = Part

    def get_success_url(self):
        return reverse('parts:part_list')

# Project CRUD Views


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = '__all__'

    def get_success_url(self):
        return reverse('parts:project_detail', kwargs={'pk': self.object.pk})


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = '__all__'
    template_name = 'parts/project_form.html'

    def get_success_url(self):
        return reverse('parts:project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project

    def get_success_url(self):
        return reverse('parts:project_list')

# Category CRUD Views


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = '__all__'

    def get_success_url(self):
        return reverse('parts:category_detail', kwargs={'pk': self.object.pk})


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'parts/category_form.html'

    def get_success_url(self):
        return reverse('parts:category_detail', kwargs={'pk': self.object.pk})


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category

    def get_success_url(self):
        return reverse('parts:category_list')


# Colour CRUD Views

class ColourListView(LoginRequiredMixin, ListView):
    model = Colour


class ColourDetailView(LoginRequiredMixin, DetailView):
    model = Colour


class ColourCreateView(LoginRequiredMixin, CreateView):
    model = Colour
    fields = '__all__'

    def get_success_url(self):
        return reverse('parts:part_list')


class ColourDeleteView(LoginRequiredMixin, DeleteView):
    model = Colour

    def get_success_url(self):
        return reverse('parts:colour_list')