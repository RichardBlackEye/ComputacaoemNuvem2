import connexion
import six

from swagger_server.models.country import Country  # noqa: E501
from swagger_server.models.indicator import Indicator  # noqa: E501
from swagger_server import util


def add_indicator(body):  # noqa: E501
    """Add a new indicator to the dataset

     # noqa: E501

    :param body: Indicator object that needs to be added to the dataset
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Indicator.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_indicator(indicatorId, api_key=None):  # noqa: E501
    """Deletes a indicator

     # noqa: E501

    :param indicatorId: Indicator id to delete
    :type indicatorId: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def get_indicator_by_id(indicatorId):  # noqa: E501
    """Find indicator by ID

    Returns a single indicator # noqa: E501

    :param indicatorId: ID of indicator to return
    :type indicatorId: int

    :rtype: Country
    """
    return 'do some magic!'


def update_indicator_with_form(indicatorId, name=None, status=None):  # noqa: E501
    """Updates a indicator in the dataset with form data

     # noqa: E501

    :param indicatorId: ID of indicator that needs to be updated
    :type indicatorId: int
    :param name: Updated name of the indicator
    :type name: str
    :param status: Updated status of the indicator
    :type status: str

    :rtype: None
    """
    return 'do some magic!'
