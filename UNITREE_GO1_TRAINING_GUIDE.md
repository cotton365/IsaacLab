# Unitree Go1 无头模式训练指南 (Unitree Go1 Headless Training Guide)

本文档说明如何在 IsaacLab 中使用无头模式训练 Unitree Go1 机器人任务。

## 快速开始 (Quick Start)

### 基础无头训练命令 (Basic Headless Training Commands)

#### 1. 平坦地形训练 (Flat Terrain Training)

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Flat-Unitree-Go1-v0 \
    --num_envs 128 \
    --headless
```

#### 2. 崎岖地形训练 (Rough Terrain Training)

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Rough-Unitree-Go1-v0 \
    --num_envs 128 \
    --headless
```

## 可用任务 (Available Tasks)

IsaacLab 为 Unitree Go1 提供了 4 个注册环境：

1. **Isaac-Velocity-Flat-Unitree-Go1-v0** - 平坦地形训练（推荐用于快速训练）
2. **Isaac-Velocity-Flat-Unitree-Go1-Play-v0** - 可视化场景（50个环境）
3. **Isaac-Velocity-Rough-Unitree-Go1-v0** - 崎岖地形训练（完整功能）
4. **Isaac-Velocity-Rough-Unitree-Go1-Play-v0** - 崎岖地形可视化

## 训练参数详解 (Training Parameters)

### 常用参数 (Common Parameters)

| 参数 | 说明 | 推荐值 |
|------|------|--------|
| `--task` | 任务名称 | Isaac-Velocity-Rough-Unitree-Go1-v0 |
| `--num_envs` | 并行环境数量 | 128-256 |
| `--headless` | 无头模式（无GUI，仅物理模拟） | 必需 |
| `--seed` | 随机种子 | 42 |
| `--max_iterations` | 最大训练迭代次数 | 1500（崎岖）/ 300（平坦） |
| `--device` | 计算设备 | cuda:0 |

### 实验管理参数 (Experiment Management)

| 参数 | 说明 | 示例 |
|------|------|------|
| `--experiment_name` | 实验文件夹名称 | my_go1_experiment |
| `--run_name` | 运行名称后缀 | run_001 |
| `--logger` | 日志记录器 | tensorboard / wandb |
| `--log_project_name` | 项目名称（wandb/neptune） | go1_locomotion |

### 视频录制参数 (Video Recording)

| 参数 | 说明 | 示例 |
|------|------|------|
| `--video` | 启用视频录制 | - |
| `--video_length` | 视频长度（步数） | 200 |
| `--video_interval` | 录制间隔（步数） | 2000 |
| `--enable_cameras` | 启用离屏渲染 | 与 --video 配合使用 |

### 检查点管理 (Checkpoint Management)

| 参数 | 说明 | 示例 |
|------|------|------|
| `--resume` | 从检查点恢复 | - |
| `--load_run` | 要恢复的运行文件夹名称 | run_001 |
| `--checkpoint` | 检查点文件名 | model_1000.pt |

## 高级训练示例 (Advanced Training Examples)

### 1. 完整配置的崎岖地形训练

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Rough-Unitree-Go1-v0 \
    --num_envs 256 \
    --headless \
    --seed 42 \
    --max_iterations 1500 \
    --experiment_name go1_rough_locomotion \
    --run_name experiment_001
```

### 2. 带视频录制的训练

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Rough-Unitree-Go1-v0 \
    --num_envs 64 \
    --headless \
    --video \
    --video_length 200 \
    --video_interval 2000 \
    --run_name go1_with_video
```

### 3. 使用 WandB 日志记录

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Rough-Unitree-Go1-v0 \
    --num_envs 128 \
    --headless \
    --logger wandb \
    --log_project_name go1_locomotion \
    --run_name wandb_experiment_001
```

### 4. 从检查点恢复训练

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Rough-Unitree-Go1-v0 \
    --num_envs 128 \
    --headless \
    --resume \
    --load_run experiment_001 \
    --checkpoint model_500.pt
```

### 5. 多 GPU 分布式训练

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Rough-Unitree-Go1-v0 \
    --num_envs 512 \
    --headless \
    --distributed
