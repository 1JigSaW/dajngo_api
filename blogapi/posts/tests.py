from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class BlogTests(TestCase):

	@classmethod
	def setUpTestData(cls):
		testuserl = User.objects.create_user(
			username='testuserl', password='abc123'
		)
		testuserl.save()

		test_post = Post.objects.create(
			author=testuserl, title='Blog title', body='Body content...'
		)
		test_post.save()

	def test_blog_content(self):
		post = Post.objects.get(id=1)
		author = f'{post.author}'
		title = f'{post.title}'
		body = f'{post.body}'
		self.assertEqual(author, 'testuserl')
		self.assertEqual(title, 'Blog title')
		self.assertEqual(body, 'Body content...')

