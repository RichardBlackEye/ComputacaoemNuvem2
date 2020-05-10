# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.country import Country  # noqa: E501
from swagger_server.models.indicator import Indicator  # noqa: E501
from swagger_server.test import BaseTestCase


class TestIndicatorController(BaseTestCase):
    """IndicatorController integration test stubs"""

    def test_add_indicator(self):
        """Test case for add_indicator

        Add a new indicator to the dataset
        """
        body = Indicator()
        response = self.client.open(
            '/bigquery/v2/projects/cloudcomputworlddevelopment/datasets/ccworlddataset/indicator',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_indicator(self):
        """Test case for delete_indicator

        Deletes a indicator
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/bigquery/v2/projects/cloudcomputworlddevelopment/datasets/ccworlddataset/indicator/{indicatorId}'.format(indicatorId=789),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_indicator_by_id(self):
        """Test case for get_indicator_by_id

        Find indicator by ID
        """
        response = self.client.open(
            '/bigquery/v2/projects/cloudcomputworlddevelopment/datasets/ccworlddataset/indicator/{indicatorId}'.format(indicatorId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_indicator_with_form(self):
        """Test case for update_indicator_with_form

        Updates a indicator in the dataset with form data
        """
        data = dict(name='name_example',
                    status='status_example')
        response = self.client.open(
            '/bigquery/v2/projects/cloudcomputworlddevelopment/datasets/ccworlddataset/indicator/{indicatorId}'.format(indicatorId=789),
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
