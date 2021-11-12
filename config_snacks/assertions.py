import os.path


def assert_none(v):
    if v is None:
        raise AssertionError(f"Value is None")

def assert_type(v, *types):
    assert_none(v)
    if not any(isinstance(v, t) for t in types):
        raise AssertionError(f"Value is not of any type: {types}")

def assert_numeric(v):
    assert_none(v)
    assert_type(v, int, float, complex)

def assert_uint(v):
    assert_none(v)
    assert_type(v, int)
    if v < 0:
        raise AssertionError(f"Value is not an unsigned int: {v}")

def assert_str(v, allow_none=False):
    assert_none(v)
    assert_type(v, str)

def assert_path_exists(v):
    assert_none(v)
    if not os.path.exists(v):
        raise AssertionError(f"Path does not exist: {v}")

def assert_file_exists(v):
    assert_path_exists(v)
    if not os.path.isfile(v):
        raise AssertionError(f"Is not a file: {v}")

def assert_dir_exists(v):
    assert_path_exists(v)
    if not os.path.isdir(v):
        raise AssertionError(f"Is not a dir: {v}")

def assert_link_exists(v):
    assert_path_exists(v)
    if not os.path.islink(v):
        raise AssertionError(f"Is not a symlink: {v}")
