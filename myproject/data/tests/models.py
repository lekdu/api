from django.test import TestCase
from .models import Review, Company
from .forms import ReviewForm
from django.utils import timezone
from django.core.urlresolvers import reverse
from .forms import ReviewForm
import datetime 

'''
    Review model test
'''
class ReviewTest(TestCase):

    def create_review(self, title="only a test", summary="yes, this is only a test", rating=2):
        ip = socket.gethostbyname(socket.gethostname())
        return Review.objects.create(title=title, summary=body, date=timezone.now(), ip=ip, rating = rating)

    def test_review_creation(self):
        w = self.create_review()
        self.assertTrue(isinstance(w, Review))
        self.assertEqual(w.__unicode__(), w.title)
        self.assertEqual(w.__unicode__(), w.summary)
        self.assertEqual(w.__unicode__(), w.rating)

    def test_review_list_view(self):
        w = self.create_whatever()
        url = reverse("review.views.review")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(w.title, resp.content)

'''
    Company model test
'''
class CompanyTest(TestCase):

    def create_company(self, name="only a test", address="yes, this is only a test",phone="0996782313"):
        return Company.objects.create(name=name, address=address, date=timezone.now(), phone=phone)

    def test_company_creation(self):
        w = self.create_company()
        self.assertTrue(isinstance(w, Company))
        self.assertEqual(str(w), w.name)

    def test_string_representation(self):
        entry = self.create_company()
        self.assertEqual(str(entry), entry.name)

    def test_review_list_view(self):
        w = self.create_whatever()
        url = reverse("company.views.company")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(w.name, resp.content)

class ReviewFormTests(TestCase):
    def test_title_starting_lowercase(self):
        form = AddBookForm(data={"title": "a lowercase title"})

        self.assertEqual(
            form.errors["title"], ["Should start with an uppercase letter"]
        )

    def test_title_ending_full_stop(self):
        form = AddBookForm(data={"title": "A stopped title."})

        self.assertEqual(
            form.errors["title"], ["Should not end with a full stop"]
        )

    def test_title_with_ampersand(self):
        form = AddBookForm(data={"title": "Dombey & Son"})

        self.assertEqual(form.errors["title"], ["Use 'and' instead of '&'"])