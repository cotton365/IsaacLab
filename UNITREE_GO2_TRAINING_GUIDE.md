# Unitree Go2 无头模式训练指南 (Unitree Go2 Headless Training Guide)

本文档说明如何在 IsaacLab 中使用无头模式训练 Unitree Go2 机器人任务。

## 快速开始 (Quick Start)

### 基础无头训练命令 (Basic Headless Training Commands)

#### 1. 平坦地形训练 (Flat Terrain Training) - 推荐命令

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 4096 \
    --headless
```

#### 2. 崎岖地形训练 (Rough Terrain Training)

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Rough-Unitree-Go2-v0 \
    --num_envs 4096 \
    --headless
```

## 可用任务 (Available Tasks)

IsaacLab 为 Unitree Go2 提供了 4 个注册环境：

1. **Isaac-Velocity-Flat-Unitree-Go2-v0** - 平坦地形训练（推荐用于快速训练）
2. **Isaac-Velocity-Flat-Unitree-Go2-Play-v0** - 可视化场景（50个环境，无随机化）
3. **Isaac-Velocity-Rough-Unitree-Go2-v0** - 崎岖地形训练（完整功能）
4. **Isaac-Velocity-Rough-Unitree-Go2-Play-v0** - 崎岖地形可视化（50个环境）

## 训练参数详解 (Training Parameters)

### 常用参数 (Common Parameters)

| 参数 | 说明 | 推荐值 |
|------|------|--------|
| `--task` | 任务名称 | Isaac-Velocity-Flat-Unitree-Go2-v0 |
| `--num_envs` | 并行环境数量 | 4096（推荐）/ 128-512 |
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

### 1. 完整配置的平坦地形训练（推荐用于 Isaac-Velocity-Flat-Unitree-Go2-v0）

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 4096 \
    --headless \
    --seed 42 \
    --max_iterations 300 \
    --experiment_name go2_flat_locomotion \
    --run_name experiment_001
```

### 2. 完整配置的崎岖地形训练

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Rough-Unitree-Go2-v0 \
    --num_envs 4096 \
    --headless \
    --seed 42 \
    --max_iterations 1500 \
    --experiment_name go2_rough_locomotion \
    --run_name experiment_001
```

### 3. 带视频录制的训练

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 64 \
    --headless \
    --video \
    --video_length 200 \
    --video_interval 2000 \
    --run_name go2_with_video
```

### 4. 使用 WandB 日志记录

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 4096 \
    --headless \
    --logger wandb \
    --log_project_name go2_locomotion \
    --run_name wandb_experiment_001
```

### 5. 从检查点恢复训练

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 4096 \
    --headless \
    --resume \
    --load_run experiment_001 \
    --checkpoint model_150.pt
```

### 6. 多 GPU 分布式训练

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 8192 \
    --headless \
    --distributed
```

### 7. 使用 SKRL 框架训练

```bash
./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 4096 \
    --headless
```

## 训练配置细节 (Training Configuration Details)

### Go2 机器人规格 (Go2 Robot Specifications)

- **模型文件**: `/Robots/Unitree/Go2/go2.usd`
- **执行器类型**: DC 电机（直流电机模型）
- **电机参数**:
  - 力矩限制: 23.5 Nm
  - 速度限制: 30.0 rad/s
  - 刚度: 25.0
  - 阻尼: 0.5
- **初始位置**: (0, 0, 0.4m)
- **软关节位置限制因子**: 0.9

### 崎岖地形 PPO 配置 (Rough Terrain)

- **训练步数**: 24 steps per environment
- **最大迭代次数**: 1500
- **保存间隔**: 每 50 次迭代
- **Actor 网络**: [512, 256, 128]
- **Critic 网络**: [512, 256, 128]
- **学习率**: 1.0e-3
- **学习周期数**: 5
- **小批次数量**: 4
- **SKRL 时间步**: 36,000

### 平坦地形 PPO 配置 (Flat Terrain)

- **最大迭代次数**: 300（更快收敛）
- **Actor/Critic 网络**: [128, 128, 128]（更小的网络）
- **学习率**: 1.0e-3
- **学习周期数**: 5
- **小批次数量**: 4
- **SKRL 时间步**: 7,200
- **特殊奖励权重**:
  - flat_orientation_l2: -2.5
  - feet_air_time: 0.25

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

