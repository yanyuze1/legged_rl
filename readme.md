<h1 align="center">legged_rl</h1>

<p align="center">
  <a href="readme.md">中文</a> | <a href="readmd_EN.md">English</a>
</p>

本项目支持在50系和旧版Nvdia显卡上进行强化学习训练，同时也会是一个机器狗与人形强化学习的基础项目仓库。当前仅支持Unitree Go2，后续逐步添加更多机器人和算法支持。
# 版本分支介绍
- [main](https://github.com/yanyuze1/legged_rl/tree/main): 默认分支，稳定支持rl_sar部署实现
- [dev](https://github.com/yanyuze1/legged_rl/tree/dev): 测试分支，测试开发版本，当前非稳定支持rl_sar部署实现
# 快速开始
## 项目环境
- 创建conda环境
```bash
conda create -n legged_rl python=3.11
conda activate legged_rl
```
- 安装torch
```bash
pip install -U torch==2.7.0 torchvision==0.22.0 --index-url https://download.pytorch.org/whl/cu128
```
- 安装isaacsim和isaaclab
```bash
pip install isaaclab[isaacsim,all]==2.3.0 --extra-index-url https://pypi.nvidia.com
```
- 安装wand、rsl_rl和cusrl
```bash
python -m pip install wandb
git clone https://github.com/leggedrobotics/rsl_rl
cd rsl_rl
python -m pip install -e .
python -m pip install cusrl[all]
```
- 安装legged_rl项目
```bash
git clone https://github.com/yanyuze1/legged_rl.git
cd legged_rl
python -m pip install -e source/legged_rl
```
## 项目使用
### 列出所有可用环境
```bash
python scripts/list_envs.py
```
### 训练
- 平地训练
```bash
python scripts/rsl_rl/train.py \
  --task=LeggedRL-Isaac-Velocity-Flat-Unitree-Go2-v0 \
  --num_envs 4096 \
  --headless
python scripts/cusrl/train.py \
  --task=LeggedRL-Isaac-Velocity-Flat-Unitree-Go2-v0 \
  --num_envs 4096 \
  --headless
# 恢复训练
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
- 坡地训练
```bash
python scripts/rsl_rl/train.py \
  --task=LeggedRL-Isaac-Velocity-Rough-Unitree-Go2-v0 \
  --num_envs 4096 \
  --headless
python scripts/cusrl/train.py \
  --task=LeggedRL-Isaac-Velocity-Rough-Unitree-Go2-v0 \
  --num_envs 4096 \
  --headless
# 恢复训练
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
### 播放
- 平地播放
```bash
python scripts/rsl_rl/play.py \
    --task=LeggedRL-Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 16
python scripts/cusrl/play.py \
    --task=LeggedRL-Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 16
```
- 坡地播放
```bash
python scripts/rsl_rl/play.py \
    --task=LeggedRL-Isaac-Velocity-Rough-Unitree-Go2-v0 \
    --num_envs 16
python scripts/cusrl/play.py \
    --task=LeggedRL-Isaac-Velocity-Rough-Unitree-Go2-v0 \
    --num_envs 16
```
## sim2sim与真机部署
- 本项目真机部署支持使用[rl_sar](https://github.com/fan-ziqi/rl_sar)实现sim2sim测试与真机部署测试。
- 关于版本分支方面，[main](https://github.com/yanyuze1/legged_rl/tree/main)分支支持robot_lab模式下进行部署。[dev](https://github.com/yanyuze1/legged_rl/tree/dev)分支下支持himloco模式下进行部署(当前效果不佳)。
# 致谢
- [robot_lab](https://github.com/fan-ziqi/robot_lab)
- [legged_lab](https://github.com/zhw0422/legged_lab)
