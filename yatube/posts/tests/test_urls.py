from django.test import TestCase, Client


class StaticURLTests(TestCase):
    
    def setUp(self) -> None:
        self.guest_client = Client()


    def test_homepage(self):
        response = self.guest_client.get('/')
        # Утверждаем, что для прохождения теста код должен быть равен 200
        self.assertEqual(response.status_code, 200)

    def test_technology_page(self):
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_author_page(self):
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, 200)