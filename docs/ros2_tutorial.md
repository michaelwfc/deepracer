# ROS 2

[ROS 2 Tutorials](https://docs.ros.org/en/foxy/Tutorials.html)
[动手学 ROS2-FROXY](https://fishros.com/d2lros2foxy/#/)
- install Ubuntu Linux - Focal Fossa (20.04)

# Env on windows11 for ROS 2 Jazzy Jalisco

 
- install VMware Workstation Pro-17.6.1 个人免费版下载 from Brodcom
- install Ubuntu Linux - Noble (24.04) 64-bit

## install ROS2
### Set locale
```bash
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings
```

### Setup Sources
You will need to add the ROS 2 apt repository to your system.


```bash
# First ensure that the Ubuntu Universe repository is enabled.
sudo apt install software-properties-common
sudo add-apt-repository universe


# Now add the ROS 2 GPG key with apt.
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

# network error:
# 小鱼最新一行代码安装ROS2：
wget http://fishros.com/install -O fishros && bash fishros



# Then add the repository to your sources list.
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

```

## Dev Env
```bash
sudo apt install git
# download vscode.deb version from https://code.visualstudio.com/docs/?dv=linux64_deb
sudo dpkg -i code.deb
```