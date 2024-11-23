# Place import statement outside of function (supported libraries: math, random, numpy, scipy, and shapely)
# Example imports of available libraries
#
# import math
# import random
# import numpy
# import scipy
# import shapely

import math


def reward_function(params):
  #  on_track, x, y, distance_from_center, car_orientation, progress, steps,
  #                   throttle, steering, track_width, waypoints, closest_waypoints
      # Read input variables
    x = params['x']
    y = params['y']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    speed= params['speed']
    
    reward = 1e-3
    
    rabbit = [0,0]
    pointing = [0,0]
        
    # Reward when yaw (car_orientation) is pointed to the next waypoint IN FRONT.
    
    # Find nearest waypoint coordinates
    
    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    # prev_point = waypoints[closest_waypoints[0]]

    rabbit = next_point
    
    radius = math.hypot(x - rabbit[0], y - rabbit[1])
    
    pointing[0] = x + (radius * math.cos(math.radians(heading)))
    pointing[1] = y + (radius * math.sin(math.radians(heading)))
    
    vector_delta = math.hypot(pointing[0] - rabbit[0], pointing[1] - rabbit[1])
    
    # Max distance for pointing away will be the radius * 2
    # Min distance means we are pointing directly at the next waypoint
    # We can setup a reward that is a ratio to this max.
    
    if vector_delta == 0:
        reward += 1
    else:
        reward += ( 1 - ( vector_delta / (radius * 2)))

    # Reduce reward if car is driving too slow
    if speed < 1.0:
        reward = reward * 0.8
    

    return reward