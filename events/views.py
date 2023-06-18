from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from datetime import datetime
import csv
from events.models import Event,Participant
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

def event(request):
    try:
        events = Event.objects.all()
        context = {'events': events}
        return render(request, 'events.html', context)
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")
    
def event_list(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Event_List.csv"'

    writer = csv.writer(response)
    writer.writerow(['Event Name', 'Organiser', 'No. of Participants'])

    events = Event.objects.all()
    for event in events:
       
            writer.writerow([event.event_name, event.event_createdby,event.participants])
    return response

def eventpost(request, id):
    try:
        event = Event.objects.filter(id=id).first()
        context = {'event': event}
        return render(request, 'event.html', context)
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")

def create_event(request):
    try:
        events = Event.objects.all()
        size = events.count()
        context = {'events': events,'count':size}
        return render(request, 'create_event.html', context)
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")

@staff_member_required
def ADD_event(request):
    try:
        if request.method == 'POST':
            event_name = request.POST.get('event_title')
            event_description = request.POST.get('event_desc')
            slug = request.POST.get('slug')
            event_createdby= request.POST.get('event_createdby')
            ev = Event(
                event_name=event_name,
                event_description=event_description,
                slug=slug,
                event_createdby = event_createdby,
            )
            ev.save()
            return redirect('create_event')
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")

def Edit_event(request):
    try:
        events = Event.objects.all()
       
        context = {'events': events}
        return redirect(request, 'create_event', context)
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")

def Update_event(request, id):
    try:
        if request.method == 'POST':
            event_name = request.POST.get('event_title')
            event_description = request.POST.get('event_desc')
            slug = request.POST.get('slug')
            event_createdby= request.POST.get('event_createdby')
            ev = Event(
                id=id,
                event_name=event_name,
                event_description=event_description,
                slug=slug,
                event_createdby = event_createdby,
                time_of_creation=datetime.now(),
            )
            ev.save()
            return redirect('create_event')
        return redirect(request, 'create_event.html')
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")

def Delete_event(request, id):
    try:
        events = Event.objects.filter(id=id)
        events.delete()
        return redirect('create_event')
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")

def search_event(request):
    try:
        query = request.GET['query']
        events = Event.objects.filter(event_name__icontains=query)
        params = {'events': events}
        return render(request, 'search.html', params)
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")

def register_participant(request):
    if request.method == "POST":
        logged_in_user = request.user
        username = logged_in_user.username
        email = logged_in_user.email
        participant = Participant(name = username, email = email)
        participant.save()
        context = {
            'username': username,
            'email': email
        }
        return render(request,'registered_event.html',context)

    else:
        prts = Participant.objects.all()
        events = Event.objects.all()
        # If the request method is not POST, render the template with the modal
        return render(request, 'events.html',{'memb':prts,'events':events})
    

@login_required
def participant_registered_events(request):

       return render(request, 'registered_event.html')
    