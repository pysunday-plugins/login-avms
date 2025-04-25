# coding: utf-8

__all__ = ['login', 'home', 'uploadFiles', 'getCode']

baseUrl = 'https://teststable-avms.stg.1qianbao.com/avms-service'

# 登录接口
login = '{}/login'.format(baseUrl)

# 首页
home = '{}/plugin'.format(baseUrl)

# 上传图片
uploadFiles = '{}/uploadFiles?filePath=plugin'.format(baseUrl)

# 短信验证码
getCode = '{}/getVerificationCode?userUm=%s'.format(baseUrl)
