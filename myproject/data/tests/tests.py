from django.test import TestCase
from .models import Review, Company
from django.utils import timezone
from django.core.urlresolvers import reverse
from .forms import ReviewForm

'''
    Review model test
'''
class ReviewTest(TestCase):

    def create_review(self, title="only a test", summary="yes, this is only a test"):
        return Review.objects.create(title=title, summary=body, date=timezone.now())

    def test_review_creation(self):
        w = self.create_review()
        self.assertTrue(isinstance(w, Review))
        self.assertEqual(w.__unicode__(), w.title)

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
        return Company.objects.create(name=name, address=address, date=timezone.now())

    def test_company_creation(self):
        w = self.create_company()
        self.assertTrue(isinstance(w, Company))
        self.assertEqual(w.__unicode__(), w.name)

    def test_review_list_view(self):
        w = self.create_whatever()
        url = reverse("company.views.company")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(w.name, resp.content)
