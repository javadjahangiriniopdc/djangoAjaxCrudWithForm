from django.shortcuts import render

# Create your views here.
from myapp.form import StudentForm
from myapp.models import Student


def home(request):
    form = StudentForm()
    stu = Student.objects.all()
    context = {'form': form, 'stu': stu}
    return render(request, 'core/home.html', context)
