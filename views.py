from datetime import datetime

from django.shortcuts import render, redirect

from .models import Exercise


def index(request):
    items = Exercise.objects.filter(date=datetime.today().date())
    print(datetime.today().date())
    context = {'items': items}
    return render(request, template_name="workout_logging.html", context=context)


def history(request):
    context = None
    if request.method == "POST":
        date_ = request.POST.get('date')
        history_ = Exercise.objects.filter(date=date_)
        context = {'items': history_, 'date': date_}
    return render(request, template_name="workout_history.html", context=context)


def log_exercise(request):
    input_ = "NO response"
    if request.method == "POST":
        date_ = datetime.today().date()
        exercise = request.POST.get('exercise')
        weight = request.POST.get('weight')
        sets = request.POST.get('sets')
        reps = request.POST.get('reps')
        input_ = Exercise(**{"date": date_, "exercise": exercise, "weight": weight, "sets": sets, "reps": reps})
        input_.save()
    return redirect("/")

# # Create your views here.
# def contacts(request):
#     return render(request, template_name="multi_axis.html")


# Create your views here.
# def base(request):
#     context = {
#         'name': "This the var i have set in base"
#     }
#     return render(request, template_name="base.html", context=context)
