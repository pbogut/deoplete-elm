import unittest
from unittest.mock import Mock
import sys

sys.path.insert(0, './rplugin/python3/deoplete')
sys.modules['sources.base'] = __import__('mock_base')

from sources import deoplete_elm  # noqa


class SourceTest(unittest.TestCase):

    def setUp(self):
        self.source = deoplete_elm.Source(Mock())

    def test_get_complete_position_for_module_function_call(self):
        position = self.source.get_complete_position(
            {'input': '       Html.d'})
        # deoplete    '0....5.^ <- 7
        self.assertEqual(position, 7)

    def test_get_complete_query_for_module_function_call(self):
        query = self.source.get_complete_query(
            {'input': '  Basic.'})
        self.assertEqual(query, 'Basic.')

    def test_get_complete_position_for_function_call(self):
        position = self.source.get_complete_position(
            {'input': '  di'})
        # deoplete    '0.^ <- 2
        self.assertEqual(position, 2)

    def test_get_complete_query_for_function_call(self):
        query = self.source.get_complete_query(
            {'input': '  cla'})
        self.assertEqual(query, 'cla')

    def test_get_complete_query_for_non_alpha_characters(self):
        query = self.source.get_complete_query(
            {'input': '  |'})
        self.assertEqual(query, '|')

        query = self.source.get_complete_query(
            {'input': '  ::'})
        self.assertEqual(query, '::')
