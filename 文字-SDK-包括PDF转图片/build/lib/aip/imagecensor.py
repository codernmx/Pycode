# -*- coding: utf-8 -*-

import re
import sys
from .base import AipBase
from .base import base64
from .base import json
from .base import urlencode
from .base import quote


class AipImageCensor(AipBase):
    """
        Aip ImageCensor
    """

    __imageCensorUserDefinedUrl = 'https://aip.baidubce.com/rest/2.0/solution/v1/img_censor/v2/user_defined'

    __textCensorUserDefinedUrl = 'https://aip.baidubce.com/rest/2.0/solution/v1/text_censor/v2/user_defined'

    __voiceCensorUserDefinedUrl = "https://aip.baidubce.com/rest/2.0/solution/v1/voice_censor/v2/user_defined"

    __videoCensorUserDefinedUrl = "https://aip.baidubce.com/rest/2.0/solution/v1/video_censor/v2/user_defined"

    def imageCensorUserDefined(self, image):
        """
            imageCensorUserDefined
        """

        data = {}

        isUrl = image[0:4] == 'http'
        if not isUrl:
            data['image'] = base64.b64encode(image).decode()
        else:
            data['imgUrl'] = image

        return self._request(self.__imageCensorUserDefinedUrl, data)

    def textCensorUserDefined(self, text):
        """
            textCensorUserDefined
        """

        data = {}

        data['text'] = text

        return self._request(self.__textCensorUserDefinedUrl, data)

    def voiceCensorUserDefined(self, voice, fmt, options=None):
        """
            voiceCensorUserDefined
        """
        data = {}
        options = options or {}
        isUrl = voice[0:4] == 'http'
        if not isUrl:
            data['base64'] = base64.b64encode(voice).decode()
        else:
            data['url'] = voice
        data['fmt'] = fmt
        data.update(options)
        return self._request(self.__voiceCensorUserDefinedUrl, data)

    def videoCensorUserDefined(self, name, videoUrl, extId, options=None):
        """
            videoCensorUserDefined
        """
        data = {}
        options = options or {}
        data['name'] = name
        data['videoUrl'] = videoUrl
        data['extId'] = extId
        data.update(options)
        return self._request(self.__videoCensorUserDefinedUrl, data)
