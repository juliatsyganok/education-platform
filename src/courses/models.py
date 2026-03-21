from django.db import models
from django.contrib.auth.models import User

class Cource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    data = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    cource = models.ForeignKey(Cource, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=200)
    content = models.TextField()
    num = models.IntegerField()

    def __str__(self):
        return self.name
    
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cource = models.ForeignKey(Cource, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.cource.title}"
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_images/', blank=True)

    def __str__(self):
        return self.user.username


