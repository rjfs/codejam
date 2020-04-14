import pytest
import re
import pattern


@pytest.mark.parametrize(
    ("patterns", "is_possible"), [
        (("*CONUTS", "*COCONUTS", "*OCONUTS", "*CONUTS", "*S"), True),
        (("*XZ", "*XYZ"), False),
        (("H*O", "HELLO*", "*HELLO", "HE*"), True),
        (("CO*DE", "J*AM"), False),
        (("CODE*", "*JAM"), True),
        (("A*C*E", "*B*D*"), True),
        (("A*C*E", "*B*D*", "ABDCE*"), True),
        (("**Q**", "*A*"), True),
    ]
)
def test_solve(patterns, is_possible):
    result = pattern.solve(patterns, n=len(patterns))
    print("Result: %s" % result)
    if is_possible:
        for p in patterns:
            pat = re.compile(p.replace("*", ".*"))
            assert pat.match(result)
    else:
        assert result == "*"