### 什么是 play.py？(What is play.py?)

**是的！** `play.py` 脚本就是用来**调用和运行训练好的模型**进行推理的工具。

**play.py 的主要功能**:
1. ✅ **加载训练好的检查点** (模型权重)
2. ✅ **运行推理** - 使用训练好的策略控制机器人
3. ✅ **可视化** - 在模拟器中实时显示机器人行为
4. ✅ **录制视频** - 可选地录制机器人运动视频
5. ✅ **导出模型** - 自动将策略导出为 JIT 和 ONNX 格式

### 使用特定检查点（推荐方式）

**示例：加载您训练的模型**

```bash
# 这个命令会加载您训练好的 model_299.pt 检查点并运行推理
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --checkpoint logs/rsl_rl/unitree_go2_flat/2026-03-13_21-37-28/model_299.pt \
    --num_envs 4
```

**这个命令做了什么？**
- 📁 从 `logs/rsl_rl/unitree_go2_flat/2026-03-13_21-37-28/model_299.pt` 加载训练好的模型
- 🤖 创建 4 个并行环境来运行推理
- 🎮 使用训练好的策略控制 Unitree Go2 机器人
- 👁️ 在 Isaac Sim 窗口中显示机器人运动（非无头模式）
- 💾 自动导出模型到 `logs/rsl_rl/unitree_go2_flat/2026-03-13_21-37-28/exported/` 目录

**注意**:
- `model_299.pt` 表示这是第 299 次迭代保存的检查点
- 如果训练了 300 次迭代，这是最后一个检查点
- 使用更少的环境数（如 4）可以更容易观察单个机器人的行为

### 使用最新检查点（自动查找）

如果不想手动指定检查点路径，可以让脚本自动查找最新的：

```bash
# RSL-RL 使用 --load_run 和 --load_checkpoint 参数
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 32
```

**注意**:
- 如果不指定 `--checkpoint`、`--load_run` 或 `--use_pretrained_checkpoint`，脚本会自动从默认日志目录查找最新的检查点
- RSL-RL 的 play.py **不支持** `--use_last_checkpoint` 参数（该参数仅在 RL-Games 和 SB3 中可用）

**使用 load_run 参数的替代方法**:

```bash
# 指定运行文件夹名称（不需要完整路径和时间戳）
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 32 \
    --load_run experiment_001
```

### 录制视频

记录训练好的机器人行为视频：

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --checkpoint logs/rsl_rl/unitree_go2_flat/2026-03-13_21-37-28/model_299.pt \
    --num_envs 4 \
    --video \
    --video_length 500
```

视频将保存在：`logs/rsl_rl/unitree_go2_flat/2026-03-13_21-37-28/videos/play/`

### 使用 Play 任务进行可视化（50个环境，更快渲染）

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-Play-v0 \
    --num_envs 50 \
    --checkpoint logs/rsl_rl/unitree_go2_flat/2026-03-13_21-37-28/model_299.pt
```

**Play 任务 vs 普通任务**:
- **Play 任务** (`-Play-v0` 后缀):
  - 固定 50 个环境
  - 禁用域随机化，更稳定的可视化
  - 更小的场景，渲染更快
- **普通任务**: 训练和评估都可以使用，可以自定义环境数量

### 实时模式运行

以实时速度运行（接近真实机器人的速度）：

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --checkpoint logs/rsl_rl/unitree_go2_flat/2026-03-13_21-37-28/model_299.pt \
    --num_envs 1 \
    --real-time
```

**推荐用于**：观察单个机器人的详细行为，或准备实际部署

## 其他强化学习库 (Other RL Libraries)

IsaacLab 也支持其他强化学习库：

### Stable-Baselines3

```bash
./isaaclab.sh -p scripts/reinforcement_learning/sb3/train.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 4096 \
    --headless
```

### RL-Games

```bash
./isaaclab.sh -p scripts/reinforcement_learning/rl_games/train.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --headless
```

### SKRL（推荐，有专门的 Go2 配置文件）

```bash
./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 4096 \
    --headless
