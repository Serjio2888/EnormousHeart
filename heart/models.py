from django.db import models

class Event(models.Model): #id добавлен автоматически
    name = models.CharField(u'Название мероприятия', max_length=255, default='event')
    desc = models.TextField(u'Описание', blank=True)
    place = models.CharField(u'Место проведения', blank=True, max_length=255)
    creat_time = models.DateTimeField(u'Дата создания', auto_now_add=True)
    start_time = models.DateTimeField(u'Дата начала')
    end_time = models.DateTimeField(u'Дата окончания')
    hidden = models.BooleanField(u'Скрытый?(False-нет, True-да)',default = False)

    def __str__(self):
        return '{}'.format(self.name)

class Task(models.Model):
    name = models.CharField(u'Задача', max_length=255, default='Zadacha')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    todo = models.TextField(u'Описание', blank=True)

    def __str__(self):
        return '{}'.format(self.name)

class Notification(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    
    author = models.CharField(u'Ваше имя', max_length=80)
    #author = models.ForeignKey(u'Привязка к волонтёру',Volonteur, on_delete=models.CASCADE)
    info = models.TextField(u'Описание', blank=True)

    def __str__(self):
        return '{} {}'.format(self.info, self.author)

class Volonteur(models.Model):
    name = models.CharField(u'Имя волонтера', max_length=255)
    pass_hash = models.CharField(u'хэш пароля', max_length=255)
    #event = models.ForeignKey(u'На каком мероприятии', Event, on_delete=models.CASCADE)
    #add volonteur
    info = models.TextField(u'Описание', blank=True)

    def __str__(self):
        return '{} '.format(self.info)