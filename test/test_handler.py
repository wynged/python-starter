import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from handler import handler
import base64
import json

class TestHandler(unittest.TestCase):

    def test_raises_exception_with_bad_arguments(self):
        with self.assertRaises(Exception):
            handler.box(length=0, width=0, height=0)

    def test_creates_box_with_valid_arguments(self):
        result = handler.box(1, 1, 1)
        self.assertIsNotNone(result['model'])
        self.assertIsNotNone(result['computed'])
        for key,value in result['computed'].items():
            print('Checking item {} for correct volume...'.format(key))
            if value.get('volume') is not None:
                self.assertEqual(value['volume'], 1)
    
    def test_model_creation(self):
        result = handler.box(1,1,1)

        with open("testModel.glb", "wb") as fh:
            fh.write(base64.b64decode(result['model']))