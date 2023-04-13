from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length=20, verbose_name='Название')
	image = models.ImageField(verbose_name='Изображение')

	def __str__(self):
		return self.name


class Posts(models.Model):
	title = models.CharField(max_length=20, verbose_name='Название')
	image = models.ImageField(verbose_name='Изображение')
	detail = models.TextField(max_length=150, verbose_name='Информация')
	date = models.DateField(auto_now_add=True)
	category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
	user = models.ForeignKey(User ,on_delete=models.CASCADE)

	def __str__(self):
		return self.title


class Comments(models.Model):
	user=models.ForeignKey(User, on_delete=models.SET_NULL,blank=True, null=True)
	product=models.ForeignKey(Posts, on_delete=models.SET_NULL,blank=True, null=True,related_name='priducts_comment')
	text=models.TextField(blank=True, max_length=35)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return 'Comment by {} on {}'.format(self.user, self.product)