from django.shortcuts import render, get_object_or_404
from .models import Courses
from .forms import ContactCourse

def index(request):
	courses = Courses.objects.all()
	template_name='courses/index.html'
	context = {
		'courses': courses
	}
	return render(request, template_name, context)
"""
def details(request, pk):
	course = get_object_or_404(Courses, pk=pk)
	context ={
		'course': course
	}
	template_name = 'courses/details.html'
	return render(request, template_name, context)
"""
def details(request, slug):
    course = get_object_or_404(Courses, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(course)
            form = ContactCourse()
    else:
        form = ContactCourse()
    context['form'] = form
    context['course'] = course
    template_name = 'courses/details.html'
    return render(request, template_name, context)