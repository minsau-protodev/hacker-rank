def birthdayCakeCandles(candles):
    # Write your code here
    highest = max(candles)
    highest_candles = list(filter(lambda x: (x == highest), candles))
    
    return len(highest_candles)

result = birthdayCakeCandles([3, 2, 1, 3])
print(result)