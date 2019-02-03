from rest_framework.test import APITestCase, APIRequestFactory
from intapp import apiviews


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
