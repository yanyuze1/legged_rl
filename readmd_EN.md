<h1 align="center">legged_rl</h1>

<p align="center">
  <a href="readme.md">中文</a> | <a href="readmd_EN.md">English</a>
</p>

This project supports reinforcement learning training on RTX 50 series and older Nvidia GPUs. It is also intended to serve as a foundational reinforcement learning repository for quadruped and humanoid robots. Currently, only Unitree Go2 is supported, with support for more robots and algorithms to be added gradually.

# Branch Overview
- [main](https://github.com/yanyuze1/legged_rl/tree/main): Default branch, with stable support for rl_sar deployment.
- [dev](https://github.com/yanyuze1/legged_rl/tree/dev): Testing branch for development versions. Currently provides unstable support for rl_sar deployment.

# Quick Start
## Project Environment
- Create a conda environment
```bash
conda create -n legged_rl python=3.11
conda activate legged_rl
```
- Install torch
```bash
pip install -U torch==2.7.0 torchvision==0.22.0 --index-url https://download.pytorch.org/whl/cu128
```
- Install isaacsim and isaaclab
```bash
pip install isaaclab[isaacsim,all]==2.3.0 --extra-index-url https://pypi.nvidia.com
```
- Install wandb, rsl_rl, and cusrl
```bash
python -m pip install wandb
git clone https://github.com/leggedrobotics/rsl_rl
cd rsl_rl
python -m pip install -e .
python -m pip install cusrl[all]
```
- Install the legged_rl project
```bash
git clone https://github.com/yanyuze1/legged_rl.git
cd legged_rl
python -m pip install -e source/legged_rl
```

## Project Usage
### List All Available Environments
```bash
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
# Resume training
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
# Resume training
python scripts/rsl_rl/train.py \
  --task=LeggedRL-Isaac-Velocity-Rough-Unitree-Go2-v0 \
  --num_envs 4096 \
  --headless \
  --resume \
  --load_run 2026-06-19_20-38-06 \
  --checkpoint model_100.pt
python scripts/cusrl/train.py \
  --task=LeggedRL-Isaac-Velocity-Rough-Unitree-Go2-v0 \
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

- Rough terrain play
```bash
python scripts/rsl_rl/play.py \
    --task=LeggedRL-Isaac-Velocity-Rough-Unitree-Go2-v0 \
    --num_envs 16
python scripts/cusrl/play.py \
    --task=LeggedRL-Isaac-Velocity-Rough-Unitree-Go2-v0 \
    --num_envs 16
```

## sim2sim and Real-Robot Deployment
- Real-robot deployment in this project supports using [rl_sar](https://github.com/fan-ziqi/rl_sar) for sim2sim testing and real-robot deployment testing.
- Regarding branch versions, the [main](https://github.com/yanyuze1/legged_rl/tree/main) branch supports deployment in robot_lab mode.The [dev](https://github.com/yanyuze1/legged_rl/tree/dev) branch supports deployment in himloco mode, although the current results are not well.

# Acknowledgements
- [robot_lab](https://github.com/fan-ziqi/robot_lab)
- [legged_lab](https://github.com/zhw0422/legged_lab)
