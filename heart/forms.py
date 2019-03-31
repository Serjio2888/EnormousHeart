from django.forms import ModelForm
from heart.models import Event, Task, Notification, Partner

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ['name', 'desc', 'partner']

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ['name', 'todo', 'event', 'partner']

class NotificationForm(ModelForm):
	class Meta:
		model = Notification
		fields = ['task', 'info']

class PartnerForm(ModelForm):
	class Meta:
		model = Partner
		fields = ['name', 'inn','web','mail','tags','telephone', 'role']
