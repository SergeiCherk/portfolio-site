from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    featured_projects = Project.objects.filter(is_featured=True)
    context = {
        'projects': projects,
        'featured_projects': featured_projects,
    }
    return render(request, 'projects/list.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project': project,
    }
    return render(request, 'projects/detail.html', context)