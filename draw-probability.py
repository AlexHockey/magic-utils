import argparse
import math

def ncr(n, r):
    assert n > r
    high_denominator = max(r, n-r)
    low_denominator = min(r, n-r)

    result = 1
    for x in xrange(high_denominator+1, n+1):
        result = result * x
    result = result / math.factorial(low_denominator)

    return result

parser = argparse.ArgumentParser(description="Calculate the probability of drawing a certain number of types of card")
parser.add_argument('--deck', type=int, default=60)
parser.add_argument('--draw', type=int)
parser.add_argument('--pool', type=int)
parser.add_argument('--needed', type=int)
args = parser.parse_args()


# Work out how many ways there are to draw `draw` cards from the deck
num_draws = ncr(args.deck, args.draw)

# How many ways
num_misses = 0
for x in xrange(args.needed):
    num_misses += ncr(args.deck - args.pool, args.draw - x) * ncr(args.pool, x)

print 1.0 - 1.0 * num_misses / num_draws


