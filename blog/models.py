from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    #글작성자
    author=models.ForeignKey('auth.user')
    #글제목
    title=models.CharField(max_length=200)
    #글내용
    text = models.TextField()
    # #migration test
    # test = models.TextField()
    #글작성 일자
    created_date= models.DateTimeField(default=timezone.now)
    #글게시 일자
    published_date= models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
