import pickle

from nose.tools import eq_

from .. import mappers
from ....dependencies import solve
from ...datasource import Datasource

tokens = Datasource("tokens")
my_ints = Datasource("my_ints")


def extract_first_char(token):
    return token[:1]


first_char = mappers.map(extract_first_char, tokens, name="first_char")

lower_case_tokens = mappers.lower_case(tokens, name="lower_case_tokens")

derepeat_tokens = mappers.derepeat(tokens, name="derepeat_tokens")

de1337_tokens = mappers.de1337(tokens, name="de1337_tokens")

abs_ints = mappers.abs(my_ints)


def test_item_mapper():
    cache = {tokens: ["alpha", "bravo", "charlie", "delta"]}
    eq_(solve(first_char, cache=cache),
        ["a", "b", "c", "d"])

    eq_(pickle.loads(pickle.dumps(first_char)), first_char)


def test_lower_case():
    cache = {tokens: ["foo", "Bar", "FOO"]}
    eq_(solve(lower_case_tokens, cache=cache),
        ["foo", "bar", "foo"])

    eq_(pickle.loads(pickle.dumps(lower_case_tokens)), lower_case_tokens)


def test_derepeat():
    cache = {tokens: ["foo", "Bar", "FOO"]}
    eq_(solve(derepeat_tokens, cache=cache),
        ["fo", "Bar", "FO"])

    eq_(pickle.loads(pickle.dumps(derepeat_tokens)), derepeat_tokens)


def test_de1337():
    cache = {tokens: ["1337", "W4ff1e"]}
    eq_(solve(de1337_tokens, cache=cache),
        ["leet", "Waffle"])

    eq_(pickle.loads(pickle.dumps(de1337_tokens)), de1337_tokens)


def test_abs():
    cache = {my_ints: [1, 0, -1]}
    eq_(solve(abs_ints, cache=cache),
        [1, 0, 1])

    eq_(pickle.loads(pickle.dumps(abs_ints)), abs_ints)
