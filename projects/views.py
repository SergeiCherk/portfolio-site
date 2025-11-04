from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    # Преобразуем tech_stack в список
    for project in projects:
        if project.tech_stack:
            project.tech_list = [tech.strip() for tech in project.tech_stack.split(',')]
        else:
            project.tech_list = []
    
    featured_projects = Project.objects.filter(is_featured=True)
    for project in featured_projects:
        if project.tech_stack:
            project.tech_list = [tech.strip() for tech in project.tech_stack.split(',')]
        else:
            project.tech_list = []
    
    context = {
        'projects': projects,
        'featured_projects': featured_projects,
    }
    return render(request, 'projects/list.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if project.tech_stack:
        project.tech_list = [tech.strip() for tech in project.tech_stack.split(',')]
    else:
        project.tech_list = []
    return render(request, 'projects/detail.html', {'project': project})