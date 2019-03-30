from django.forms import ModelForm
from heart.models import Event, Task, Notification, Partner

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

class PartnerForm(ModelForm):
	class Meta:
		model = Partner
		fields = ['task', 'name', 'inn','web','mail','tags','telephone', 'event', 'role']
