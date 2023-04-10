import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Learning\\Python_ST_2\\addressbook\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture
