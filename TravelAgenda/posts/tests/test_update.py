from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from posts.models import Post, Image

User = get_user_model()

class PostSendViewTests(TestCase):
    def setUp(self):
        # Create a user and log them in
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_post_send_success(self):
        # Simulate a successful form submission
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        response = self.client.post(reverse('posts:send'), {
            'title': 'Test Post Title',
            'content': 'This is a test post content',
            'images': [image]
        })

        # Check if it redirects to 'my_post'
        self.assertRedirects(response, reverse('posts:my_post'))

        # Check if the post was created successfully and associated with the current user
        post = Post.objects.get(title='Test Post Title')
        self.assertEqual(post.user, self.user)
        self.assertEqual(post.content, 'This is a test post content')
        self.assertEqual(post.images.count(), 1)  # Check that the image was uploaded

    def test_post_send_content_too_long(self):
        # Simulate a form submission with content that exceeds the character limit
        long_content = 'A' * 201  # Assuming the character limit is 200
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        response = self.client.post(reverse('posts:send'), {
            'title': 'Test Post Title',
            'content': long_content,
            'images': [image]
        })

        # Check that it does not redirect and instead re-renders the form (status code 200)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'content', 'Ensure this value has at most 200 characters (it has 201).')

    def test_post_send_too_many_images(self):
        # Simulate a form submission with too many images
        images = [
            SimpleUploadedFile(f"test_image_{i}.jpg", b"file_content", content_type="image/jpeg")
            for i in range(10)  # Assuming the image limit is 9
        ]
        response = self.client.post(reverse('posts:send'), {
            'title': 'Test Post Title',
            'content': 'This is a test post content',
            'images': images
        })

        # Check that it does not redirect and instead re-renders the form (status code 200)
        self.assertEqual(response.status_code, 200)
        # You may need to customize this error message based on your form's validation
        self.assertContains(response, 'You can only upload up to 9 images.')

class PostUpdateViewTests(TestCase):
    def setUp(self):
        # Create a user and log in
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create another user
        self.other_user = User.objects.create_user(username='otheruser', password='otherpassword')

        # Create a post and related images for the test user
        self.post = Post.objects.create(user=self.user, title='Test Post', content='Test content')
        self.image = Image.objects.create(post=self.post, image=SimpleUploadedFile("test.jpg", b"file_content"))

        # URL for the PostUpdateView
        self.update_url = reverse('posts:post_edit', args=[self.post.id])

    def test_view_accessible_by_owner(self):
        # Test that the post owner can access the update view
        response = self.client.get(self.update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/edit.html')

    def test_view_not_accessible_by_other_user(self):
        # Log in as a different user
        self.client.logout()
        self.client.login(username='otheruser', password='otherpassword')

        # Try to access the update view
        response = self.client.get(self.update_url)
        self.assertEqual(response.status_code, 404)  # Expecting a 404, since they shouldn't access it

    def test_post_update_valid_data(self):
        # Upload a new image and update post content
        new_image = SimpleUploadedFile("new_test.jpg", b"new_file_content")
        response = self.client.post(self.update_url, {
            'title': 'Updated Title',
            'content': 'Updated content',
            'image_formset-TOTAL_FORMS': '2',
            'image_formset-INITIAL_FORMS': '1',
            'image_formset-0-id': self.image.id,
            'image_formset-0-DELETE': '',
            'image_formset-1-image': new_image
        })

        # Debug: Output form errors if the response is not a redirect
        if response.status_code == 200:
            print("Form errors:", response.context['form'].errors)
            for form in response.context['image_formset']:
                print("Image form errors:", form.errors)

        # Check redirection after successful update
        self.assertRedirects(response, reverse('posts:my_post'))

        # Verify the post was updated
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')
        self.assertEqual(self.post.content, 'Updated content')

        # Verify that a new image was added
        self.assertEqual(self.post.images.count(), 2)

    def test_post_update_delete_image(self):
        # Test deleting the existing image
        response = self.client.post(self.update_url, {
            'title': 'Updated Title',
            'content': 'Updated content',
            'image_formset-TOTAL_FORMS': '1',
            'image_formset-INITIAL_FORMS': '1',
            'image_formset-0-id': self.image.id,
            'image_formset-0-DELETE': 'on'
        })

        # Check redirection after successful update
        self.assertRedirects(response, reverse('posts:my_post'))

        # Verify the post was updated
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')
        self.assertEqual(self.post.content, 'Updated content')

        # Verify that the image was deleted
        self.assertEqual(self.post.images.count(), 0)

    def test_invalid_data_submission(self):
        # Test with invalid form data (e.g., content too short)
        response = self.client.post(self.update_url, {
            'title': 'Updated Title',
            'content': '',  # Invalid content
            'image_formset-TOTAL_FORMS': '1',
            'image_formset-INITIAL_FORMS': '1',
            'image_formset-0-id': self.image.id
        })

        # Check that the form is invalid and returns the edit page
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/edit.html')
        self.assertFormError(response, 'form', 'content', 'This field is required.')

    def test_only_authenticated_user_can_access(self):
        # Log out the current user
        self.client.logout()

        # Try to access the update view
        response = self.client.get(self.update_url)
        self.assertRedirects(response, f'/accounts/login/?next={self.update_url}')  # Redirects to login
