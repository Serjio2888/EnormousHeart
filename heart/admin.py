from django.contrib import admin
from heart import models


admin.site.register(models.Event)
admin.site.register(models.Notification)
admin.site.register(models.Task)