```

SKRL 配置文件位置：
- 平坦地形: `/source/isaaclab_tasks/.../config/go2/agents/skrl_flat_ppo_cfg.yaml`
- 崎岖地形: `/source/isaaclab_tasks/.../config/go2/agents/skrl_rough_ppo_cfg.yaml`

## 完整工作流程 (Complete Workflow)

### 从训练到评估的完整流程

```bash
# 步骤 1: 训练模型（无头模式，更快）
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 4096 \
    --headless \
    --experiment_name my_go2_experiment \
    --run_name run_001

# 训练完成后，检查点会保存在:
# logs/rsl_rl/unitree_go2_flat/my_go2_experiment/run_001_{timestamp}/model_*.pt

# 步骤 2: 评估训练好的模型（带可视化）
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --checkpoint logs/rsl_rl/unitree_go2_flat/my_go2_experiment/run_001_{timestamp}/model_299.pt \
    --num_envs 4

# 步骤 3: 录制视频
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --checkpoint logs/rsl_rl/unitree_go2_flat/my_go2_experiment/run_001_{timestamp}/model_299.pt \
    --num_envs 4 \
    --video \
    --video_length 500
```

### 理解检查点文件

训练过程中会定期保存检查点：

```
logs/rsl_rl/unitree_go2_flat/my_experiment/run_001_2026-03-13_21-37-28/
├── model_0.pt       # 第 0 次迭代（初始化）
├── model_50.pt      # 第 50 次迭代
├── model_100.pt     # 第 100 次迭代
├── model_150.pt     # 第 150 次迭代
├── model_200.pt     # 第 200 次迭代
├── model_250.pt     # 第 250 次迭代
├── model_299.pt     # 第 299 次迭代（最后一个，如果训练了 300 次）
└── exported/        # play.py 自动导出的模型
    ├── policy.pt    # JIT 格式
    └── policy.onnx  # ONNX 格式
```

**选择检查点的建议**:
- 使用**最后一个检查点** (`model_299.pt`) 通常是最好的
- 如果最后的检查点表现不佳，可以尝试较早的检查点（如 `model_250.pt`）
- 平坦地形默认每 50 次迭代保存一次

## 性能优化建议 (Performance Optimization)

1. **使用无头模式**: `--headless` 可以显著提高训练速度
2. **增加并行环境数**: Go2 推荐使用 4096 个并行环境以加快训练（比 Go1 更多）
3. **使用 GPU**: 确保使用 `--device cuda:0`
4. **避免在训练时渲染**: 除非需要录制视频，否则不要使用 `--enable_cameras`
5. **调整环境数量**: 如果 GPU 内存不足，减少 `--num_envs`
6. **选择合适的地形**: 平坦地形训练更快（300 迭代 vs 1500 迭代）

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

### 评估时找不到检查点

检查日志目录结构：
```bash
ls -la logs/rsl_rl/unitree_go2_flat/
```

确保使用正确的时间戳目录和检查点文件名。

### Isaac Sim 启动后卡住（显示网格警告）

**症状**: Isaac Sim 成功启动，显示大量网格 primvar 警告后卡住

```
[Warning] [omni.hydra] Mesh '/__Prototype_xxx/mesh_0' has corrupted data in primvar 'st':
buffer size 6270 doesn't match expected size 25806 in faceVarying primvars
```

**原因**:
- 地形网格生成时 UV 坐标数据不一致
- Hydra 渲染引擎尝试验证/修复损坏的网格数据时阻塞
- 主要发生在使用复杂地形（rough terrain）的环境中

**解决方案**:

1. **使用平坦地形进行测试**（最简单）:
```bash
# 使用 Flat 任务，避免复杂地形生成
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --checkpoint logs/rsl_rl/unitree_go2_flat/.../model_299.pt \
    --num_envs 4
```

2. **使用无头模式**（跳过渲染验证）:
```bash
# 添加 --headless 避免网格渲染问题
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task Isaac-Velocity-Rough-Unitree-Go2-v0 \
    --checkpoint logs/rsl_rl/unitree_go2_flat/.../model_299.pt \
    --num_envs 4 \
    --headless
