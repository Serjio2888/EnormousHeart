from django.forms import ModelForm
from heart.models import Event, Task, Notification

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ['name', 'desc']

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['name', 'todo', 'event']

class NotificationForm(ModelForm):
	class Meta:
		model = Notification
		fields = ['task', 'info']


