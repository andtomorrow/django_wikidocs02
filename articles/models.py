from django.db import models

class Article(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField()
    
    def __str__(self):
        return self.subject

