#!/usr/bin/env python3
import pyotp
import os
import traceback
from settings import BASE_DIR
from qrcode import QRCode, constants


def get_qrcode(secret_key, username):
    dirpath = os.path.join(BASE_DIR, 'static', 'image', 'qrcode')

    data = pyotp.totp.TOTP(secret_key).provisioning_uri(
        username, issuer_name="opspo")
    qr = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=6,
        border=4
    )
    try:
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        filename = str(username)+ "-" + str(secret_key) + '.png'
        filepath = str(dirpath) + str(os.sep) + filename
        print('filepath: ', filepath)
        # 保存二维码
        img.save(filepath)
        return filename
    except Exception as e:
        traceback.print_exc()
        return None


def verify_mfa(secret_key, verifycode):
    t = pyotp.TOTP(secret_key)
    # 对输入验证码进行校验，正确返回 True
    result = t.verify(verifycode)
    print(result)
    return result
