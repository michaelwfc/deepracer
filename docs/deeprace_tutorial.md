[crash course on Reinforcement Learning](https://us-east-1.console.aws.amazon.com/deepracer/home?region=us-east-1#getStarted)

# How does AWS DeepRacer learn to drive itself?
- Agent
The agent simulates the AWS DeepRacer vehicle in the simulation for training. More specifically, it embodies the neural network that controls the vehicle, taking inputs and deciding actions.

- Environment
The environment contains a track that defines where the agent can go and what state it can be in. The agent explores the environment to collect data to train the underlying neural network.

- State
A state represents a snapshot of the environment the agent is in at a point in time.

For AWS DeepRacer, a state is an image captured by the front-facing camera on the vehicle.

- Action
An action is a move made by the agent in the current state. For AWS DeepRacer, an action corresponds to a move at a particular speed and steering angle.

- Reward
The reward is the score given as feedback to the agent when it takes an action in a given state.

In training the AWS DeepRacer model, the reward is returned by a reward function. In general, you define or supply a reward function to specify what is desirable or undesirable action for the agent to take in a given state.

# How to train a reinforcement learning model?


# [Parameters of reward functions](https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-console-train-evaluate-models.html#deepracer-reward-function-signature)

Reward function parameters for AWS DeepRacer
In AWS DeepRacer, the reward function is a Python function which is given certain parameters that describe the current state and returns a numeric reward value.

The parameters passed to the reward function describe various aspects of the state of the vehicle, such as its position and orientation on the track, its observed speed, steering angle and more.

We will explore some of these parameters and how they describe the vehicle as it drives around the track:

- Position on track
- Heading
- Waypoints  
The waypoints parameter is an ordered list of milestones placed along the track center.
Each waypoint in waypoints is a pair [x, y] of coordinates in meters, measured in the same coordinate system as the car's position.

- Track width
- Distance from center line
- All wheels on track
- Speed
- Steering angle


# Reward function

## 1. Stay On Track 
In this example, we give a high reward for when the car stays on the track, and penalize if the car deviates from the track boundaries.

This example uses the all_wheels_on_track, distance_from_center and track_width parameters to determine whether the car is on the track, and give a high reward if so.

Since this function doesn't reward any specific kind of behavior besides staying on the track, an agent trained with this function may take a longer time to converge to any particular behavior.


```python
def reward_function(params):
    '''
    Example of rewarding the agent to stay inside the two borders of the track
    '''

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = 1.0

    # Always return a float value
    return float(reward)
```


## 2. Follow Center Line
In this example we measure how far away the car is from the center of the track, and give a higher reward if the car is close to the center line.

This example uses the track_width and distance_from_center parameters, and returns a decreasing reward the further the car is from the center of the track.

This example is more specific about what kind of driving behavior to reward, so an agent trained with this function is likely to learn to follow the track very well. However, it is unlikely to learn any other behavior such as accelerating or braking for corners.


```python
def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    return float(reward)

```

## 3. Prevent zig-zag
This example incentivizes the agent to follow the center line but penalizes with lower reward if it steers too much, which will help prevent zig-zag behavior.

The agent will learn to drive smoothly in the simulator and likely display the same behavior when deployed in the physical vehicle.


```python
def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''
    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle
    # Calculate 3 marks that are farther and father away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15 
    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8
    return float(reward)
    
```
