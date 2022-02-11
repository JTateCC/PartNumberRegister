from django.urls import path
from parts.views import (PartListView, PartDetailView, PartCreateView, PartUpdateView, PartDeleteView, PartSearchView,
                         ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView,
                         CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
                         ColourListView, ColourDetailView, ColourCreateView, ColourDeleteView,
                         FixingCategoryListView, FixingListView)


app_name = 'parts'

urlpatterns = [
    # parts url paths
    path('', PartListView.as_view(), name='part_list'),
    path('parts/', PartListView.as_view(), name='part_list'),
    path('parts/<int:pk>/', PartDetailView.as_view(), name='part_detail'),
    path('parts/newpart/', PartCreateView.as_view(), name='part_create'),
    path('parts/<int:pk>/update', PartUpdateView.as_view(),name='part_update'),
    path('parts/<int:pk>/delete/', PartDeleteView.as_view(), name='part_delete'),
    path('parts/search_result/', PartSearchView.as_view(), name='search_result'),
    # projects url paths
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/newproject/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/update', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    # category url paths
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/newcategory/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/update', CategoryUpdateView.as_view(), name ='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    # colours url paths
    path('colours/', ColourListView.as_view(), name='colour_list'),
    path('colours/<int:pk>/', ColourDetailView.as_view(), name='colour_detail'),
    path('colours/newcolour/', ColourCreateView.as_view(), name='colour_create'),
    path('colours/<int:pk>/delete/', ColourDeleteView.as_view(), name='colour_delete'),
    # fixing catalog paths
    path('fixings/fixing_category/', FixingCategoryListView.as_view(), name='fixing_category_list'),
    path('fixings/fixing_category/<int:fixing_category>/', FixingListView.as_view(), name='fixing_list'),
]
