import pytest

from tools.accum import Accumulator


@pytest.fixture
def accum(scope='function'):
    yield Accumulator()
    print("DONE with the test")

@pytest.fixture
def accum2():
    return Accumulator()