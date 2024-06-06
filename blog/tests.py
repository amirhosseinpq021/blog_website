from django.test import TestCase

from .models import Post
from django.contrib.auth.models import User

from django.shortcuts import reverse


class BlogPostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='amirhossein')

        self.post1 = Post.objects.create(
            title='title1',
            text='this is text1',
            status=Post.STATUS_CHOICES[0][0],
            author=self.user
        )

        self.post2 = Post.objects.create(
            title='title2',
            text='this is text2',
            status=Post.STATUS_CHOICES[1][0],
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
    def test_post_detail_url(self):
        response = self.client.get(f'/posts/{self.post1.id}/')
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

    # 8
    # تست اینکخ پست های پیش نویس در صفحه نباشد
    def test_draft_post_not_show_on_posts_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    # 9
    # تست اینکه در مدل پست ها بر اساس عنوان نمایش داده شود --str--
    def test_post_model_str(self):
        post = self.post1
        self.assertEqual(str(post), post.title)

    # 10
    # تست اینکه همون چیزی که ذخیره میشه
    def test_post_detail(self):
        self.assertEqual(self.post1.title, 'title1')
        self.assertEqual(self.post1.text, 'this is text1')

    # 11
    # بررسی کنیم که ایا پست ساخته میشه یا نه
    def test_post_create_view(self):
        response = self.client.post(reverse('add_post'), {
            'title': 'some title',
            'text': 'this is some text',
            'status': 'pub',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'some title')
        self.assertEqual(Post.objects.last().text, 'this is some text')


    # 12
    # بررسی اینکه ایا پست ویرایش میشود
    def test_post_update_view(self):
        response = self.client.post(reverse('edit_post', args=[self.post2.id]), {
            'title': "post 2 updated",
            'text': "text update",
            'status': 'pub',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "post 2 updated")
        self.assertEqual(Post.objects.last().text, "text update")

    # 13
    # بررسی اینکه پست حذف میشود یا نه
    def test_post_delete_view(self):
        response = self.client.post(reverse('delete_post', args=[self.post1.id]))
        self.assertEqual(response.status_code, 302)


















