from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
"""
-class post(models.Model) defines model (is object).
-class means defining object
-post is name of model (always start class name with uppercase)
-models.Model means the post is a django model, so django knows it should
be saved in the database
"""
"""
-models.CharField - how you define text with limited characters
-models.TextField - for long text without limit. Ideal for blog post
-models.DateTimeField - this adds date and time
-models.ForeignKey - link to another model 
"""