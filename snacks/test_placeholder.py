import unittest

import snacks.source.placeholder

class TestEnvSource(unittest.TestCase):
    def test_happy_path(self):
        mocked_env = {
            "a": "foo",
            "b": "bar",
            "c": "monkey",
        }
        expected_env = {
            '${B}': 'bar',
            '${b}': 'bar',
            '${C}': 'monkey',
            '${c}': 'monkey',
        }
        actual_env = snacks.source.placeholder.parse(mocked_env, whitelist_patterns=["^[bc]$"])
        self.assertEqual(expected_env, actual_env)

    def test_render(self):
        mocked_env = {
            "a": "foo",
            "b": "bar",
            "c": "monkey",
        }
        env = snacks.source.placeholder.parse(mocked_env, whitelist_patterns=["^[bc]$"])

        sample_config = {
            "h": "${a}/the/quick/fox",
            "i": "/jumps/over/the/${b}",
            "j": "lazy/${c}/dog",
        }
        expected_rendered_config = {
            'h': '${a}/the/quick/fox',
            'i': '/jumps/over/the/bar',
            'j': 'lazy/monkey/dog'
        }
        actual_rendered_config = snacks.source.placeholder.render(sample_config, env)
        self.assertEqual(expected_rendered_config, actual_rendered_config)

    def test_render_no_whitelist(self):
        mocked_env = {
            "a": "foo",
            "b": "bar",
            "c": "monkey",
        }
        env = snacks.source.placeholder.parse(mocked_env)

        sample_config = {
            "h": "${a}/the/quick/fox",
            "i": "/jumps/over/the/${b}",
            "j": "lazy/${c}/dog",
        }
        expected_rendered_config = {
            'h': 'foo/the/quick/fox',
            'i': '/jumps/over/the/bar',
            'j': 'lazy/monkey/dog',
        }
        actual_rendered_config = snacks.source.placeholder.render(sample_config, env)
        self.assertEqual(expected_rendered_config, actual_rendered_config)
