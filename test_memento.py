"""
- What you gonna do?
- My job

(Kung Fury)
"""

from memento import dict_key_from_max_value


def test_dict_key_from_max_value():
    # this is a fixture
    d_fixture = {
        'x': 1,
        'y': 2,
    }
    assert dict_key_from_max_value(d=d_fixture) == 'y'


test_dict_key_from_max_value()
