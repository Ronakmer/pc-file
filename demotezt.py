# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from color.models import Color
from django.contrib.auth import get_user_model




class AuthViewsTests(APITestCase):
    def setUp(self):
        self.username = "usuario"
        self.password = "contrasegna"
        self.data = {"username": self.username, "password": self.password}

    def test_current_user(self):
        url = reverse("token_obtain_pair")

        user = User.objects.create_user(
            username="usuario", email="usuario@mail.com", password="contrasegna"
        )
        self.assertEqual(user.is_active, 1, "Active User")

        response = self.client.post(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        token = response.data["access"]

        # self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(token))
        token_data = {"token": token}
        response = self.client.post(reverse("token_verify"), token_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)

class ColorAPITestCase(APITestCase):
     
    def setUp(self):
        self.client = APIClient()  # Initialize the client
        self.user = get_user_model().objects.create_user(
            username='admin',
            password='admin'
        )
        url = reverse('token_obtain_pair')
        self.data = {
            "username": "admin",
            "password": "admin"
        }
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        self.form_date = {
            "id": 1,
            "name": "aasdasdasd",
            "hex": "#asdhadjbadjkbd",
            "status": "active",
        }

    def test_color(self):
        self.color = Color.objects.create(name = "name", hex = "hex")
        # self.token = token

        url = reverse('Color-list')

        data  = {
        #    "id" : "id",
           "name":"aasdasdasd",
           "hex": "#asdhadjbadjkbd",
            "status":"active"
       }
        
        response = self.client.post(url, data, format='json')
        # self.token = response.data['access']
        # self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.token))
        response = self.client.get(reverse('Color-list'),data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)