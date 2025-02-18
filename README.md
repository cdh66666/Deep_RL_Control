# 四足 DRL 运动控制研究

以下所有操作均针对 Linux 系统，具体使用的是 Ubuntu 22.04。

- [四足 DRL 运动控制研究](#四足-drl-运动控制研究)
  - [项目日志](#项目日志)
    - [\[2025 年 2 月 15 日\]](#2025-年-2-月-15-日)
    - [\[2025 年 2 月 16 日\]](#2025-年-2-月-16-日)
    - [\[2025 年 2 月 17 日\]](#2025-年-2-月-17-日)
      - [项目环境安装步骤](#项目环境安装步骤)
  - [极简环境配置](#极简环境配置)
    - [特定网络工具使用指南](#特定网络工具使用指南)
    - [Miniconda 安装](#miniconda-安装)
    - [小鱼一键安装相关软件](#小鱼一键安装相关软件)
    - [VScode 开发与插件配置](#vscode-开发与插件配置)
  - [实战项目](#实战项目)
    - [基于 DDPG 算法的倒立摆控制](#基于-ddpg-算法的倒立摆控制)


## 项目日志
### [2025 年 2 月 15 日]
最初使用常规的 `git clone` 命令克隆四足 RL 毕设项目代码时，由于会获取全量历史记录，导致原本 3.7MB 的 GitHub 压缩包项目在克隆后达到 900MB。采用 `git clone --depth 1` 命令可仅获取最新版本，有效减少磁盘占用与克隆时间。本项目的完整克隆命令为：
```bash
git clone --depth 1 https://github.com/cdh66666/Deep_RL_Control.git
```
之后，我新建了一个同名仓库，将原仓库资料迁移过来并去除了所有历史记录，现在项目大小仅为 3.7MB，且已删除原仓库。后续计划搭建环境并对代码进行测试。

### [2025 年 2 月 16 日]
为配置深度强化学习环境，我参考了 [ISAAC Lab 官方指导文档](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/pip_installation.html)，该文档详细阐述了环境搭建的步骤与要求。
![issac_lab示例图](img_for_readme/issac_lab示例图.png)

同时，我还借鉴了 [isaacsim+isaaclab 一键安装脚本](https://www.bilibili.com/video/BV1k5BtYDEHU/?spm_id_from=333.337.search-card.all.click&vd_source=17ff47d01089cfbc609f2983503e8663) 视频中的方法。**特别注意**，<u>不管采用何种方法安装，都需预先配置好 miniconda 和 ros2 humble 环境。</u>

按照视频指导，通过执行以下命令可实现一键安装：
```bash
wget https://docs.robotsfan.com/install_isaaclab.sh -O install_isaaclab.sh && bash install_isaaclab.sh
```
执行上述命令后，所需环境便快速搭建完成，后续可基于此开展相关开发与测试工作。

目前，我已将所需环境全部安装至名为 `isaac` 的 Conda 虚拟环境中。激活该环境可使用如下命令：
```bash
conda activate isaac
```

激活后，能够正常使用 `isaacsim` 命令打开程序。然而，运行过程中出现诸多报错信息，且无法启用 GPU 加速功能，后续需对这些问题进行排查解决。 
 
### [2025 年 2 月 17 日]

在今日的工作中，安装 Isaac Lab 时频繁遭遇报错，致使安装工作未能成功。面对这一困境，我决定调整策略，重新尝试启用 Isaac Gym，期望以此为突破口推进相关工作。

与此同时，我开启了[强化学习训练 GO2 翻越多种地形](https://github.com/jindadu00/legged_robot_competition)项目的复刻工作。此项目极具研究价值与实践意义，它致力于运用强化学习算法，让 GO2 机器人在多样化的地形环境中自如地完成翻越动作。
![项目相关图片](img_for_readme/image.png)

#### 项目环境安装步骤
1. **创建并激活虚拟环境**
    - 为项目创建一个名为 `legged_robot_parkour` 的 Python 3.10 虚拟环境：
```bash
conda create --name legged_robot_parkour python=3.10
```
  - 激活该虚拟环境：
```bash
conda activate legged_robot_parkour
```
2. **安装 PyTorch 及其相关库**
根据 [PyTorch 官网](https://pytorch.org/get-started/previous-versions/) 的指导，针对 CUDA 12.1 环境，安装指定版本的 PyTorch 及相关库：
```bash
conda install pytorch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 pytorch-cuda=12.1 -c pytorch -c nvidia
```
3. **后续安装操作**
完成上述步骤后，其余的环境安装步骤可参照项目链接中的说明进行。后续我会持续跟进安装情况，并记录遇到的问题与解决方案。 


























## 极简环境配置
### 特定网络工具使用指南
参考链接：[四轮足仿真 - cdh](https://suyvt0crm5.feishu.cn/docx/XK72dTuyco6y7PxgA0dcaZZVngd)

1. **下载资源**：下载`0.tar`及`.yaml`配置文件。
2. **解压与启动**：在终端运行`tar -xvf 0.tar`解压`0.tar`。解压后，进入对应目录执行`./cfw`，打开界面，如下图所示：
![用户界面截图](img_for_readme/image2.png)
3. **导入配置文件**：在打开的界面左侧，点击“Profiles”，选择“import”，导入之前下载的`.yaml`配置文件。
4. **选择节点**：点击界面左侧“proxies”，挑选一个延迟较低的节点，右键点击该节点并选择“run script” 。
5. **网络代理设置**：打开电脑“设置”，进入“网络”，找到“网络代理”板块，参照以下图示进行设置：
![网络代理设置截图](img_for_readme/image3.png)
6. **端口同步**：每次重启电脑后，需保证电脑网络代理端口与界面左侧“General”下的“Port”一致。若“General”中的端口号改变，要把网络代理原来的端口7890更新为新的端口值。

**注意**：操作需符合相关规定 。 


### Miniconda 安装
可从 [Miniconda 官网](https://docs.anaconda.com/miniconda/install/#quick-command-line-install) 下载适用于 Linux 系统的安装脚本，然后按照官网的安装教程完成安装。


### 小鱼一键安装相关软件
使用小鱼一键安装脚本能够便捷地同时安装多个实用软件，其操作极为简便。在终端中依次运行以下命令：
```bash
wget http://fishros.com/install -O fishros_install.sh
chmod +x fishros_install.sh
./fishros_install.sh
```
**特别注意**：<u>在安装过程中，务必选择安装VSCode、GitHub Desktop Linux版、ROS 2 Humble版本以及微信Linux版。 </u>


### VScode 开发与插件配置
1. **安装 Python 插件**：打开 VSCode，按 `Ctrl + shift + x` 打开扩展面板，搜索并安装 Python 插件，该插件是后续进行 Python 开发及选择解释器的基础。
2. **选择 Python 解释器**：按 `Ctrl + shift + p` 打开命令面板，输入 `Python: Select Interpreter`，从系统中选择合适的 Python 解释器。
3. **配置默认终端**：在命令面板中输入 `Terminal: Select Default Profile`，选择 `bash` 作为默认终端配置。
4. **安装其他插件**
    - **中文语言包**：在扩展面板搜索 `Chinese (Simplified) Language Pack for Visual Studio Code` 并安装，安装完成后重启 VSCode，界面将变为中文。
    - **代码优化插件**：安装 MarsCode AI 插件实现代码自动联想补全，安装 Jupyter 插件优化 debug 体验。
    - **Markdown 相关插件**：安装 `Markdown All in One` 和 `Markdown Preview Enhanced` 插件，前者提供丰富的 Markdown 语法支持，后者提供美观且功能强大的实时预览功能，支持数学公式渲染、图表绘制等高级特性。

## 实战项目
### 基于 DDPG 算法的倒立摆控制
本项目的目标是实现四足深度强化学习运动控制，先从基于 DDPG 算法的倒立摆控制实战入手，通过该项目理解算法在控制问题中的应用，为后续应用到四足机器人的运动控制做准备。
![基于 DDPG 算法的倒立摆控制](img_for_readme/基于DDPG算法的倒立摆控制.gif) 