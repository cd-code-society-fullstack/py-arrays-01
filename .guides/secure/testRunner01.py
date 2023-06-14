import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from problem01 import maxProfit

prices = list(map(int, sys.argv[1].split(',')))
fee = int(sys.argv[2])

print(maxProfit(prices, fee))