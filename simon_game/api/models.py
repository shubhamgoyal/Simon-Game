from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Symbol(models.Model):
	word = models.TextField()

class Sequence(models.Model):
	words = models.ManyToManyField(Symbol)
	class Meta:
		abstract = True

class OriginalSequence(Sequence):
	pass

class ResponseSequence(Sequence):
	originalSequence = models.ForeignKey(OriginalSequence, related_name='response_sequences')
	user = models.ForeignKey(User)