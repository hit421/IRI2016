#!/usr/bin/env python
from pathlib import Path
import subprocess
import pytest

R = Path(__file__).parent


def test_matlab_api():
    try:
        subprocess.check_call(['matlab', '-nojvm', '-r',
                               'r=runtests(); exit(any([r.Failed]))'],
                              cwd=R, timeout=60)
    except FileNotFoundError as e:
        pytest.skip(f'Matlab not available  {e}')


def test_octave_api():
    try:
        subprocess.check_call(['octave', '-q', '--eval="exit(test_iri2016)"'],
                              cwd=R, timeout=60)
    except FileNotFoundError as e:
        pytest.skip(f'GNU Octave not available  {e}')


if __name__ == '__main__':
    pytest.main(['-xrsv', __file__])
