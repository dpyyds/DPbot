# DPbot - 全能机器人

DPbot是一个基于Python的机器人框架，支持插件化开发，提供了丰富的功能接口，可基于此框架拓展为群活跃助手、台账机器人、定时推送机器人、ai画图机器人、智能客服、返利机器人。

## 互助群

欢迎加入我们的互助交流群，和更多开发者一起交流、答疑解惑、分享经验！

![DPbot 互助群二维码](Help/img/dpbot.png)


## 功能特点

- 🔌 插件化架构，易于扩展
- 🚀 异步处理，收发消息队列处理，避免消息丢失
- 🖼️ 支持图片、视频、音频等多媒体消息处理
- 🎵 支持语音消息转换和处理
- 📝 支持群聊和私聊消息处理
- ⚙️ 支持群聊设定模式，支持特定群聊模式插件口令启停
- ⏭️ 历史消息跳过
- 🔄 支持二维码登录
- 💾 SQLite数据库支持
- 📊 完整的日志系统
- 🛠️ 丰富的工具类支持

## 系统要求

- Python 3.11+
- Windows 10+ 或 Linux (ubuntu:24.04)
- 2GB+ RAM
- 500MB+ 磁盘空间

## 系统介绍
### 系统框架

项目采用模块化设计，主要包含以下核心组件：

- 📂 Core/
  - 🔧 核心引擎模块，消息队列和事件处理系统 (MessageHandler.py)
  - 🔌 插件基类和管理器 (PluginBase.py, PluginManager.py)
  - 🚦 消息字段封装处理，可适配WCF/NGCBOT (msg.py)
  - 🔗 登录流程处理 (LoginManager.py)

- 📂 Plugins/
  - 🎮 内置功能插件 (Admin/, Menu/, DailyPoint/, RandomPic/, RandomVideo/, ReqMusic/, DpWenan/, ShortVideoParse/，DpTools/,DemoPlugin/)
  - 🔧 自定义插件工具接口 (_Tools/)

- 📂 WeChatApi/
  - 🤖 协议接入层 
  - 📡 消息收发接口
  - 🔐 登录管理
  - 🔄 二次封装接口，基于其他接口进行封装，例如（获取昵称、获取头像）（CommonApi.py）

- 📂 DbServer/
  - 💾 数据库操作封装 (SQLite)
  - 📊 数据模型定义
  - 🔄 数据同步管理

- 📂 Config/
  - ⚙️ 全局配置文件 ，可配置管理员wxid、是否跳过历史信息、日志管理(Config.toml)
  - 📝 日志文件 (logs/app.log, logs/error.log)
  - 🔐 登录配置 ，可配置协议运行IP、端口、机器人wxid（首次登录会自动配置，不需自处理）(Login.toml)
  - 插件配置文件，配置插件启动模式（plugininit.xlsx）
- 系统工作流程：
   - 通过 WeChatApi 模块接收消息
   - Core 引擎进行消息分发和处理
   - Plugins 系统处理具体业务逻辑
   - DbServer 负责数据持久化
   - Config 模块提供全局配置支持

### 内置插件
- Admin: 管理员插件
- Menu: 菜单插件
- DailyPoint: 签到插件（后续可拓展积分功能）
- RandomPic: 随机图片插件
- RandomVideo: 随机视频插件
- ReqMusic: 点歌插件
- DpWenan: 文案插件
- ShortVideoParse：短视频解析插件
- ReqMusic：点歌插件

### 开发自定义插件

   - 在 `Plugins` 目录下创建新的插件目录
   - 创建插件主文件（例如：`DemoPlugin.py`）
   - 创建插件配置文件（例如：`config.toml`）
   - 继承 `PluginBase` 类并实现必要方法：
   ```python
   from Plugins._Tools import Tools
   from Config.logger import logger
   import Config.ConfigServer as Cs
   from Core.PluginBase import PluginBase
   class DemoPlugin(PluginBase):
       def __init__(self):
           super().__init__()
           self.name = "DemoPlugin"#此名称需与App/Config/plugininit.xlsx中名称一致
           self.description = "插件描述"
           self.version = "1.0.0"
           self.author = "作者名"
           self.tools = Tools()
           self.configData = self.tools.returnConfigData(os.path.dirname(__file__))
           self.word = self.configData.get('word')
       async def handle_message(self, msg) -> bool:
           # 处理群聊消息的逻辑
           pass
       async def handle_private_message(self, msg):
           # 处理私聊消息的逻辑
           pass         
   ```

## 数据库说明

项目使用SQLite数据库，包含以下数据表：
- admin: 管理员配置
- plugin_config: 插件配置
## linux系统安装指南
   - 支持linux直接运行或者docker运行
   - 熟练掌握linux基础操作的朋友，可私我免费获取Wxapi的compose文件，自行构建项目，无教程，没基础就算了，没空教
