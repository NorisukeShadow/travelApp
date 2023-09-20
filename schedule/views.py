from django.shortcuts import render, redirect
from .models import ScheduleEvent
from .forms import ScheduleEventForm

def schedule(request):
    events = ScheduleEvent.objects.all()
    if request.method == 'POST':
        form = ScheduleEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule')
    else:
        form = ScheduleEventForm()
    return render(request, 'schedule/schedule.html', {'events': events, 'form': form})

