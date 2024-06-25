import unittest
from unittest.mock import patch
import subprocess

from beets.test.helper import has_program


class TestHasProgram(unittest.TestCase):
    @patch(
        "subprocess.check_call",
        side_effect=subprocess.CalledProcessError(1, "cmd"),
    )
    def test_called_process_error(self, mock_subprocess):
        self.assertFalse(has_program("some_command"))

    @patch("subprocess.check_call", side_effect=OSError)
    def test_os_error(self, mock_subprocess):
        self.assertFalse(has_program("some_command"))

    @patch("subprocess.check_call", return_value=0)
    def test_success(self, mock_subprocess):
        self.assertTrue(has_program("some_command"))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestHasProgram))
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest="suite")
