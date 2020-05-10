# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.country import Country  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCountryController(BaseTestCase):
    """CountryController integration test stubs"""

    def test_add_country(self):
        """Test case for add_country

        Add a new country to the dataset
        """
        data = dict(CountryCode='CountryCode_example',
                    ShortName='ShortName_example')
        response = self.client.open(
            '/bigquery/v2/projects/cloudcomputworlddevelopment/datasets/ccworlddataset/tables/country',
            method='POST',
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_country(self):
        """Test case for delete_country

        Deletes a country
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/bigquery/v2/projects/cloudcomputworlddevelopment/datasets/ccworlddataset/tables/country/{CountryCode}'.format(CountryCode='CountryCode_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_country_by_id(self):
        """Test case for get_country_by_id

        Find country by ID
        """
        response = self.client.open(
            '/bigquery/v2/projects/cloudcomputworlddevelopment/datasets/ccworlddataset/tables/country/{CountryCode}'.format(CountryCode=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_country_with_form(self):
        """Test case for update_country_with_form

        Updates a country in the dataset with form data
        """
        data = dict(name='name_example',
                    status='status_example')
        response = self.client.open(
            '/bigquery/v2/projects/cloudcomputworlddevelopment/datasets/ccworlddataset/tables/country/{CountryCode}'.format(CountryCode=789),
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
