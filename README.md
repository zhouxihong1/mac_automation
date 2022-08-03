## mac_automation
### mac automation autotest uitest base on appium2.0


`macos`上做UI自动化的公共方法,基于 `appium2.0`和 `mac2` driver的二次封装

## MAC端的环境部署(只需配置一次)
### 1. 安装Xcode环境
#### 1.1 打开 `App Store`
#### 1.2 搜索 `Xcode`
#### 1.3 等待下载完成后,打开`Xcode`
### 2. 打开Xcode,将Xcode Helper添加到辅助功能
#### 2.1 打开访达(`Finder`) —> MAC版本的资源管理器
#### 2.2 跳转到如下地址
```text
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/Library/Xcode/Agents/Xcode Helper.app
```
#### 2.3 打开屏幕左上角图标,点击系统偏好设置，点击安全性与隐私，点击隐私，点击辅助功能，点击左下角开锁按钮，输入密码解锁后，将Xcode Helper软件拖拽到添加栏中，即完成辅助功能的添加 
### 3. 配置认证辅助功能
```text
在macos的shell中,输入以下指令,并回车
automationmodetool enable-automationmode-without-authentication
```

### 4. 安装NodeJS环境
#### 4.1 正常下载NodeJS MAC版本的安装包，可以去官网下载
下载安装,安装完成后,打开mac的终端，输入npm，有命令行提示代表安装成功 
### 5. 切换npm源
#### 5.1 在终端中输入,
```text
npm install -g nrm
或者简写: npm i -g nrm
```

#### 5.2 输入 `nrm ls`，查看当前可用源, 建议选择腾讯源, 
```text
nrm use tencent
```

### 6. 安装`Appium2.0`环境
#### 6.1 在终端中输入
```text
npm i -g appium@next
```

来安装 `Appium 2.0`版本
#### 6.2 安装完成后,输入 (针对Appium 1.x无效)
`appium driver list`
会发现当前未安装`mac2`的驱动，下一步即将安装
### 7. 安装`appium-mac2-driver`驱动
#### 7.1 安装完 appium后，输入
```text
appium driver install mac2
```
等待 `mac`驱动安装完成
### 8. 安装待测软件，如xxx
#### 8.1 安装常规软件的过程不再赘述
### 9. 在应用程序中打开包内容，记住bundleId
#### 9.1 安装完软件后，打开访达，点击应用程序
#### 9.2 定位到已安装的软件，单击右键，点击显示包内容
#### 9.3 定位到 Info.plist，打开查看
#### 9.4 记住显示出来的 Bundle identifier内容

### 10. 启动 Appium2.0环境
#### 10.1 在终端中输入：
`appium`
然后回车即可启动

## Win端的环境部署
### 1. 安装Appium Inspector环境
#### 1.1 常规安装，可以上官网下载最新版：

安装或者解压后点击运行
### 2. 配置Inspector参数,连接上MACOS
#### 2.1 启动 Inspector后，选中 JSON Representation, 编辑并输入：
```json
{
  "appium:automationName": "Mac2",
  "platformName": "mac",
  "appium:bundleId": "xxx",
  "appium:noReset": true,
  "appium:newCommandTimeout": 2000
}
```

#### 2.2 在远程主机中输入正确的IP，点击 启动会话
#### 2.3 即可查看到如下页面，进行定位、封装和调试即可


## 3. 识别并记录控件,进行封装调试 TODO



## 4. 在现有框架中调试和编写用例 TODO



