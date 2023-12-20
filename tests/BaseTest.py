import pytest
import unittest


@pytest.mark.usefixtures("appium_driver")
class BaseTest(unittest.TestCase):
    pass
