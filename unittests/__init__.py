import unittests
import getopt
import sys
import os

## parse inputs
try:
    optlist, args = getopt.getopt(sys.argv[1:],'v')
except getopt.GetoptError:
    print(getopt.GetoptError)
    print(sys.argv[0] + "-v")
    print("... the verbose flag (-v) may be used")
    sys.exit()

VERBOSE = False
RUNALL = False

sys.path.append(os.path.realpath(os.path.dirname(__file__)))

for o, a in optlist:
    if o == '-v':
        VERBOSE = True

## api tests
from ApiTests import *
ApiTestSuite = unittests.TestLoader().loadTestsFromTestCase(ApiTest)

## model tests
from ModelTests import *
ModelTestSuite = unittests.TestLoader().loadTestsFromTestCase(ModelTest)

## logger tests
from LoggerTests import *
LoggerTestSuite = unittests.TestLoader().loadTestsFromTestCase(LoggerTest)

MainSuite = unittests.TestSuite([ApiTestSuite, ModelTestSuite, LoggerTestSuite])
