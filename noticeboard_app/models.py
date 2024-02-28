from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

POSTCATEGORY = [
    ('other', 'Прочее'),
    ('tanks', 'Танки'), 
    ('holls', 'Хилы'), 
    ('DD', 'ДД'), 
    ('traders', 'Торговцы'), 
    ('guildmeisters', 'Гилдмастеры'), 
    ('questgivers', 'Квестгиверы'), 
    ('blacksmiths', 'Кузнецы'), 
    ('tanners', 'Кожевники'), 
    ('potion_makers', 'Зельевары'), 
    ('spell_masters', 'Мастера заклинаний')
]

class Post(models.Model):
    name = models.CharField(max_length = 255)
    category = models.CharField(max_length = 20, choices = POSTCATEGORY, default = 'other')
    # text = models.TextField()
    text = RichTextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateField(auto_now_add = True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('postdetail', args=[str(self.id)])


APPROVAL_STATUS = [
    ('RA',  'requires approval'),
    ('A', 'approved'),
    ('NA', 'not approved'),
]

class Comment(models.Model):
    text = models.TextField(max_length = 1024)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    date = models.DateField(auto_now_add = True)
    approved =  models.CharField(max_length = 20, choices = APPROVAL_STATUS, default = 'RA')

    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return reverse('commentdetail', args=[str(self.id)])