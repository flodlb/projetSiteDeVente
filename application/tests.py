import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from .forms import AjouterAuPanierForm, VetementForm
from selenium import webdriver
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Vetement, Panier


class VetementModelTest(TestCase):
    def setUp(self):
        self.vetement = Vetement.objects.create(
            nom='T-shirt',
            description='Un T-shirt confortable',
            qnte=10,
            prix=20
        )

    def test_vetement_str(self):
        self.assertEqual(str(self.vetement), 'T-shirt')

    def test_vetement_delete(self):
        image_path = self.vetement.image.path if self.vetement.image else None
        self.vetement.delete()
        if image_path:
            self.assertFalse(os.path.isfile(image_path))


class AjouterAuPanierFormTest(TestCase):
    def test_ajouter_au_panier_form_valid(self):
        form_data = {'qnte': 2}
        form = AjouterAuPanierForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_ajouter_au_panier_form_invalid(self):
        form_data = {'qnte': 0}
        form = AjouterAuPanierForm(data=form_data)
        self.assertFalse(form.is_valid())


class VetementFormTest(TestCase):
    def test_vetement_form_valid(self):
        form_data = {'nom': 'Jeans', 'description': 'Pantalon en denim', 'qnte': 5, 'prix': 50}
        form = VetementForm(data=form_data)
        self.assertTrue(form.is_valid())


class IntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='complex_password123')
        self.vetement = Vetement.objects.create(
            nom='T-shirt',
            description='Un T-shirt confortable',
            qnte=10,
            prix=20
        )
        self.client.login(username='testuser', password='complex_password123')

    def test_add_to_panier(self):
        response = self.client.post(reverse('application:addToPanier', args=[self.vetement.id_V]), {'qnte': 2})
        self.assertEqual(response.status_code, 302)
        panier_item = Panier.objects.get(id_U=self.user, id_V=self.vetement)
        self.assertEqual(panier_item.qnte, 2)
        self.vetement.refresh_from_db()
        self.assertEqual(self.vetement.qnte, 8)


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.user = User.objects.create_user(username='testuser', password='complex_password123')

    def tearDown(self):
        self.browser.quit()

    def test_user_can_add_vetement_to_panier(self):
        self.browser.get(self.live_server_url + reverse('compte:login'))
        self.browser.get(self.live_server_url + reverse('application:viewPanier'))
