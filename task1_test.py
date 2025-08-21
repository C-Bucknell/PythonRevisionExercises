import os.path
import sys
from task1 import main
from tud_tests import *

def test_task1():
    try:
        exists = os.path.exists("task1.py")
        assert exist == True
    except:
        sys.exit()

    set_keyboard_input(["Bob"])
    
    assert hello.hello_world() == "Hello World!"
