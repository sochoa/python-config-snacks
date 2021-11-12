from unittest import TestCase

import snacks.assertions

class TestAssertions(TestCase):
    def test_assert_type(self):
        expected_assertion_exceptions = {
            r"Value is None": lambda: snacks.assertions.assert_none(None),
            r"Value is not of any type: \(<class 'int'>, <class 'float'>, <class 'complex'>\)": lambda: snacks.assertions.assert_numeric("foo"),
            r"Value is not of any type: \(<class 'str'>,\)": lambda: snacks.assertions.assert_str(1),
        }
        for pattern, _callable in expected_assertion_exceptions.items():
            self.assertRaisesRegex(AssertionError, pattern, _callable)
            
        expected_no_assertions = [
            lambda: snacks.assertions.assert_none(True),
            lambda: snacks.assertions.assert_numeric(1),
            lambda: snacks.assertions.assert_numeric(complex(2, 3)),
            lambda: snacks.assertions.assert_str("foo"),
        ]
        for _callable in expected_no_assertions:
            _callable()
