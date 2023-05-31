import pytest
from unittest import mock
from requests.models import Response
from ..src.modules.module import total, listTotal, getResponseCode, getRequest

def test_total_0():
    assert total(0, 0) == 0

def test_total_1():
    assert total(0, 1) == 1

def test_total_3():
    assert total(1, 2) == 3

def test_total_4():
    assert total(1, 3) == 4

def test_total_minus4():
    assert total(0, -4) == -4

def test_list_total_None():
    assert listTotal([]) == 0

def test_list_total_6():
    assert listTotal([1.0, 2.0, 3.0]) == 6.0

def test_can_use_third_party_package():
    assert getResponseCode() == 200

def test_can_make_get_request(mocker):
    # Arrange
    expected_status_code = 200
    mocked_request = Response()
    mocked_request.status_code = expected_status_code

    mocker.patch('requests.get', return_value=mocked_request)

    # Act
    actual_response = getRequest('https://doesntexist.secarma.com/')

    # Assert
    assert actual_response.status_code == expected_status_code
