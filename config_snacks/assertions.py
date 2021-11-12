def assert_none(v):
    if v is None:
        raise AssertionError(f"Value is None")

def assert_type(v, *types, allow_none=False):
    if not allow_none:
        assert_none(v)
    if not any(isinstance(v, t) for t in types):
        raise AssertionError(f"Value is not of any type: {types}")

def assert_numeric(v, allow_none=False):
    if not allow_none:
        assert_none(v)
    assert_type(v, int, float, complex)

def assert_str(v, allow_none=False):
    if not allow_none:
        assert_none(v)
    assert_type(v, str)
