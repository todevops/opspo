#!/usr/bin/env python3

import os

# 获取随机密钥，存于用户表中，随机64位
# cat /dev/urandom | base64 | tr -Cd A-Za-z0-9 | head -c 64; echo
secret_key = "GCMLJXIECYZMPQREJRHRFUUERRIPOXYIHQBMBCMOIIAJFWLZUMFJZIIWKLTVDHJT"
# qrcode = get_qrcode(secret_key, 'jeremy')

# verifycode = input()
# verify_mfa(secret_key, verifycode)

BASE_DIR = os.path.dirname(__file__)
debug = True
xsrf_cookies = False
expire_seconds = 365 * 24 * 60 * 60
cookie_secret = '61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2X6TP1o/Vo='

# 这是写库，
DB_HOST = os.getenv('DB_HOST', '172.16.0.223')  # 修改
DB_PORT = os.getenv('DB_PORT', '3306')  # 修改
DB_USER = os.getenv('DB_USER', 'root')  # 修改
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')  # 修改
DB_NAME = os.getenv('DB_NAME', 'cmdb')  # 默认

# 这是Redis配置信息，默认情况下和codo-admin里面的配置一致
REDIS_HOST = os.getenv('REDIS_HOST', '172.16.0.223')  # 修改
REDIS_PORT = os.getenv('REDIS_PORT', '6379')  # 修改
REDIS_DB = 8
REDIS_AUTH = True
REDIS_CHARSET = 'utf-8'
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', 'cWCVKJ7ZHAK122VbivUf')  # 修改


# Aws Events 事件邮件通知人
AWS_EVENT_TO_EMAIL = '1111@qq.com,2222@gmail.com'

# SSH公钥,获取资产使用，一般都是机器默认路径,建议不要修改
PUBLIC_KEY = '/root/.ssh/id_rsa.pub'  # 默认

# Web Terminal 地址，请填写你部署的webterminal地址
WEB_TERMINAL = 'http://1.1.1.1:8080'


settings = dict(
    debug=debug,
    xsrf_cookies=xsrf_cookies,
    cookie_secret=cookie_secret,
    expire_seconds=expire_seconds,
    app_name='opspo',
    databases={
        "DB_HOST_KEY": DB_HOST,
        "DB_PORT_KEY": DB_PORT,
        "DB_USER_KEY": DB_USER,
        "DB_PASSWORD_KEY": DB_PASSWORD,
        "DB_NAME_KEY": DB_NAME,
    },
    redises={
        "RD_HOST_KEY": REDIS_HOST,
        "RD_PORT_KEY": REDIS_PORT,
        "RD_DB_KEY": REDIS_DB,
        "RD_AUTH_KEY": REDIS_AUTH,
        "RD_CHARSET_KEY": REDIS_CHARSET,
        "RD_PASSWORD_KEY": REDIS_PASSWORD
    }
)
