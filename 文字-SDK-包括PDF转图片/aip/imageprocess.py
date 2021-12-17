# -*- coding: utf-8 -*-

"""
图像处理
"""

import re
import sys
import math
import time
from .base import AipBase
from .base import base64
from .base import json
from .base import urlencode
from .base import quote

class AipImageProcess(AipBase):

    """
    图像处理
    """

    __imageQualityEnhanceUrl = 'https://aip.baidubce.com/rest/2.0/image-process/v1/image_quality_enhance'

    __dehazeUrl = 'https://aip.baidubce.com/rest/2.0/image-process/v1/dehaze'

    __contrastEnhanceUrl = 'https://aip.baidubce.com/rest/2.0/image-process/v1/contrast_enhance'

    __colourizeUrl = 'https://aip.baidubce.com/rest/2.0/image-process/v1/colourize'

    __stretchRestoreUrl = 'https://aip.baidubce.com/rest/2.0/image-process/v1/stretch_restore'

    __styleTrans = "https://aip.baidubce.com/rest/2.0/image-process/v1/style_trans"

    __inpainting = "https://aip.baidubce.com/rest/2.0/image-process/v1/inpainting"

    __imageDefinitionEnhance = "https://aip.baidubce.com/rest/2.0/image-process/v1/image_definition_enhance"

    __selfieAnime = "https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime"

    __skySeg = "https://aip.baidubce.com/rest/2.0/image-process/v1/sky_seg"

    __colorEnhances = "https://aip.baidubce.com/rest/2.0/image-process/v1/color_enhance"


    def imageQualityEnhance(self, image, options=None):
        """
            图像无损放大
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__imageQualityEnhanceUrl, data)
    
    def dehaze(self, image, options=None):
        """
            图像去雾
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__dehazeUrl, data)
    
    def contrastEnhance(self, image, options=None):
        """
            图像对比度增强
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__contrastEnhanceUrl, data)
    
    def colourize(self, image, options=None):
        """
            黑白图像上色
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__colourizeUrl, data)
    
    def stretchRestore(self, image, options=None):
        """
            拉伸图像恢复
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__stretchRestoreUrl, data)


    def selfieAnime(self, image, options=None):
        """
            人像动漫化
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__selfieAnime, data)

    def imageDefinitionEnhance(self, image, options=None):
        """
            图像清晰度增强
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__imageDefinitionEnhance, data)

    def styleTrans(self, image, options=None):
        """
            图像风格转换
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__styleTrans, data)


    def skySeg(self, image, options=None):
        """
            天空分割
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__skySeg, data)

    def inpaintingByMask(self, image, rectangle, options=None):
        """
            图像修复
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data['rectangle'] = rectangle
        data.update(options)
        return self._request(self.__inpainting, data)

