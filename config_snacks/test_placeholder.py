import unittest

from fs import open_fs

import config_snacks.placeholder

class TestEnvSource(unittest.TestCase):
    def test_parse(self):
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
        actual_env = config_snacks.placeholder.parse(mocked_env, whitelist_patterns=["^[bc]$"])
        self.assertEqual(expected_env, actual_env)

    def test_render(self):
        mocked_env = {
            "a": "foo",
            "b": "bar",
            "c": "monkey",
        }
        env = config_snacks.placeholder.parse(mocked_env, whitelist_patterns=["^[bc]$"])

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
        actual_rendered_config = config_snacks.placeholder.render(sample_config, env)
        self.assertEqual(expected_rendered_config, actual_rendered_config)

    def test_render_no_whitelist(self):
        mocked_env = {
            "a": "foo",
            "b": "bar",
            "c": "monkey",
        }
        env = config_snacks.placeholder.parse(mocked_env)

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
        actual_rendered_config = config_snacks.placeholder.render(sample_config, env)
        self.assertEqual(expected_rendered_config, actual_rendered_config)

    def test_file_placeholders(self):
        memfs = open_fs('mem://')
        memfs.makedir("/etc", permissions=0o0755)
        memfs.writetext("/etc/region", "us-ashburn-1")
        placeholders = config_snacks.placeholder.get_file_placeholders(memfs, "/etc/region")
        expected_placeholders = {'${REGION}': 'us-ashburn-1', '${region}': 'us-ashburn-1'}
        self.assertEqual(expected_placeholders, placeholders)

