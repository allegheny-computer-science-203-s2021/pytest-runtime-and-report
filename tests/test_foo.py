import pytest
import time

import conftest

# Sampled from Darlene Wong's presenation for PyOhio 2019 for testing purposes with modifications

@pytest.mark.performance
def test_foo():
    """This is the foo test"""
    assert True

@pytest.mark.high
def test_bar():
    """The bar test"""
    assert True

def test_baz():
    """The baz test
    Make sure we get multiline formatting right.
    """
    assert True

def test_short():
    """Test for a short amount of time"""
    time.sleep(3)
    assert True

def test_long():
    """Test for a long amount of time"""
    time.sleep(7)
    assert True

def test_longer():
    """Test for a longer amount of time"""
    time.sleep(12)
    assert True

class TestFoo():

    @pytest.mark.high
    @pytest.mark.performance
    def test_a(self):
        """The TestFoo.a test
        Make it a multiline docstring.
        """
        assert True

    def test_b(self):
        """The TestFoo.b test"""
        assert True

def test_collection_modifyitems():
    """this tests the method in conftest"""
    assert True
