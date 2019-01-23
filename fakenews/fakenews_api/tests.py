import datetime, json
from django.test import TestCase
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from fakenews_api import apiviews
from fakenews_api.models import Report


def get_test_single_report():
    return [{'title' : 'TEST post title',
            'author' : 'TEST post author',
            'content' : 'TEST post content',
            'is_train' : True,
            'label' : 0}]

# Tests for the rest api framework
class TestReport(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = apiviews.ReportViewSet.as_view({'get' : 'list'})
        self.uri = '/api/reports/'
        self.headers = {'Content-Type': 'application/json', 'Accept':'application/json'}

    def test_list(self):
        EXPECTED_CODE = 200
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, EXPECTED_CODE,
                         'Expected Response Code {}, received {} instead.'
                         .format(EXPECTED_CODE, response.status_code))

    def test_create(self):
        EXPECTED_CODE = 201
        data = get_test_single_report()
        response = self.client.post(self.uri, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, EXPECTED_CODE,
                         'Expected Response Code {}, received {} instead.'
                         .format(EXPECTED_CODE, response.status_code))
        self.assertEqual(Report.objects.count(), 1)
        self.assertEqual(Report.objects.get().title, "TEST post title")


    def test_delete(self):
        EXPECTED_CODE = 204
        data = get_test_single_report()

        self.client.post(self.uri, json.dumps(data), content_type='application/json')
        self.uri = self.uri + str(Report.objects.get().pk) + "/"
        response = self.client.delete(self.uri, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, EXPECTED_CODE,
                         'Expected Response Code {}, received {} instead.'
                         .format(EXPECTED_CODE, response.status_code))
        self.assertEqual(Report.objects.count(), 0)

# Tests for the web views
class TestWebViews(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = apiviews.ReportViewSet.as_view({'get' : 'list'})
        self.uri = "/"

    def test_index(self):
        self.uri = '/'
        EXPECTED_CODE = 200
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, EXPECTED_CODE,
                         'Expected Response Code {}, received {} instead.'
                         .format(EXPECTED_CODE, response.status_code))

    def test_training(self):
        self.uri = '/training/'
        EXPECTED_CODE = 200
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, EXPECTED_CODE,
                         'Expected Response Code {}, received {} instead.'
                         .format(EXPECTED_CODE, response.status_code))

    def test_detail(self):
        EXPECTED_CODE = 200
        data = get_test_single_report()
        self.uri = '/api/reports/'
        response = self.client.post(self.uri, json.dumps(data), content_type='application/json')

        self.uri = '/reports/' + str(Report.objects.get().pk) + "/"
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, EXPECTED_CODE,
                         'Expected Response Code {}, received {} instead.'
                         .format(EXPECTED_CODE, response.status_code))
