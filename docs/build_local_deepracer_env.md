[deepracer-core](https://github.com/aws-deepracer-community/deepracer-core?tab=readme-ov-file)
[deepracer-for-cloud](https://aws-deepracer-community.github.io/deepracer-for-cloud/)

# Main Components
The primary components of DeepRacer are four docker containers:
- Robomaker Container: Responsible for the robotics environment. Based on ROS + Gazebo as well as the AWS provided "Bundle". Uses components of AWS Robomaker
- Sagemaker Container: Responsible for training the neural network. Uses components of AWS Sagemaker
- Reinforcement Learning (RL) Coach: Responsible for preparing and starting the Sagemaker environment.
- Log-Analysis: Providing a containerized Jupyter Notebook for analyzing the logfiles generated. Uses Deepracer Utils.
