import pytest
import randomized
import random


def test_sample():
    with open("sample.in.txt", "r") as f:
        lines = f.read().splitlines()

    u = lines[1]
    requests = [i.split() for i in lines[2:]]

    assert randomized.solve(u, requests) == "TPFOXLUSHB"


@pytest.mark.parametrize("code", ["CODEJAMFUN", "ABCDEFGHIJ", "ASDFGHJKLZ", "QWERTYUIOP"])
def test_generated(code):
    assert len(code) == len(set(code)) == 10
    u = 2
    assert randomized.solve(u, generate(code, u)) == code


@pytest.mark.parametrize("code", ["CODEJAMFUN", "ABCDEFGHIJ", "ASDFGHJKLZ", "QWERTYUIOP"])
def test_set3(code):
    assert len(code) == len(set(code)) == 10
    u = 16
    assert randomized.solve(u, generate(code, u, number_known=False)) == code


def generate(code, u, n_req=10**4, number_known=True):
    """ Generates requests ans answers for given code and u """
    req = []
    lower = 1
    upper = 10 ** u - 1
    for _ in range(n_req):
        m = str(random.randint(lower, upper))
        q = m if number_known else "-1"
        req.append([q, get_reply(m, code)])

    return req


def get_reply(n, code):
    n = str(random.randint(1, int(n)))
    return "".join([code[int(_n)] for _n in n])
