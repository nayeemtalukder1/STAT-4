from .models import Student

def student_processor(request):
    if request.user.is_authenticated:
        try:
            student = Student.objects.get(user=request.user)
        except Student.DoesNotExist:
            student = None
    else:
        student = None
    return {'student': student}