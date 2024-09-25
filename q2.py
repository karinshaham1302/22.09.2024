import statistics

# start

heights: list[float] = []
counter: int = 0
SENTINEL: int = 999
while True:
    height = float(input('enter player height:'))
    if height == 999:
        break
    if not 1.60 <= height <= 3.0:
        continue
    heights.append(height)
    if height > 2.0:
        counter += 1
        print('player than taller from 2.0')
if max(heights) is None or statistics.mean(heights) > max(heights):
    max_heights = statistics.mean(heights)
    max_heights += heights
    print('the highest player')

if len(heights) > 0:
    print(f'the len heights is:', {len(heights)})
    print(f'max height is:', {max(heights)})
    print(f'min height is:', {min(heights)})
    print(f'average is:', {statistics.mean(heights)})

# stop
