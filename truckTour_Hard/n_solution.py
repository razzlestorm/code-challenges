def truckTour(petrolpumps):
  tank = 0
  # two pointers, start position == head, current position == tail
  start = 0
  current = 0

  while start < len(petrolpumps):
  # move our current pointer through each gas station
    # at each station we want to fill up on gas, put it in our tank
    tank += petrolpumps[current][0]
    # subtract however much it would take to get to the next station
    tank -= petrolpumps[current][1]

    # if we can make it to the next station
    if tank >= 0:
      # move current + 1
      current = (current + 1) % len(petrolpumps)
      # if our head and our tail are at the same point, then we've made it all the way around
      # return it}
      if current == start:
        return start
    # if we can't
    else:
      # move start + 1 and current to start
      start = current + 1
      current = start
      # reset our gas tank = 0
      tank = 0
