"""What is faster, to repeat it 500 times
or to stackoverflow it 500 times?

'La letra con sangre entra'
"""

from typing import Dict
import operator


def dict_key_from_max_value(d: Dict) -> str:
    """retrieve the key from a 
    dictionary whose value is maximum"""
    return max(d.items(), key=operator.itemgetter(1))[0]
