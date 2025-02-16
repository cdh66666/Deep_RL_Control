# 四足 DRL 运动控制研究

以下所有操作均针对 Linux 系统，具体使用的是 Ubuntu 22.04。

- [四足 DRL 运动控制研究](#四足-drl-运动控制研究)
  - [项目日志](#项目日志)
    - [\[2025 年 2 月 15 日\]](#2025-年-2-月-15-日)
    - [\[2025 年 2 月 16 日\]](#2025-年-2-月-16-日)
  - [极简环境配置](#极简环境配置)
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
为配置深度强化学习环境，我参考了 [ISAAC Lab 官方指导文档](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/pip_installation.html)，其详细说明了环境搭建的步骤与要求。
![issac_lab示例图](img_for_readme/issac_lab示例图.png)

同时，我还参考了 [isaacsim+isaaclab 一键安装脚本](https://www.bilibili.com/video/BV1k5BtYDEHU/?spm_id_from=333.337.search-card.all.click&vd_source=17ff47d01089cfbc609f2983503e8663) 视频。按照视频中的指导，可通过以下命令完成一键安装：
**特别注意**：<u>需有miniconda和ros2 humble环境。</u>
```bash
wget https://docs.robotsfan.com/install_isaaclab.sh -O install_isaaclab.sh && bash install_isaaclab.sh
```
执行上述代码后，即可快速搭建所需环境，后续可基于此开展相关开发与测试工作。 

 

## 极简环境配置
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