```

3. **使用更少的环境数**:
```bash
# 减少并行环境可以降低网格复杂度
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task Isaac-Velocity-Rough-Unitree-Go2-v0 \
    --checkpoint logs/rsl_rl/unitree_go2_flat/.../model_299.pt \
    --num_envs 1  # 只用一个环境
```

4. **清除地形缓存**（如果问题持续）:
```bash
# 删除缓存的地形文件
rm -rf logs/terrains/
```

**注意**:
- 这些警告本身不会导致功能失败，但可能导致启动延迟或卡住
- 平坦地形（Flat）环境不会触发这些警告，因为它使用简单的平面而非程序化地形
- 无头模式训练不受影响，因为不需要渲染网格

## 常见问题 (FAQ)

### Q1: play.py 和 train.py 有什么区别？

| 脚本 | 用途 | 模式 | 保存检查点 |
|------|------|------|-----------|
| **train.py** | 训练新模型 | 无头模式（推荐）| ✅ 是 |
| **play.py** | 评估已训练模型 | 有可视化 | ❌ 否（但导出 JIT/ONNX）|

### Q2: 为什么 play.py 使用较少的环境数？

- **训练**: 使用大量环境（4096）加快数据收集
- **评估**: 使用少量环境（4-32）更容易观察和调试单个机器人

### Q3: play.py 会修改我的检查点吗？

**不会**。play.py 只读取检查点，不会修改它。它会在 `exported/` 子目录中创建导出的模型。

### Q4: 我可以在训练过程中使用 play.py 吗？

**可以**。您可以在训练的同时，在另一个终端中使用 play.py 评估中间检查点，观察训练进度。

### Q5: 导出的 policy.pt 和 policy.onnx 是什么？

- **policy.pt** (JIT): 可以在 Python/PyTorch 中直接使用
- **policy.onnx**: 可以在其他框架中使用，或部署到实际机器人
- 这两个文件是 play.py 自动创建的，方便模型部署

### Q6: 为什么我的检查点路径和文档中的不同？

检查点路径取决于：
- `--experiment_name`: 实验名称
- `--run_name`: 运行名称
- 时间戳: 训练开始时自动生成

示例: `logs/rsl_rl/unitree_go2_flat/my_experiment/run_001_2026-03-13_21-37-28/`

### Q7: 如何选择最佳检查点？

1. 查看 TensorBoard 日志，找到奖励最高的迭代
2. 通常最后的检查点 (`model_299.pt`) 是最好的
3. 使用 play.py 测试多个检查点，选择表现最好的

### Q8: 为什么出现 "LexerNoViableAltException" 错误？

**错误原因**: 您可能使用了 `--use_last_checkpoint` 参数，但 RSL-RL 的 play.py **不支持**此参数。

**错误示例**:
```bash
# ❌ 会导致 LexerNoViableAltException 错误
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --use_last_checkpoint
```

**正确做法**:
```bash
# ✅ 方法 1: 省略检查点参数，自动查找最新的
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0

# ✅ 方法 2: 使用 --load_run 参数
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --load_run experiment_001

