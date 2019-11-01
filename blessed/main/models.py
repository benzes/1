from django.db import models

# Create your models here.

#postprod
class PostProd(models.Model):
	title = models.CharField(verbose_name='Титул', max_length=40)
	typecontent = models.ForeignKey('Types', verbose_name='Тип', on_delete='PROTECT')
	content = models.TextField(max_length=300, verbose_name='Контент')
	datetoo = models.DateTimeField(auto_now_add=True, db_index=True)
	like = models.PositiveIntegerField(default=0, verbose_name='Лайк')
	dislike = models.PositiveIntegerField(default=0, verbose_name='Дизлайк')

	def __str__(self):
		name = self.title
		return name

class Types(models.Model):
	name = models.CharField(max_length=30, verbose_name='Тип')
	def __str__(self):
		return self.name

