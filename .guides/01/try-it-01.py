import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from problem01 import maxProfit

print(maxProfit([1, 3, 2, 8, 4, 9], 2)) 