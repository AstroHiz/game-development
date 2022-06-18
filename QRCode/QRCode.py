# -*- encoding: utf-8 -*-
'''
@File    : QRCode.py
@Time    : 2022/06/18
@Author  : huangyancai@hotmail.com
@Desc    : 
'''

import pyqrcode
import pyzbar.pyzbar as pyzbar
from PIL import Image

class QRCode:
    """ QRCode类
    """
    def __init__(self, content, output_path):
        self._content = content
        self._output_path = output_path

    def create(self):
        """创建QRCode的图片"""
        qr = pyqrcode.create(self._content)
        qr.png(self._output_path, scale = 12)

    def decode(self, input_code):
        """解析QRCode的内容"""
        o = pyzbar.decode(Image.open(input_code))
        return o[0].data.decode("utf-8")

