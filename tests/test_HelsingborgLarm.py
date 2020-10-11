from helsingborgalarm import HelsingborgAlarm
from unittest import TestCase


class TestHelsingborgAlarm(TestCase):

    def test_download_json(self):
        hl = HelsingborgAlarm()
        assert len(hl.get_larms()) > 0

    def test_load_json_file(self):
        hl = HelsingborgAlarm(download=False)
        hl.load_json_file('example.json')
        assert len(hl.get_larms()) > 0




