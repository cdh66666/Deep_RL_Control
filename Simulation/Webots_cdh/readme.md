## Webots2023b 机器人环境搭建（[教程](https://blog.csdn.net/weixin_43968987/article/details/128621942)）

![两轮机器人搭建](https://github.com/cdh66666/Deep_RL_Control/blob/main/img_for_readme/webots.png)

### VScode 联合 webots python开发流程

1. 在webots里创建python控制器。

2. 在vscode中打开控制器所在文件夹。

3. 按“ctrl+shift+P”打开搜索框，搜索“settings”，点击“首选项：打开工作区设置（JSON）”。

4. 在自动创建的.vscode/settings.json文件中加入如下代码（**即webots的python库路径**）：

   ```json
   {
       "python.autoComplete.extraPaths": [
           "E:\\webots_cdh\\Webots\\lib\\controller\\python"
       ],
       "python.analysis.extraPaths": [
           "E:\\webots_cdh\\Webots\\lib\\controller\\python"
       ]
   }
   ```

5. 开始享受vscode代码补全和跳转的魅力！