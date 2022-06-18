# -*- encoding: utf-8 -*-
'''
@File    : test.py
@Time    : 2022/06/18
@Author  : huangyancai@hotmail.com
@Desc    : 
'''

import QRCode

def Main():
    content = "https://www.baidu.com"
    output_path = "qr.png"
    qrcode = QRCode.QRCode(content, output_path)
    qrcode.create()
    print(qrcode.decode(output_path))


if __name__ == "__main__":
    Main()