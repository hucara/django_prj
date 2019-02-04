from rest_framework.test import APITestCase, APIRequestFactory
from intapp import apiviews
import json


def get_search_one_doc():
    return [{'query': 'illness', 'return': 1}]

def get_search_many_docs():
    return [{'query': 'illness', 'return': 10}]


# Tests for the rest api framework
class TestReport(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.uri = '/api/search/'
        self.headers = {'Content-Type': 'application/json',
                        'Accept': 'application/json'}

    def test_search_one_doc(self):
        EXPECTED_CODE = 200
        data = get_search_one_doc()
        response = self.client.post(
            self.uri, json.dumps(data),
            content_type='application/json'
        )

        self.assertEqual(
            response.status_code, EXPECTED_CODE,
            'Expected Response Code {}, received {} instead.'
            .format(EXPECTED_CODE, response.status_code)
        )

        self.assertEqual(len(response.data), 1)


    def test_search_many_docs(self):
        EXPECTED_CODE = 200
        data = get_search_one_doc()
        len_docs = data[0]['return']
        response = self.client.post(
            self.uri, json.dumps(data),
            content_type='application/json'
        )

        self.assertEqual(
            response.status_code, EXPECTED_CODE,
            'Expected Response Code {}, received {} instead.'
            .format(EXPECTED_CODE, response.status_code)
        )

        self.assertEqual(len(response.data), len_docs)


# Create your tests here.
class TestWebViews(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = apiviews.ReportViewSet.as_view({'get': 'list'})
        self.uri = "/"

    def test_index(self):
        self.uri = '/'
        EXPECTED_CODE = 200
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(
            response.status_code, EXPECTED_CODE,
            'Expected Response Code {}, received {} instead.'
            .format(EXPECTED_CODE, response.status_code)
        )
