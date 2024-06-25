import unittest
from unittest.mock import patch, Mock
from beets.library import Item
from beets.autotag.match import match_by_id

class TestMatchById(unittest.TestCase):
    def setUp(self):
        global Item

        class ItemMock:
            def __init__(self, mb_albumid):
                self.mb_albumid = mb_albumid

        self.Item = ItemMock

    def test_no_album_id(self):
        items = [self.Item(None), self.Item(None)]
        self.assertIsNone(match_by_id(items))

    @patch('beets.autotag.match.hooks.album_for_mbid')
    def test_consensus(self, mock_album_for_mbid):
        mock_album_for_mbid.return_value = "AlbumInfo for 123"
        items = [self.Item("123"), self.Item("123"), self.Item("123")]
        self.assertEqual(match_by_id(items), "AlbumInfo for 123")

    def test_no_consensus(self):
        items = [self.Item("123"), self.Item("456"), self.Item("123")]
        self.assertIsNone(match_by_id(items))

    @patch('beets.autotag.match.hooks.album_for_mbid')
    def test_loop_execution(self, mock_album_for_mbid):
        mock_album_for_mbid.return_value = "AlbumInfo for 123"
        items = [self.Item("123"), self.Item("123"), self.Item("123"), self.Item("123")]
        self.assertEqual(match_by_id(items), "AlbumInfo for 123")

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMatchById))
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest="suite")
