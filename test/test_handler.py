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
    
    # This test saves the model to a .glb file for local testing
    # with the gltf viewer.
    def test_save_glb(self):
        result = handler.box(1,1,1)
        with open("testModel.glb", "wb") as fh:
            fh.write(base64.b64decode(result['model']))
    
    # This test saves a .gltf file and an associated .bin file
    # for local testing. 
    def test_save_gltf(self):
        result = handler.create_box(1,1,1)
        result[1].save('test.gltf')

    # https://github.com/hypar-io/python-starter/issues/2 
    def test_save_glb_save_gltf(self):
        result = handler.create_box(1,1,1)
        result[1].save_glb('resave_test.glb')
        result[1].save('resave_test.gltf')