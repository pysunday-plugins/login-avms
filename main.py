# coding: utf-8
import os
from sunday.login.avms import config
from sunday.utils import mergeObj, LoginBase
from sunday.core import paths, Logger, enver, cache_name, Auth, getCurrentUser
from bs4 import BeautifulSoup

@cache_name('avms')
class Login(LoginBase):
    def __init__(self):
        self.logger = Logger('AVMS LOGIN').getLogger()
        LoginBase.__init__(self, __file__, logger=self.logger,
          pacWifi='PA_WLAN', pacUrl='http://626888.paic.com.cn')
        self.rs, self.isLogin = self.initRs(config.home)
    
    def initAuth(self):
        auth = Auth(self.getEnvPwd(), '[avms]')
        getenv = enver(self.getEnvPwd())[0]
        self.user = auth.addParams('userId', 'user', getenv('userId'), defaultValue=getCurrentUser())
        if self.isLogin: return
        if self.user == 'admin':
            # admin用户自动设置短信验证码
            auth.addParams('userPwd', value='Pingan@12qw')
            auth.addParams('code', value='123456')
        else:
            auth.addParams('userPwd', 'pwd', getenv('userPwd'), isPass=True)
            self.logger.info('获取验证码')
            getCodeUrl = config.getCode % self.user
            self.rs.get(getCodeUrl, verify=False)
            auth.addParams('code', isSave=False)
        self.auth = auth
    
    def login(self):
        self.initAuth()
        if self.isLogin:
            self.logger.info('登录成功')
            return self
        self.logger.debug('执行登录流程')
        headers = { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8' }
        req = self.rs.post(config.login, data=self.auth.getParams(), headers=headers)
        if not req.ok: raise Exception('请求失败')
        reqCode = req.json()['retCode']
        reqData = req.json()['retData']
        self.logger.info(reqData)
        if reqCode != '000000':
            raise Exception('登陆失败')
        self.isLogin = True
        self.saveCookie()
        self.logger.info('登录成功')
        return self

if __name__ == "__main__":
    login = Login()
    login.login()
