"""Test morse decoder"""
import os
import sys
import pytest


currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import morse


@pytest.mark.parametrize('message', [
    'I WORK ALL NIGHT I WORK ALL DAY',
    'TO PAY THE BILLS I HAVE TO PAY',
    'AINT IT SAD?'
])
def test_identity(message: str) -> None:
    """ Test identity property of the morse encoder"""
    assert morse.decode(morse.encode(message)) == ''.join(message.split())


@pytest.mark.parametrize('morse_str, eng_str', [
    ('.-.-.- ..--.. -....- -....- ..--.. .-.-.-', '.?--?.'),
    ('--. - ---.. --... ..--- ...--', 'GT8723'),
    ('.--. --- --. -.-. .... .- -- .--.', 'POGCHAMP')
])
def test_decode(morse_str: str, eng_str: str) -> None:
    """ Test morse decoding"""
    assert morse.decode(morse_str) == eng_str
