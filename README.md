# 四足DRL毕设日志

- [四足DRL毕设日志](#四足drl毕设日志)
  - [项目日志](#项目日志)
    - [\[2025年2月15日\]](#2025年2月15日)
    - [\[2025年2月16日\]](#2025年2月16日)
      - [安装 NVIDIA 570 显卡驱动](#安装-nvidia-570-显卡驱动)
      - [安装 CUDA 12.1](#安装-cuda-121)
  - [极简环境配置](#极简环境配置)
    - [Miniconda 安装](#miniconda-安装)
      - [Windows 系统](#windows-系统)
      - [Linux 系统](#linux-系统)
    - [Pytorch 和 Gymnasium 安装](#pytorch-和-gymnasium-安装)
    - [VScode 代码开发环境配置](#vscode-代码开发环境配置)
      - [Windows 系统](#windows-系统-1)
      - [Linux 系统](#linux-系统-1)
    - [VScode 配置中文环境](#vscode-配置中文环境)
    - [GitHub Desktop Linux 安装教程](#github-desktop-linux-安装教程)
    - [VScode Markdown 语法编辑预览插件安装及使用教程](#vscode-markdown-语法编辑预览插件安装及使用教程)
  - [实战项目](#实战项目)
    - [1. 基于DDPG算法的倒立摆控制](#1-基于ddpg算法的倒立摆控制)


## 项目日志

### [2025年2月15日]

今日在克隆四足 RL 毕设项目代码时，遇到了磁盘占用过大的问题。项目在 GitHub 上的压缩包仅 3.7MB，但使用常规克隆命令：
```bash
git clone https://github.com/cdh66666/Deep_RL_Control.git
```
克隆后的项目大小达到了 900MB。经过分析，发现该命令默认会克隆项目的所有历史提交记录，从而导致占用大量磁盘空间。

为解决这一问题，采用了以下命令进行克隆：
```bash
git clone --depth 1 https://github.com/cdh66666/Deep_RL_Control.git
```
此命令仅获取项目的最新版本，有效减少了磁盘占用，同时也显著缩短了克隆所需的时间。后续计划搭建项目环境并对代码进行测试。

### [2025年2月16日]

今日主要围绕深度强化学习环境的配置展开工作，参考了[isaacsim+isaaclab一键安装脚本](https://www.bilibili.com/video/BV1k5BtYDEHU/?spm_id_from=333.337.search-card.all.click&vd_source=17ff47d01089cfbc609f2983503e8663)视频中的安装步骤。同时，也参考了 ISAAC Lab 官方指导文档：[pip_installation](https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/pip_installation.html) ，具体示例图如下：
![issac_lab示例图](img_for_readme/issac_lab示例图.png)

#### 安装 NVIDIA 570 显卡驱动
在配置过程中，首先在 `base` 环境下进行了合适显卡驱动的安装。由于该安装操作是系统级别的，安装完成后整个系统均可通用，所有虚拟环境也能适用。具体安装流程如下：
1. **禁用 Nouveau 驱动**：Nouveau 是 NVIDIA 显卡的开源驱动，会和 NVIDIA 官方驱动冲突，需要将其禁用。
```bash
sudo bash -c "echo -e 'blacklist nouveau\noptions nouveau modeset=0' > /etc/modprobe.d/blacklist-nouveau.conf"
sudo update-initramfs -u
```
之后重启系统：
```bash
sudo reboot
```
2. **添加 NVIDIA 官方软件源**：
```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update
```
注意：如果你的系统不是 Ubuntu 22.04，需要将 `ubuntu2204` 替换为对应的 Ubuntu 版本代号。
3. **安装 NVIDIA 570 驱动**：
```bash
sudo apt-get install nvidia-driver-570
```
安装完成后，再次重启系统使驱动生效：
```bash
sudo reboot
```
4. **验证驱动安装**：
```bash
nvidia-smi
```
若能正常显示显卡信息和驱动版本，则说明驱动安装成功。

#### 安装 CUDA 12.1
本电脑最终确定的配置为：安装了 NVIDIA 570 显卡驱动以及 CUDA 12.1。CUDA 12.1 的安装流程如下：
1. **确保系统更新**：
```bash
sudo apt-get update
sudo apt-get upgrade
```
2. **安装 CUDA 12.1**：
```bash
sudo apt-get install cuda-12-1
```
3. **配置环境变量**：
编辑 `~/.bashrc` 文件：
```bash
nano ~/.bashrc
```
在文件末尾添加以下内容：
```plaintext
export PATH=/usr/local/cuda-12.1/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-12.1/lib64:$LD_LIBRARY_PATH
```
保存并退出文件，然后使配置生效：
```bash
source ~/.bashrc
```
4. **验证 CUDA 安装**：
```bash
nvcc --version
```
若能显示 CUDA 12.1 的版本信息，则说明 CUDA 安装成功。

接下来将基于此配置继续完成后续的环境搭建工作。 


 

## 极简环境配置
### Miniconda 安装
#### Windows 系统
1. 可从 Miniconda 官网自行下载：[Miniconda 下载](https://docs.anaconda.com/miniconda/install/#quick-command-line-install)
2. 或者通过 win + R 输入 cmd 回车打开命令行，运行以下代码（可一次性粘贴）：
```bash
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
start /wait "" .\miniconda.exe /S
del miniconda.exe
```
3. 按 win 键，搜索 Anaconda Prompt 并打开，输入以下命令，创建一个以“gym”为名字的新的虚拟环境：
```bash
conda create --name gym python=3.8
```
4. 激活虚拟环境“gym”：
```bash
conda activate gym
```

#### Linux 系统
1. 打开终端，使用 `wget` 下载 Miniconda 安装脚本：
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
2. 赋予脚本执行权限并运行安装脚本：
```bash
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
```
3. 按照安装提示完成安装，安装完成后，在终端输入以下命令，创建“gym”虚拟环境：
```bash
conda create --name gym python=3.8
```
4. 激活虚拟环境“gym”：
```bash
conda activate gym
```

### Pytorch 和 Gymnasium 安装
1. 访问 Pytorch 官网：[Pytorch 官网](https://pytorch.org/)
2. 向下滑动页面，选择配置，运行对应命令。
    - 本电脑配置：Stable (2.5.1) ---- Windows ---- Pip ---- Python ---- CPU，可在 Anaconda Prompt 运行如下命令：
```bash
conda activate gym
pip3 install torch torchvision torchaudio
```
3. 安装 Gymnasium 及相关库：
```bash
pip install gymnasium
pip install matplotlib
```

### VScode 代码开发环境配置
#### Windows 系统
1. 从 VScode 官网下载安装包并安装：[VScode 官网](https://code.visualstudio.com/)
2. 打开 VScode，按 Ctrl + shift + p 打开命令提示行。
3. 安装 Python 解释器插件。
4. 命令行输入 `Python: select interpreter`，选择要使用的 Python 解释器（选虚拟环境 gym 对应解释器）。
    ![](img_for_readme/vscode环境配置1.png)
5. 在命令行输入 `Terminal: select default profile`，确保你选择的是合适的终端配置（如 `Command Prompt` 等），而非 `powershell`。
    ![](img_for_readme/vscode环境配置2.png)
6. 出现相应界面即可在 VScode 终端中进行环境配置操作（gym&cmd）。
7. 安装优化代码插件，在搜索栏搜索安装：
    - 安装 MarsCode AI 插件，代码自动联想补全，超级实用。
    - 安装 Jupyter 插件，优化 debug 体验。

#### Linux 系统
1. **通用安装方法（适用于大多数基于 Debian 或 Ubuntu 的系统）**：
    - 打开终端，更新系统软件包列表并安装必要工具：
```bash
sudo apt-get update
sudo apt-get install wget gpg
```
    - 下载并安装 Microsoft GPG 密钥：
```bash
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
```
    - 添加 VScode 软件源：
```bash
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
rm -f packages.microsoft.gpg
```
    - 更新软件包列表并安装 VScode：
```bash
sudo apt-get update
sudo apt-get install code
```
2. 后续步骤与 Windows 系统一致，按 Ctrl + shift + p 打开命令提示行，安装 Python 解释器插件，选择 Python 解释器、终端默认配置（如 `bash`），安装相关插件等。

### VScode 配置中文环境
1. 打开 VScode，按 Ctrl + shift + x 打开扩展面板。
2. 在搜索框输入 `Chinese (Simplified) Language Pack for Visual Studio Code` 并安装。
3. 安装完成后，右下角会提示重启 VScode，重启后界面即为中文。 

### GitHub Desktop Linux 安装教程
1. 打开终端，使用 `wget` 下载 GitHub Desktop 的 `.deb` 安装包（以 3.1.7 版本为例，你可根据实际情况调整版本号）：
```bash
wget https://github.com/shiftkey/desktop/releases/download/release-3.1.7-linux1/GitHubDesktop-linux-3.1.7-linux1.deb
```
2. 安装下载的 `.deb` 包（需确保系统已安装 `dpkg`）：
```bash
sudo dpkg -i GitHubDesktop-linux-3.1.7-linux1.deb
```
3. 如果安装过程中提示依赖缺失，可使用以下命令修复依赖：
```bash
sudo apt-get install -f
```
4. 安装完成后，你可以在应用程序菜单中找到 GitHub Desktop 并启动它。首次启动时，按照提示进行登录和相关设置即可使用。

### VScode Markdown 语法编辑预览插件安装及使用教程
1. **安装插件**：
    - 打开 VScode，按 Ctrl + shift + x 打开扩展面板。
    - 在搜索框输入 `Markdown All in One` 并安装。该插件提供了丰富的 Markdown 语法支持，包括代码块语法高亮、表格编辑等功能。
    - 另外，强烈推荐安装 `Markdown Preview Enhanced` 插件。它能提供更美观、功能更强大的 Markdown 实时预览功能，支持数学公式渲染、图表绘制等高级特性。在扩展面板搜索框输入该插件名称并安装。
2. **使用教程**：
    - **基本语法编辑**：安装 `Markdown All in One` 后，在新建或打开 Markdown 文件（`.md` 后缀）时，即可直接使用 Markdown 语法进行编辑。例如，输入 `# 标题` 生成一级标题，`## 二级标题` 生成二级标题等。使用 `* 列表项` 生成无序列表，`1. 列表项` 生成有序列表。
    - **实时预览**：安装 `Markdown Preview Enhanced` 后，打开 Markdown 文件，按 `Ctrl + Shift + V` 组合键（或者点击编辑器右上角的眼睛图标），即可在右侧打开实时预览窗口，实时展示 Markdown 内容渲染后的效果。在编辑区修改内容时，预览区会实时更新。
    - **高级功能**：`Markdown Preview Enhanced` 支持多种高级功能。例如，要插入数学公式，可使用 `$` 符号包裹 LaTeX 公式语法，如 `$E = mc^2$` 会渲染为 $E = mc^2$。绘制图表方面，可使用特定的语法，如 Mermaid 语法来创建流程图、时序图等。比如创建一个简单的流程图：
```mermaid
    graph TD;
        A-->B;
        A-->C;
        B-->D;
        C-->D;
```
只需在 Markdown 文件中输入上述代码块，预览时就会显示为对应的流程图。
 
## 实战项目

### 1. 基于DDPG算法的倒立摆控制

![基于DDPG算法的倒立摆控制](img_for_readme/基于DDPG算法的倒立摆控制.gif)