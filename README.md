# entrance secretary
[![Build Status](https://travis-ci.org/mqcmd196/entrance_secretary.svg?branch=master)](https://travis-ci.org/mqcmd196/entrance_secretary)

## What is this?

## To use on Raspberry pi 4
To use the entrance secretary, you need to install ROS Melodic. But ROS Melodic for Raspbian buster and Ubuntu 19.xx has not been released yet(1/12/2019), you must install Ubuntu 18.04 at first. (I sufferred...)

If you use Raspberry pi 3, Raspbian stretch and Ubuntu Mate 18.04 are available officially. But there are no USB3.0 ports and I can't assure you of working it on raspi3.

### 1. Install Ubuntu 18.04 on Raspberry pi 4

### 2. Install ROS Melodic


### X. Install tensorflow lite
There are no tensorflow lite apt-packages for python3.6 & arm64, so you need to build tf-lite yourself.  

```bash
sudo apt install swig libjpeg-dev zlib1g-dev python3-dev python3-numpy
sh tensorflow/lite/tools/pip_package/build_pip_package.sh
```

[show more details](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/tools/pip_package)

