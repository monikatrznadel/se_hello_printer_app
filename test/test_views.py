import unittest
import json
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        expected = {'imie': 'Maria', 'msg': 'Hello World!'}
        actual = json.loads(rv.data)
        self.assertEqual(expected['imie'], actual['imie'])
        self.assertEqual(expected['msg'], actual['msg'])

    def test_message_output_with_name(self):
        expected_name = 'Natalia'
        rv = self.app.get('/?output=json&name={0}'.format(expected_name))
        actual = json.loads(rv.data)
        self.assertEqual(expected_name, actual['imie'])
