from django.urls import path
from parts.views import (PartListView, PartDetailView, PartCreateView, PartUpdateView,
                        ProjectListView, ProjectDetailView)


app_name = 'parts'

urlpatterns = [
    path('parts/', PartListView.as_view()),
    path('parts/<int:pk>/', PartDetailView.as_view(), name='detail'),
    path('parts/newpart/', PartCreateView.as_view()),
    path('parts/<int:pk>/update', PartUpdateView.as_view()),
    path('project/', ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),

]
