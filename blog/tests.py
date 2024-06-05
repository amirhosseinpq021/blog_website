from django.test import TestCase

from .models import Post
from django.contrib.auth.models import User

from django.shortcuts import reverse


class BlogPostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='amirhossein')

        self.post1 = Post.objects.create(
            title='title',
            text='this is text',
            status=Post.STATUS_CHOICES[0][0],
            author=self.user
        )

    # تست این که بر اساس یو ار ال چک کنه صفحه میاره یا نه
    def test_post_list_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # تست بر اساس name در urls
    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    # 3
    # تست اینکه عنوان پست در صفحه باشد
    def test_title_on_blog_list_page(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)

    # 4
    # تست بر اساس اینکه بره تو صفحه detail و بررسی کن ایا متن و عنوان هست یا نه
    def test_post_detail_on_blog_detail_page(self):
        response = self.client.get(f'/posts/{self.post1.id}/')
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    # 5
    # تست بر اساس url صفحه دیتل
    def test_post_detail_url_by_name(self):
        response = self.client.ge(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    # 6
    # تست بره به صفحه جزییات پست name=post_detail
    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    # 7
    # وقتی ای دی ادن پست رو نداشته باشیم خطای 404 بده
    def test_status_404_if_not_found_posts_detail(self):
        response = self.client.get(reverse('post_detail', args=[100000]))
        self.assertEqual(response.status_code, 404)