```

## 训练配置细节 (Training Configuration Details)

### 崎岖地形 PPO 配置 (Rough Terrain)

- **训练步数**: 24 steps per environment
- **最大迭代次数**: 1500
- **保存间隔**: 每 50 次迭代
- **Actor 网络**: [512, 256, 128]
- **Critic 网络**: [512, 256, 128]
- **学习率**: 1.0e-3

### 平坦地形 PPO 配置 (Flat Terrain)

- **最大迭代次数**: 300（更快收敛）
- **Actor/Critic 网络**: [128, 128, 128]（更小的网络）

## 监控训练 (Monitoring Training)

### 使用 TensorBoard

在单独的终端中运行：

```bash
./isaaclab.sh -p -m tensorboard.main --logdir logs/rsl_rl/
```

然后在浏览器中访问：`http://localhost:6006`

### 训练日志位置

训练日志保存在：
```
logs/rsl_rl/{task_name}/{experiment_name}/{run_name}_{timestamp}/
```

## 评估训练模型 (Evaluating Trained Models)

### 使用最新检查点

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task Isaac-Velocity-Rough-Unitree-Go1-v0 \
    --num_envs 32 \
    --use_last_checkpoint
```

### 使用特定检查点

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task Isaac-Velocity-Rough-Unitree-Go1-v0 \
    --num_envs 32 \
    --checkpoint logs/rsl_rl/rough_unitree_go1/experiment_001/model_1000.pt
```

## 其他强化学习库 (Other RL Libraries)

IsaacLab 也支持其他强化学习库：

### Stable-Baselines3

```bash
./isaaclab.sh -p scripts/reinforcement_learning/sb3/train.py \
    --task Isaac-Velocity-Rough-Unitree-Go1-v0 \
    --num_envs 128 \
    --headless
```

### RL-Games

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rl_games/train.py \
    --task Isaac-Velocity-Rough-Unitree-Go1-v0 \
    --headless
```

### SKRL

```bash
./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py \
    --task Isaac-Velocity-Rough-Unitree-Go1-v0 \
    --num_envs 128 \
    --headless
```

## 性能优化建议 (Performance Optimization)

1. **使用无头模式**: `--headless` 可以显著提高训练速度
2. **增加并行环境数**: 更多的环境可以加快数据收集速度（推荐 128-512）
3. **使用 GPU**: 确保使用 `--device cuda:0`
4. **避免在训练时渲染**: 除非需要录制视频，否则不要使用 `--enable_cameras`
5. **调整环境数量**: 如果 GPU 内存不足，减少 `--num_envs`

## 故障排除 (Troubleshooting)

### 内存不足

减少并行环境数：
```bash
--num_envs 64
```

### 训练速度慢

确保使用无头模式和 GPU：
```bash
--headless --device cuda:0
```

### 找不到任务

列出所有可用任务：
```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py --help
```

## 相关文件 (Related Files)

| 文件 | 路径 |
|------|------|
| RSL-RL 训练脚本 | `/scripts/reinforcement_learning/rsl_rl/train.py` |
| Go1 平坦地形配置 | `/source/isaaclab_tasks/.../velocity/config/go1/flat_env_cfg.py` |
| Go1 崎岖地形配置 | `/source/isaaclab_tasks/.../velocity/config/go1/rough_env_cfg.py` |
| Go1 PPO 代理配置 | `/source/isaaclab_tasks/.../velocity/config/go1/agents/rsl_rl_ppo_cfg.py` |
| 环境注册 | `/source/isaaclab_tasks/.../velocity/config/go1/__init__.py` |

## 参考文档 (Reference Documentation)

- Training Guide: `/docs/source/overview/reinforcement-learning/training_guide.rst`
- Run RL Training Tutorial: `/docs/source/tutorials/03_envs/run_rl_training.rst`
- AppLauncher Documentation: `/source/isaaclab/isaaclab/app/app_launcher.py`

---

## 总结 (Summary)

**最推荐的无头训练命令**:

```bash
# 崎岖地形（完整功能）
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Rough-Unitree-Go1-v0 \
    --num_envs 128 \
    --headless

# 平坦地形（快速训练）
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Flat-Unitree-Go1-v0 \
    --num_envs 128 \
    --headless
```

这些命令将启动无头模式训练，使用 RSL-RL 库和 PPO 算法训练 Unitree Go1 机器人完成速度跟踪任务。
