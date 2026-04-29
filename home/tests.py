from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post

User = get_user_model()


class HomeViewsTests(TestCase):
    def test_home_returns_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_admin_url_is_not_matched_as_post_slug(self):
        """Evita regressão: /admin/ não deve cair no PostDetailView."""
        response = self.client.get('/admin/')
        self.assertIn(
            response.status_code,
            (200, 302),
            msg='/admin/ deve ser o site admin (200 ou redirect para login), não 404 de post.',
        )

    def test_post_detail_shows_published_post(self):
        user = User.objects.create_user(username='tester', password='pass12345')
        post = Post.objects.create(
            title='Post de teste',
            content='Conteúdo',
            status='published',
            author=user,
        )
        response = self.client.get(reverse('post_detail', kwargs={'slug': post.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.title)

    def test_post_detail_404_for_nonexistent_slug(self):
        response = self.client.get(reverse('post_detail', kwargs={'slug': 'slug-inexistente'}))
        self.assertEqual(response.status_code, 404)
