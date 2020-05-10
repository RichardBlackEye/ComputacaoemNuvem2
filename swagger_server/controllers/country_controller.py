import connexion
import six

from swagger_server.models.country import Country  # noqa: E501
from swagger_server import util


def add_country(CountryCode, ShortName):  # noqa: E501
    """Add a new country to the dataset

     # noqa: E501

    :param CountryCode: Code of the country
    :type CountryCode: str
    :param ShortName: Short name of the country
    :type ShortName: str

    :rtype: None
    """
    return 'do some magic!'


def delete_country(CountryCode, api_key=None):  # noqa: E501
    """Deletes a country

     # noqa: E501

    :param CountryCode: Country  to delete
    :type CountryCode: str
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def get_country_by_id(CountryCode):  # noqa: E501
    """Find country by ID

    Returns a single country # noqa: E501

    :param CountryCode: ID of country to return
    :type CountryCode: int

    :rtype: Country
    """
    return 'do some magic!'


def update_country_with_form(CountryCode, name=None, status=None):  # noqa: E501
    """Updates a country in the dataset with form data

     # noqa: E501

    :param CountryCode: ID of country that needs to be updated
    :type CountryCode: int
    :param name: Updated name of the country
    :type name: str
    :param status: Updated status of the country
    :type status: str

    :rtype: None
    """
    return 'do some magic!'
