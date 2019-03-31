from django.db import models

class Partner(models.Model):
    name = models.CharField(u'ФИО/ЮР. Лицо', max_length=255)
    inn = models.CharField(u'ИНН', max_length=255,blank=True)
    web = models.CharField(u'web-сайт', max_length=255,blank=True)
    mail = models.CharField(u'Mail', max_length=255,blank=True)
    tags = models.CharField(u'Тэги', max_length=255)
    telephone = models.CharField(u'телефон партнёра', max_length=255,blank=True)
    #author = models.ForeignKey(u'Привязка к волонтёру',Volonteur, on_delete=models.CASCADE)
    role = models.TextField(u'Что делает для мероприятия?', blank=True)

    def __str__(self):
        return '{}'.format(self.name)

class Event(models.Model): #id добавлен автоматически
    name = models.CharField(u'Название мероприятия', max_length=255, default='event')
    desc = models.TextField(u'Описание', blank=True)
    place = models.CharField(u'Место проведения', blank=True, max_length=255)
    creat_time = models.DateTimeField(u'Дата создания', auto_now_add=True)
    start_time = models.DateTimeField(u'Дата начала')
    end_time = models.DateTimeField(u'Дата окончания')
    hidden = models.BooleanField(u'Скрытый?(False-нет, True-да)',default = False)
    tags = models.CharField(u'Тэги(через запятую)', max_length=255)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

class Task(models.Model):
    name = models.CharField(u'Задача', max_length=255, default='Zadacha')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    todo = models.TextField(u'Описание', blank=True)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    end_time = models.DateTimeField(u'Время окончания', blank=True, auto_now=True)
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
        return '{} {}'.format(self.name, self.info)

