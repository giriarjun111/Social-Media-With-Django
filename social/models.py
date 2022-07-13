from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	image = models.ManyToManyField('ImageModel', blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	likes = models.ManyToManyField(User, blank=True, related_name='likes')
	dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

class Comment(models.Model):
	comment = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
	dislikes = models.ManyToManyField(User, blank=True, related_name='comment_dislikes')
	parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')

	@property
	def children(self):
		return Comment.objects.filter(parent=self).order_by('-created_on').all()

	@property
	def is_parent(self):
		if self.parent is None:
			return True
		else:
			return False

class userProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
	name = models.CharField(max_length=50, blank=True, null=True)
	bio = models.TextField(max_length=200, blank=True, null=True)
	dob = models.DateField(null=True, blank=True)
	location = models.CharField(max_length=100, blank=True, null=True)
	picture = models.ImageField(upload_to='uploads/profile_pictures', blank=True)
	followers = models.ManyToManyField(User, blank=True, related_name='followers')

	def __str__(self):
		return self.user.username


class Notification(models.Model):
	# 1 = Like, 2 = Comment, 3 = Follow, 4 = DM
	notification_type = models.IntegerField()
	to_user = models.ForeignKey(User, related_name='notification_to', on_delete=models.CASCADE, null=True)
	from_user = models.ForeignKey(User, related_name='notification_from', on_delete=models.CASCADE, null=True)
	post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='+', blank=True, null=True)
	comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='+', blank=True, null=True)
	thread = models.ForeignKey('ThreadModel', on_delete=models.CASCADE, related_name='+', blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)
	user_has_seen = models.BooleanField(default=False)

class ThreadModel(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

	def __str__(self):
		return f'{self.user} - {self.receiver}'

class MessageModel(models.Model):
	thread = models.ForeignKey('ThreadModel', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
	sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	body = models.CharField(max_length=1000)
	image = models.ImageField(upload_to='uploads/message_photos', blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)
	is_read = models.BooleanField(default=False)


class ImageModel(models.Model):
	image = models.ImageField(upload_to='uploads/post_photos', blank=True, null=True)