from django.db import models
from django.utils import timezone
import os

def get_image_path(instance, filename):
    return os.path.join('media', str(instance.id), filename )
#    pass

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    image = models.ImageField(upload_to='media/blog_media', blank=True, null=True)
    #post_image = get_image_path(objects.image, 'image')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
