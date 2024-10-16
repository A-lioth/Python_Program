
# * 1
import test_package.test_module_1
import test_package.test_module_2

# * 2
from test_package import *

def test_1():
    test_package.test_module_1.test_func()
    test_package.test_module_2.test_func()
    
def test_2():
    test_module_1.test_func()
    test_module_2.test_func()
    
def main():
    test_1()
    test_2()
    
main()
