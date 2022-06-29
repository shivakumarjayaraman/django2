from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from .models import Post

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!!")

    def test_url_exists_at_correct_location(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_web_stuff(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home.html")
        self.assertContains(resp, "This is a test")
