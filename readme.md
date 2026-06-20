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
- 安装wand与rsl_rl
```bash
python -m pip install wandb
git clone https://github.com/leggedrobotics/rsl_rl
cd rsl_rl
pip install -e .
```
- 安装legged_rl项目
```bash
git clone https://github.com/yanyuze1/legged_rl.git
cd legged_rl
python -m pip install -e source/legged_rl
python -m pip install -e source/legged_rl/legged_rl/rsl_rl
```
## 项目使用
- 列出所有可用环境
```bash
python scripts/list_envs.py
```
- 训练
```bash
python scripts/rsl_rl/train.py \
  --task=LeggedRL-Velocity-Flat-Unitree-Go2-v0 \
  --num_envs 4096 \
  --headless
# 恢复训练
python scripts/rsl_rl/train.py \
  --task=LeggedRL-Velocity-Flat-Unitree-Go2-v0 \
  --num_envs 4096 \
  --headless \
  --resume \
  --load_run 2026-06-19_20-38-06 \
  --checkpoint model_100.pt
```
- 播放
```bash
python scripts/rsl_rl/play.py \
    --task=LeggedRL-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 16
```
