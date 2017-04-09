from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.views import generic
from Visthuset_web.models import Event
import datetime 
from django.utils import formats


# Create your views here.
class MenyView(generic.TemplateView):
    template_name = 'cafe/meny.html'
    
def EventView(request):
    today = datetime.date.today()
    eventlist = []
    events = Event.objects.filter()
    result = []
    public = []
    
    for event in events:
        eventlist.append(event)
        if event.Pub_date > today: 
            result.append(event)
           
        if event.Pub_end < today:
            result.append(event)
        
    for c in eventlist:
        if c not in result:
            public.append(c)

    args = {}
    args['events'] = public
    
    return render_to_response('cafe/event.html', args)