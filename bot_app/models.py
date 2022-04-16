from django.db import models


class User(models.Model):
    telegram_id = models.CharField(max_length=255)


class Test(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tests')
    title = models.CharField(max_length=255)


class Quection(models.Model):
    title = models.CharField(max_length=255)
    test = models.ForeignKey(Test,on_delete=models.CASCADE,related_name='questions')


class Answer(models.Model):
    title = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)
    quection = models.ForeignKey(Quection,on_delete=models.CASCADE,related_name='answers')
