

def assert_type(v, *types):
    if not any(isinstance(v, t) for t in types):
        raise AssertionError(f"Value is not of any type: {types}")

def assert_none(v):
    if v is None:
        raise AssertionError(f"Value is None")

def assert_numeric(v):
    assert_none(v)
    assert_type(v, int, float, complex)

def assert_str(v):
    assert_none(v)
    assert_type(v, str)
