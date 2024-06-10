from django.shortcuts import render, redirect
from .forms import StudentForm, SubjectForm, GradeForm
from .models import Student, Subject, Grade

def home(request):
    return render(request, 'home.html')

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'register_student.html', {'form': form})

def register_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'register_subject.html', {'form': form})

def register_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'register_grade.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects})

def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'grade_list.html', {'grades': grades})

def student_report(request):
    students = Student.objects.all()
    report_data = []

    for student in students:
        grades = Grade.objects.filter(student=student)

        subjects = {}
        for grade in grades:
            if grade.subject not in subjects:
                subjects[grade.subject] = {
                    'trimester_1': None,
                    'trimester_2': None,
                    'trimester_3': None,
                    'average': 0,
                    'result': 'Pending'
                }
            if grade.trimester == 1:
                subjects[grade.subject]['trimester_1'] = grade.grade
            elif grade.trimester == 2:
                subjects[grade.subject]['trimester_2'] = grade.grade
            elif grade.trimester == 3:
                subjects[grade.subject]['trimester_3'] = grade.grade

        for subject, data in subjects.items():
            grades_list = [g for g in [data['trimester_1'], data['trimester_2'], data['trimester_3']] if g is not None]
            if grades_list:
                average = sum(grades_list) / len(grades_list)
                data['average'] = round(average, 2)
                data['result'] = 'Aprobado' if average >= 15 else 'Reprobado'

        report_data.append({'student': student, 'subjects': subjects})

    context = {
        'report_data': report_data,
    }
    return render(request, 'students_report.html', context)