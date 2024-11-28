[deepracer-core](https://github.com/aws-deepracer-community/deepracer-core?tab=readme-ov-file)
[deepracer-for-cloud](https://aws-deepracer-community.github.io/deepracer-for-cloud/)


# Main Components
The primary components of DeepRacer are four docker containers:
- Robomaker Container: 
  Responsible for the robotics environment. 
  Based on ROS + Gazebo as well as the AWS provided "Bundle".
  AWS-Robomaker provides a virtual environment. It creates a 3d-world with one of a couple of virtual race tracks and a car to race through it.
  
  
- Sagemaker Container: 
  Responsible for training the neural network.
  AWS-Sagemaker provides an environment for training the car. The design of the neuronal network is provided. The input is the image received from a camera mounted on the car. The output is an action. One can choose which actions to use. For instance one might want two speeds, say 1 m/s and 2 m/s. Then one can choose for instance 5 steering angles that the car shall be able to steer to. In this example there would be a total of 2*5 = 10 possible actions available, each represented by an output neuron. The command associated with the neuron that receives the strongest input will be chosen to drive the car.
  A 3 layer convolutional neuronal network is used, followed by a couple of fully connected layers. The algorithm to learn the weights is a proximal policy optimization algorithm.

- Reinforcement Learning (RL) Coach: 
  Responsible for preparing and starting the Sagemaker environment.

- Log-Analysis: 
  Providing a containerized Jupyter Notebook for analyzing the logfiles generated. Uses Deepracer Utils.
