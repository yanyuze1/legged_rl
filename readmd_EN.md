<h1 align="center">legged_rl</h1>

<p align="center">
  <img src="https://www.unitree.com/images/1c36f0b03cfd445fbcad12b4b1eb3a29_3840x3266.jpg?x-oss-process=image%2Fformat%2Cwebp" alt="Unitree Go2" width="720">
</p>

<p align="center">
  <a href="readme.md">中文</a> | <a href="readmd_EN.md">English</a>
</p>

This is a quadruped robot reinforcement learning project based on Isaac Sim. It uses [rl_sar](https://github.com/fan-ziqi/rl_sar) for sim2sim testing and real-robot deployment testing. At the current stage, it uses the quadruped robot MDP and reward functions from [robot_lab](https://github.com/fan-ziqi/robot_lab) to train and run play tests for Unitree Go2. For the himloco-mode implementation, see the branch overview.

# Branch Overview
- [main](https://github.com/yanyuze1/legged_rl/tree/main): Default branch, with stable support for deploying rl_sar with robot_lab.
- [dev](https://github.com/yanyuze1/legged_rl/tree/dev): Testing branch for development versions, currently with unstable support for deploying rl_sar in himloco mode.

# Project Structure
![alt text](images/image.png)

# Quick Start
## Project Environment
- Create a conda environment
```bash
conda create -n legged_rl python=3.11
conda activate legged_rl
```
- Install torch
```bash
python -m pip install -U torch==2.7.0 torchvision==0.22.0 --index-url https://download.pytorch.org/whl/cu128
```
- Install isaacsim and isaaclab
```bash
python -m pip install isaaclab[isaacsim,all]==2.3.0 --extra-index-url https://pypi.nvidia.com
```
- Install the legged_rl project
```bash
git clone https://github.com/yanyuze1/legged_rl.git
cd legged_rl
python -m pip install -e source/legged_rl
```

- Install wandb, rsl_rl, and cusrl
```bash
python -m pip install wandb
cd legged_rl/source/legged_rl/rsl_rl
python -m pip install -e .
python -m pip install cusrl[all]
```

## Project Usage
### List All Available Tasks
```bash
cd legged_rl
python scripts/list_envs.py
```

### Training

- Flat terrain training
```bash
python scripts/rsl_rl/train.py \
  --task=LeggedRL-Isaac-Velocity-Flat-Unitree-Go2-v0 \
  --num_envs 4096 \
  --headless
python scripts/cusrl/train.py \
  --task=LeggedRL-Isaac-Velocity-Flat-Unitree-Go2-v0 \
  --num_envs 4096 \
  --headless
```
- Rough terrain training
```bash
python scripts/rsl_rl/train.py \
  --task=LeggedRL-Isaac-Velocity-Rough-Unitree-Go2-v0 \
  --num_envs 4096 \
  --headless
python scripts/cusrl/train.py \
  --task=LeggedRL-Isaac-Velocity-Rough-Unitree-Go2-v0 \
  --num_envs 4096 \
  --headless
```
- Resume training
```bash
python scripts/rsl_rl/train.py \
  --task=LeggedRL-Isaac-Velocity-Flat-Unitree-Go2-v0 \
  --num_envs 4096 \
  --headless \
  --resume \
  --load_run 2026-06-19_20-38-06 \
  --checkpoint model_100.pt
python scripts/cusrl/train.py \
  --task=LeggedRL-Isaac-Velocity-Flat-Unitree-Go2-v0 \
  --num_envs 4096 \
  --headless \
  --resume \
  --load_run 2026-06-19_20-38-06 \
  --checkpoint model_100.pt
```

### Play
- Flat terrain play
```bash
python scripts/rsl_rl/play.py \
    --task=LeggedRL-Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 16
python scripts/cusrl/play.py \
    --task=LeggedRL-Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 16
```
![alt text](images/converted.gif)
- Rough terrain play
```bash
python scripts/rsl_rl/play.py \
    --task=LeggedRL-Isaac-Velocity-Rough-Unitree-Go2-v0 \
    --num_envs 16
python scripts/cusrl/play.py \
    --task=LeggedRL-Isaac-Velocity-Rough-Unitree-Go2-v0 \
    --num_envs 16
```

![alt text](images/converted1.gif)

## sim2sim and Real-Robot Deployment
- Real-robot deployment in this project supports using [rl_sar](https://github.com/fan-ziqi/rl_sar) for sim2sim testing and real-robot deployment testing.
- Regarding branch versions, the [main](https://github.com/yanyuze1/legged_rl/tree/main) branch supports deployment in robot_lab mode. The [dev](https://github.com/yanyuze1/legged_rl/tree/dev) branch supports deployment in himloco mode as a testing and development version.

# Reinforcement Learning Framework
## RSL_RL
![alt text](images/image1.png)

For detailed learning about rsl_rl, see [Eryingzhang's video](https://www.bilibili.com/video/BV1KJdgB1EuA/?spm_id_from=333.1391.0.0&vd_source=d2c056c41b6dadc7b66b4f6b51f235fc).

# Acknowledgements
- [robot_lab](https://github.com/fan-ziqi/robot_lab)
- [legged_lab](https://github.com/zhw0422/legged_lab)
- [RSL_RL](https://github.com/leggedrobotics/rsl_rl)
- [CUSRL](https://github.com/chengruiz/cusrl)
