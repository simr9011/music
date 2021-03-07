from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
class Album(models.Model):
    title=models.CharField(max_length=100,null=False,help_text='Album title')
    artist = models.CharField(max_length=100,help_text='Album artist')
    genre = models.CharField(max_length=50,help_text='Album genre')
    year= models.DateField(help_text='Album year')
    image= models.FileField(validators=[FileExtensionValidator(['jpg','png'])],default='')

    def __str__(self):
        return self.title
class Song(models.Model):
    title = models.CharField(max_length=100, null=False, help_text='Songs title')
    artist = models.CharField(max_length=100,help_text='Song artist')
    genre = models.CharField(max_length=50,help_text='Song genre')
    al_id=models.ForeignKey(Album,on_delete=models.CASCADE)
    image=models.FileField(validators=[FileExtensionValidator(['jpg','png'])])
    soundfile = models.FileField(validators=[FileExtensionValidator(['mp3', 'aac'])])

    def __str__(self):
        return self.title



