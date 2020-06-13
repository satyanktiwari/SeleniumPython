import pytest
import sys

@pytest.mark.skip(reason='not included in build')
def test_demo_1():
    assert True
@pytest.mark.skipif(sys.version_info > (3,6),
                    reason="skip if python is higher than 3.6" )
def test_demo_2():
    assert True

def test_demo_3():
    assert True
# name
@pytest.mark.windows
def test_UiFlowWindows1():
    assert True

@pytest.mark.windows
def test_UiFlowWindows2():
    assert True

@pytest.mark.linux
def test_UiFlowLinux1():
    assert True

@pytest.mark.linux
def test_UiFlowLinux2():
    assert True

@pytest.mark.mac
def test_UiFlowmac():
    assert True
# pytest test_demo_skip.py -v -rxs
# pytest test_demo_skip.py -v -rxs -k demo_3
# use skipif to skip only if a given condition is met
# pytest test_demo_skip.py -m mac -v