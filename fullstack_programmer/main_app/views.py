from django.shortcuts import render
from . import models


def index_page(request):
    return render(request, 'index.html')


def skill_page(request):
    skills = models.pop_skills.objects.order_by('-skill_count')
    skills_fs = models.pop_skills_fsprogrammer.objects.all()
    return render(request, 'skills.html', {"skills": skills, 'skills_fs': skills_fs})


def salary_page(request):
    zp_prof = models.zp_prof.objects.all()
    zp_fs = models.zp_fsprog.objects.all()
    vac = models.vacancy_count.objects.all()
    vac_fs = models.vacancy_fsprog_count.objects.all()
    return render(request, 'salary.html', {'fs':zp_fs, 'prof':zp_prof, 'vac':vac,'vac_fs':vac_fs})
