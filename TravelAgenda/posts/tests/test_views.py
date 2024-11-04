from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from posts.models import Post, Image, Comment
import uuid
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
class MyPostListViewTests(TestCase):
    def setUp(self):
        # 创建两个用户
        self.user1 = get_user_model().objects.create_user(username='user1', password='testpass')
        self.user2 = get_user_model().objects.create_user(username='user2', password='testpass')

        # 登录第一个用户
        self.client.login(username='user1', password='testpass')

        # 为两个用户创建各自的帖子
        for i in range(15):
            Post.objects.create(
                title=f'User1 Post {i}',
                content=f'Content of user1 post {i}',
                user=self.user1
            )
        for i in range(5):
            Post.objects.create(
                title=f'User2 Post {i}',
                content=f'Content of user2 post {i}',
                user=self.user2
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/posts/mypost')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('posts:my_post'))
        self.assertEqual(response.status_code, 200)

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('posts:my_post'))
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['posts']), 10)  # 确认分页显示10个帖子

    def test_only_user_posts_displayed(self):
        response = self.client.get(reverse('posts:my_post'))
        posts = response.context['posts']
        # 确认只显示 user1 的帖子
        self.assertTrue(all(post.user == self.user1 for post in posts))
        self.assertNotIn('User2 Post 0', [post.title for post in posts])

    def test_ordering_by_created_at(self):
        response = self.client.get(reverse('posts:my_post'))
        posts = response.context['posts']
        # 确认按创建时间降序排序
        for i in range(len(posts) - 1):
            self.assertGreaterEqual(posts[i].created_at, posts[i + 1].created_at)

    def test_search_functionality(self):
        response = self.client.get(reverse('posts:my_post') + '?q=User1 Post 1')
        posts = response.context['posts']
        # 确认搜索结果包含 "User1 Post 1" 关键字
        self.assertTrue(all('User1 Post 1' in post.title for post in posts))

class PostListViewTests(TestCase):
    def setUp(self):
        # 创建一个用户并登录
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # 创建一些测试帖子
        for i in range(15):  # 创建15个帖子用于分页测试
            post = Post.objects.create(
                title=f'Test Post {i}',
                content=f'Some content for post {i}',
                user=self.user
            )
            # 模拟点赞数
            for j in range(i):  # 每个帖子分配不同数量的点赞数
                unique_username = f'liker_{uuid.uuid4().hex[:8]}'  # 生成一个唯一用户名
                liker = get_user_model().objects.create_user(username=unique_username, password='pass')
                post.likes.add(liker) 

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/posts/list')  
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('posts:post_list'))  
        self.assertEqual(response.status_code, 200)

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('posts:post_list'))
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertEqual(len(response.context['posts']), 10)  # 每页应有10个帖子

    def test_ordered_by_likes(self):
        response = self.client.get(reverse('posts:post_list'))
        posts = response.context['posts']
        # 确认按点赞数排序
        for i in range(len(posts) - 1):
            self.assertGreaterEqual(posts[i].num_likes, posts[i + 1].num_likes)

    def test_search_functionality(self):
        response = self.client.get(reverse('posts:post_list') + '?q=Test Post 1')
        posts = response.context['posts']
        # 确认搜索结果包含 "Test Post 1" 关键字
        self.assertTrue(all('Test Post 1' in post.title for post in posts))

class MyPostDetailViewTests(TestCase):
    def setUp(self):
        User = get_user_model()
        # Create a user and log them in
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a post and comments
        self.post = Post.objects.create(user=self.user, title='Test Post', content='Test content')
        for i in range(25):
            Comment.objects.create(post=self.post, user=self.user, content=f'Comment {i}')

        self.url = reverse('posts:mypost_detail', kwargs={'pk': self.post.id})

    def test_access_by_logged_in_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/mypost_detail.html')

    def test_access_by_anonymous_user(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')

    def test_context_data(self):
        response = self.client.get(self.url)
        self.assertIn('post', response.context)
        self.assertIn('images', response.context)
        self.assertIn('comments', response.context)
        self.assertEqual(len(response.context['comments']), 10)  # Paginated, so only 10

class PostDetailViewTests(TestCase):
    def setUp(self):
        User = get_user_model()
        # Create a user and log them in
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a post and comments
        self.post = Post.objects.create(user=self.user, title='Test Post', content='Test content')
        self.image = Image.objects.create(post=self.post, image=SimpleUploadedFile("test.jpg", b"file_content"))
        for i in range(25):
            Comment.objects.create(post=self.post, user=self.user, content=f'Comment {i}')

        self.url = reverse('posts:post_detail', kwargs={'pk': self.post.id})

    def test_access_by_logged_in_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_detail.html')

    def test_access_by_anonymous_user(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')

    def test_context_data(self):
        response = self.client.get(self.url)
        self.assertIn('post', response.context)
        self.assertIn('images', response.context)
        self.assertIn('comments', response.context)
        self.assertIn('form', response.context)
        self.assertEqual(len(response.context['comments']), 10)  # Paginated, so only 10

class CommentCreateViewTests(TestCase):
    def setUp(self):
        # Create a user and log them in
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a post
        self.post = Post.objects.create(user=self.user, title='Test Post', content='Test content')
        self.url = reverse('posts:add_comment', kwargs={'pk': self.post.id})

    def test_create_comment(self):
        response = self.client.post(self.url, {'content': 'New comment'})
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.first().content, 'New comment')

    def test_create_reply_comment(self):
        parent_comment = Comment.objects.create(post=self.post, user=self.user, content='Parent comment')
        response = self.client.post(self.url, {
            'content': 'Reply comment',
            'parent_id': parent_comment.id
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Comment.objects.count(), 2)
        self.assertEqual(Comment.objects.last().parent, parent_comment)

    def test_access_by_anonymous_user(self):
        self.client.logout()
        response = self.client.post(self.url, {'content': 'Anonymous comment'})
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')