# ✅ 方法 3: 直接指定 --checkpoint 路径
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --checkpoint logs/rsl_rl/unitree_go2_flat/.../model_299.pt
```

**注意**: `--use_last_checkpoint` 仅在 RL-Games 和 Stable-Baselines3 (SB3) 中可用。

### Q9: 不同 RL 框架的 checkpoint 加载方式有何不同？

| RL 框架 | 自动加载最新检查点 | 指定检查点路径 |
|---------|-------------------|---------------|
| **RSL-RL** | 省略所有参数 或 使用 `--load_run` | `--checkpoint path/to/model.pt` |
| **RL-Games** | `--use_last_checkpoint` | `--checkpoint path/to/model.pt` |
| **SB3** | `--use_last_checkpoint` | `--checkpoint path/to/model.zip` |
| **SKRL** | 省略所有参数 | `--checkpoint path/to/model` |

### Q10: 网格 primvar 警告是什么意思？可以忽略吗？

**警告示例**:
```
[Warning] [omni.hydra] Mesh '/__Prototype_xxx/mesh_0' has corrupted data in primvar 'st'
```

**含义**:
- `primvar 'st'` 是 USD 中存储纹理坐标（UV 映射）的数据
- 警告表示纹理坐标数据的缓冲区大小与网格面数不匹配
- 这通常发生在地形生成时多个网格被合并但 UV 数据不一致

**是否可以忽略**:
- ✅ **训练时**: 完全可以忽略，不影响物理模拟和训练
- ✅ **无头模式评估**: 可以忽略，因为不需要渲染
- ⚠️ **可视化评估**: 可能导致启动延迟或卡住，建议使用故障排除中的解决方案

**不同地形类型的影响**:
- **Flat (平坦地形)**: 不会出现警告，使用简单平面
- **Rough (崎岖地形)**: 会出现多个警告，使用程序化地形生成

**最佳实践**:
- 训练使用无头模式，不受影响
- 评估使用平坦地形任务（`-Flat-` 版本）避免警告
- 如需评估崎岖地形模型，使用无头模式或减少环境数

## 相关文件 (Related Files)

| 文件 | 路径 |
|------|------|
| RSL-RL 训练脚本 | `/scripts/reinforcement_learning/rsl_rl/train.py` |
| SKRL 训练脚本 | `/scripts/reinforcement_learning/skrl/train.py` |
| Go2 平坦地形配置 | `/source/isaaclab_tasks/.../velocity/config/go2/flat_env_cfg.py` |
| Go2 崎岖地形配置 | `/source/isaaclab_tasks/.../velocity/config/go2/rough_env_cfg.py` |
| Go2 RSL-RL PPO 配置 | `/source/isaaclab_tasks/.../velocity/config/go2/agents/rsl_rl_ppo_cfg.py` |
| Go2 SKRL 平坦配置 | `/source/isaaclab_tasks/.../velocity/config/go2/agents/skrl_flat_ppo_cfg.yaml` |
| Go2 SKRL 崎岖配置 | `/source/isaaclab_tasks/.../velocity/config/go2/agents/skrl_rough_ppo_cfg.yaml` |
| Go2 环境注册 | `/source/isaaclab_tasks/.../velocity/config/go2/__init__.py` |
| Go2 机器人配置 | `/source/isaaclab_assets/isaaclab_assets/robots/unitree.py` (行 140-181) |
| Sim2Sim 转移配置 | `/scripts/sim2sim_transfer/config/newton_to_physx_go2.yaml` |

## 参考文档 (Reference Documentation)

- Training Guide: `/docs/source/overview/reinforcement-learning/training_guide.rst`
- Run RL Training Tutorial: `/docs/source/tutorials/03_envs/run_rl_training.rst`
- Environments Overview: `/docs/source/overview/environments.rst`
- Newton Physics Integration: `/docs/source/experimental-features/newton-physics-integration/training-environments.rst`
- AppLauncher Documentation: `/source/isaaclab/isaaclab/app/app_launcher.py`

---

## 总结 (Summary)

**最推荐的 Isaac-Velocity-Flat-Unitree-Go2-v0 无头训练命令**:

```bash
# 使用 RSL-RL 训练（推荐，默认配置）
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 4096 \
    --headless

# 使用 SKRL 训练（有专门的 Go2 配置文件）
./isaaclab.sh -p scripts/reinforcement_learning/skrl/train.py \
    --task Isaac-Velocity-Flat-Unitree-Go2-v0 \
    --num_envs 4096 \
    --headless
```

这些命令将启动无头模式训练，使用 PPO 算法训练 Unitree Go2 机器人在平坦地形上完成速度跟踪任务。

### 关键要点 (Key Points)

1. **任务名称**: `Isaac-Velocity-Flat-Unitree-Go2-v0`（不是 Go1）
2. **推荐并行环境数**: 4096（Go2 比 Go1 推荐更多环境）
3. **训练框架**: RSL-RL 或 SKRL（Go2 有专门的 SKRL 配置）
4. **平坦地形迭代次数**: 300（比崎岖地形的 1500 快得多）
5. **网络结构**: [128, 128, 128]（平坦地形使用更小的网络）
6. **机器人特点**: 使用 DC 电机模型，力矩限制 23.5 Nm
