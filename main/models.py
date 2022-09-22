from django.db import models

class Task(models.Model):
    title = models.CharField("Название",max_lenght =50)
    task = models.TextField("Описание")

    def __str__(self):
        return self.title

    answer = models.TextField("Ответ")