## win系统安装指南
   - **star项目是获得永久授权的前置条件**
   - **star项目是获得永久授权的前置条件**
   - **star项目是获得永久授权的前置条件**
### 环境自检
   - 确认是否安装`python`，如无，自行百度安装
   - `8059`、`6379`端口是否占用，如占用可自行关闭或者修改`Wxapi-conf-app.conf`改为其他端口
### 启动redis
   - 进入`Redis`文件夹，双击`redis-server.exe`
### 启动协议
   - 进入`Wxapi`文件夹，双击`wxapi_win64_v1_0_5.exe`
   - 记录缘分码，后面用于插件兑换永久授权
### 启动机器人：
   - 进入`App`文件夹
   - 安装依赖，`pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`然后`python.exe -m pip install --upgrade pip`然后`pip install -r requirements-win.txt`
   - 其中处理语音需要依赖`ffmpeg`，自行百度安装
   - 自定义设备信息，修改文件App/WeChatApi/LoginApi.py,
   - ```
         async def getIpadQr(self) -> Optional[Dict]:
        """
        获取二维码
        """
        try:
            payload = {
                "DeviceID": "123456",
                "DeviceName": "iPhone18plus",
                "Proxy": {
                    "ProxyIp": "",
                    "ProxyPassword": "",
                    "ProxyUser": ""
                }
            }
            return await sendPostReq("/Login/LoginGetQR", payload)
        except Exception as e:
            logger.error(f"获取二维码失败: {e}")
            return None
     ```
     其中DeviceID和DeviceName随便修改一下，不要使用这个，否则会触发风控风险（疑似多人共用一台设备）
   - 启动机器人程序，CMD命令行下或者其他IDE程序中输入：`python main.py`
   - 首次登录，输入2
   - 修改机器人代码时只需关闭重启App程序即可，Redis和Wxapi保持常开即可
   - 修改代码后重启App程序，输入1，跳过登录即可，无需重复扫码

## 使用简介
### 首次使用
   - 必须配置管理员wxid，用来控制机器人
      - `App/Config/Config.toml`
   - 启动机器人程序，CMD命令行下或者其他IDE程序中输入：`python main.py`
   - 首次登录，输入2,手机扫码
   - 建一个测试群，绑定群模式，类似与白名单一类，具体口令可再`App/Plugin/Admin/config.toml`,例如发送`这群可以`，即绑定custom模式
   - 再该群进行插件初始化操作，发送`插件初始化`，后面所有custom的群都会启动对应的插件
   - 修改插件配置文件，`App/Config/plugininit.xlsx`,在此修改状态
   - 到此基本可以体验现有插件了，有问题可行解决或者进群寻求群友帮助
### 体验插件
   - 相关口令如下，可自行前往各插件的`config.toml`查看
   - 签到、热搜、早安、舔狗、菜单、点歌 黄昏、666、色色、视频、等等
### 接口对接
   - 娱乐接口：https://api.dudunas.top
   - 项目中的多数插件需要依赖dpkey，可前往上述站点进行获取或自行更换，dpkey免费获取


## 常见问题

1. ffmpeg相关错误
   - 确保ffmpeg正确安装并添加到PATH
   - Windows用户检查环境变量设置

2. 图片处理相关错误
   - 检查系统依赖是否完整安装
   - 确认Python Pillow库安装正确

3. 登录问题
   - 检查网络连接
   - 确认Login.toml配置正确
   - 查看日志文件排查具体错误
4. 缺失依赖
   - 例如`No module named 'pysilk'`，可尝试`pip install pysilk-mod==1.6.4`,如继续报错，可尝试将本项目下`Help/pysilk`文件夹复制到你的python目录下的`Lib/`下，然后尝试运行项目
## 安全建议

1. 定期更新依赖包
2. 不要将配置文件提交到版本控制系统
3. 使用环境变量存储敏感信息
4. 定期备份数据库

## 贡献指南-插件共创
0. 我为人人，人人为我，欢迎有志同僚共同开发插件
1. 关于Wxapi，避免**泛滥**导致无法使用，启动时会进行缘分鉴权，初始缘分30天，群内可续杯**介意勿用**
2. 持续*提交插件*、*介绍定制业务*、*热心帮助群友*、*打赏*等友善行为可**获得无限期延长缘分**
3. Fork Star项目
4. 创建特性分支
5. 提交更改
6. 推送到分支
7. 创建 Pull Request
8. **star项目是获得永久授权的前置条件**

## 许可证

MIT License

## 作者

大鹏

## 更新日志
### V1.0.1
- 修复已知问题
### V1.0.0
- 最新版本
- 完善插件系统
- 优化登录流程
- 增加更多API支持

## 联系方式

- 问题反馈：请提交Issue
- 功能建议：请提交Issue或PR

## 致谢

感谢所有贡献者的支持！ 
