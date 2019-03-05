#### 前言
在游戏开发，当接入的渠道SDK越来越多时，单独去适配各种SDK就变得不切实际，那如何解决呢？

#### 方案
1. 为了能让游戏能能够适配各种SDK，在客户端会对SDK进行抽象处理，把游戏接入SDK进行分离，暴露出接口，然后各种不同的渠道SDK实现这个框架
2. 同理，服务器为了能支持多个不同的游戏，可以对SDK管理逻辑进行抽象为微服务。但本例中，只是在游戏服中提供统一的用户登录认证及统一支付中心。

#### 举个栗子
以下给出针对常用的登录及充值的解决流程

![login](https://github.com/AstroHiz/game-development/blob/master/SDK%E6%8E%A5%E5%85%A5%E7%9A%84%E7%9B%B8%E5%85%B3%E5%A4%84%E7%90%86/media/sdk_login%20.jpg)


![pay](https://github.com/AstroHiz/game-development/blob/master/SDK%E6%8E%A5%E5%85%A5%E7%9A%84%E7%9B%B8%E5%85%B3%E5%A4%84%E7%90%86/media/sdk_pay.jpg)
