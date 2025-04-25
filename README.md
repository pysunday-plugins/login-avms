该插件为avms登录插件, 用于登录avms平台

霸道网址: <https://teststable-avms.stg.1qianbao.com/>

**网络支持: 内网**

## 1. 安装

### 1.1 远程安装

执行安装: `sunday_install ssh://git@code.paic.com.cn:8009/yqb-travelpluginh5/car_board.git#login-avms`

### 1.2 源代码安装

克隆源代码: `git clone -b login-avms ssh://git@code.paic.com.cn:8009/yqb-travelpluginh5/car_board.git login-avms`

本地安装: `sunday_install ./login-avms`

## 2. 试玩

```python
from sunday.login.avms import Login as Avms
avms = Avms().login()
r = avms.rs.get('https://teststable-avms.stg.1qianbao.com/avms-service/queryUser')
from pydash import get, find
userList = get(r.json(), 'retData.userlist')
currentUser = find(userList, lambda item: item['userId'] == avms.user)
print(currentUser)
# {'userId': 'admin', 'userPwd': '', 'userName': '超级管理员', 'roleName': '管理员', 'roleId': '4', 'createTime': '2020-2-12 10:29:54', 'updateTime': '2020-2-12 10:29:54', 'operator': 'zhangliang548'}
```
