import unittest
from unittest.mock import patch
import desktopBackgroundChange


class TestDesktopBackgroundChange(unittest.TestCase):

    def test_bad_folder(self):
        path = "C:\\Users\\Backal\\bacgrouns"
        self.assertEqual(len(desktopBackgroundChange.get_picture_list(path)), 0)

    def test_good_folder(self):
        path = "C:\\Users\\Backal\\Backgrounds"
        self.assertTrue(len(desktopBackgroundChange.get_picture_list(path))>0)

    # @patch('desktopBackgroundChange.get_picture_list', return_value=[])
    # def test_empty_backgrounds(self):
    #     self.assertEqual(desktopBackgroundChange.main(), 1)
