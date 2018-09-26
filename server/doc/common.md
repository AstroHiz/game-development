### 名词解释
1. 登录服务器(LoginServer，LS)，提供登录验证、选网关等功能
2. 网关服务器(GateWay，GateServer，GW)，提供选游戏服相关功能
3. 游戏服务器（GameServer，GS），提供游戏的主要逻辑服务
4. 数据库服务器（DatabaseServer，DS），提供与数据库（mongodb）连接服务
5. 战斗服务器（BattleServer），提供战斗相关计算服务，提高游戏服承载能力
6. 中心服（GlobalServer），提供全局唯一的服务
7. 世界服（WorldMgr），与其他服务器相连，管理服务器状态等功能
8. 交易服务器（TradeServer），提供寄售中心服务
9. 机器人服务器（RobotServer），为某些玩法提供机器人逻辑支持服务

### 架构图
![image](https://github.com/AstroHiz/game/blob/master/server/doc/server.png)
