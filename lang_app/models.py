from django.db import models

class AnkiCard(models.Model):
    id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=64)
    translation = models.CharField(max_length=64)
    image = models.ImageField(upload_to='static/anki')
    def __str__(self):
        return self.word + '[' + self.translation + ']'
    class Meta:
        # managed=False
        db_table = 'anki_card'

class Topic(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name
    class Meta:
        # managed=False
        db_table = 'topic'

class Lesson(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    topic = models.ForeignKey('Topic',on_delete=models.CASCADE)
    grade = models.IntegerField()
    def __str__(self):
        return str(self.topic) + ' [' + str(self.date) + ']' + ' ' + str(self.grade)
    class Meta:
        # managed=False
        db_table = 'lesson'