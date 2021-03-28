from hello_world.formater import plain_text_upper_case
from hello_world.formater import plain_text_lower_case
from hello_world.formater import format_to_xml
from hello_world.formater import plain_text
from hello_world.formater import format_to_json

import unittest
import json
import xml.etree.cElementTree as ET


class TestFormater(unittest.TestCase):
    def test_plain_uppercase(self):
        r = plain_text_upper_case("wwww", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())

    def test_plain_text_lower_case(self):
        r = plain_text_lower_case("wwww", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.islower())
        self.assertTrue(msg.islower())

    def test_format_to_xml(self):
        name = "Krysia"
        msg = "Hello"
        result = format_to_xml(msg, name)
        actual = ET.fromstring(result)
        actualName = actual.find("name")
        actualMsg = actual.find("msg")
        self.assertEqual(name, actualName.text)
        self.assertEqual(msg, actualMsg.text)

    def test_format_to_json(self):
        name = "Kasia"
        msg = "How are you?"
        actual = json.loads(format_to_json(msg, name))
        self.assertEqual(name, actual['imie'])
        self.assertEqual(msg, actual['msg'])

    def test_plain_text(self):
        name = "Basia"
        msg = "Hi"
        result = plain_text(msg, name)
        self.assertEqual(name, result.split(" ")[0])
        self.assertEqual(msg, result.split(" ")[1])
