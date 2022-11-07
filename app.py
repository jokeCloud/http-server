from event import Event
from event_online import EventOnline

ev_online = EventOnline('Live of the Python')
ev2_online = EventOnline('Live of the Javascript')
# ev_online.print_information()
# ev2_online.print_information()
print(ev_online.to_json())
print(ev2_online.to_json())

ev = Event('Python class', 'Rio de Janeiro')
ev.print_information()
