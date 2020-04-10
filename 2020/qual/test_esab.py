import pytest
import os
import interactive_runner


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


@pytest.mark.parametrize("test_n", [0, 1, 2])
def test_example(test_n):
    judge_args = ['python', os.path.join(SCRIPT_DIR, 'local_testing_tool.py'), str(test_n)]
    sol_args = ['python', os.path.join(SCRIPT_DIR, 'esab.py')]
    judge_code, sol_code = interactive_runner.run(judge_args, sol_args)
    assert judge_code == 0 and sol_code == 0
