
# -*- coding: utf-8 -*-

"""
图像识别
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
class AipImageClassify(AipBase):

    """
    图像识别
    """

    __advancedGeneralUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general'

    __dishDetectUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/dish'

    __carDetectUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/car'

    __vehicleDetectUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect'

    __vehicleDamageUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_damage'

    __logoSearchUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/logo'

    __logoAddUrl = 'https://aip.baidubce.com/rest/2.0/realtime_search/v1/logo/add'

    __logoDeleteUrl = 'https://aip.baidubce.com/rest/2.0/realtime_search/v1/logo/delete'

    __animalDetectUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/animal'

    __plantDetectUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/plant'

    __objectDetectUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/object_detect'

    __landmarkUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/landmark'

    __flowerUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/flower'

    __ingredientUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/classify/ingredient'

    __redwineUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/redwine'


    __currencyUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/currency'

    __customDishAddUrl = "https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/dish/add"

    __customDishSearchUrl = "https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/dish/search"

    __customDishDeleteUrl = "https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/dish/delete"

    __multiObjectDetectUrl = "https://aip.baidubce.com/rest/2.0/image-classify/v1/multi_object_detect"

    __combinationUrl = "https://aip.baidubce.com/api/v1/solution/direct/imagerecognition/combination"

    __vehicle_attrUrl = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_attr"

    __vehicle_detect_highUrl = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect_high"

    __traffic_flowUrl = "https://aip.baidubce.com/rest/2.0/image-classify/v1/traffic_flow"


    def advancedGeneral(self, image, options=None):
        """
            通用物体识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__advancedGeneralUrl, data)

    def dishDetect(self, image, options=None):
        """
            菜品识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__dishDetectUrl, data)

    def carDetect(self, image, options=None):
        """
            车辆识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__carDetectUrl, data)

    def vehicleDetect(self, image, options=None):
        """
            车辆检测
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__vehicleDetectUrl, data)

    def vehicleDamage(self, image, options=None):
        """
            车辆外观损伤识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__vehicleDamageUrl, data)

    def logoSearch(self, image, options=None):
        """
            logo商标识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__logoSearchUrl, data)

    def logoAdd(self, image, brief, options=None):
        """
            logo商标识别—添加
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()
        data['brief'] = brief

        data.update(options)

        return self._request(self.__logoAddUrl, data)

    def logoDeleteByImage(self, image, options=None):
        """
            logo商标识别—删除
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__logoDeleteUrl, data)

    def logoDeleteBySign(self, cont_sign, options=None):
        """
            logo商标识别—删除
        """
        options = options or {}

        data = {}
        data['cont_sign'] = cont_sign

        data.update(options)

        return self._request(self.__logoDeleteUrl, data)

    def animalDetect(self, image, options=None):
        """
            动物识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__animalDetectUrl, data)

    def plantDetect(self, image, options=None):
        """
            植物识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__plantDetectUrl, data)

    def objectDetect(self, image, options=None):
        """
            图像主体检测
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__objectDetectUrl, data)

    def landmark(self, image, options=None):
        """
            地标识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__landmarkUrl, data)

    def flower(self, image, options=None):
        """
            花卉识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__flowerUrl, data)

    def ingredient(self, image, options=None):
        """
            果蔬识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__ingredientUrl, data)

    def redwine(self, image, options=None):
        """
            红酒识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__redwineUrl, data)

    def currency(self, image, options=None):
        """
            货币识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode()

        data.update(options)

        return self._request(self.__currencyUrl, data)


    def customDishesAddImage(self, image, brief, options=None):
        """
            自定义菜品识别—入库
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data['brief'] = brief
        data.update(options)
        return self._request(self.__customDishAddUrl, data)

    def customDishesSearch(self, image, options=None):
        """
            自定义菜品识别—检索
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__customDishSearchUrl, data)

    def customDishesDeleteImage(self, image, options=None):
        """
            自定义菜品识别—删除
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__customDishDeleteUrl, data)

    def customDishesDeleteContSign(self, cont_sign, options=None):
        """
            自定义菜品识别—删除
        """
        options = options or {}
        data = {}
        data['cont_sign'] = cont_sign
        data.update(options)
        return self._request(self.__customDishDeleteUrl, data)


    def multiObjectDetect(self, image, options=None):
        """
            图像多主体检测
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data.update(options)
        return self._request(self.__multiObjectDetectUrl, data)


    def combinationByImage(self, image, scenes, options=None):
        """
        组合接口-image
        """
        options = options or {}
        data = {}
        data['image'] = base64.b64encode(image).decode()
        data['scenes'] = scenes
        data.update(options)
        return self._request(self.__combinationUrl, json.dumps(data, ensure_ascii=False),
                             {'Content-Type': 'application/json;charset=utf-8'})


    def combinationByImageUrl(self, imageUrl, scenes, options=None):
        """
        组合接口-imageUrl
        """
        options = options or {}
        data = {}
        data['imgUrl'] = imageUrl
        data['scenes'] = scenes
        data.update(options)
        return self._request(self.__combinationUrl, json.dumps(data, ensure_ascii=False),
                             {'Content-Type': 'application/json;charset=utf-8'})



    def vehicleAttr(self, image, options=None):
        """
            车辆属性识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode();

        data.update(options)

        return self._request(self.__vehicle_attrUrl, data)


    def vehicleAttrUrl(self, url, options=None):
        """
            车辆属性识别
        """
        options = options or {}

        data = {}
        data['url'] = url
        data.update(options)

        return self._request(self.__vehicle_attrUrl, data)


    def vehicleDetectHigh(self, image, options=None):
        """
            车辆检测-高空版
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode();

        data.update(options)

        return self._request(self.__vehicle_detect_highUrl, data)



    def vehicleDetectHighUrl(self, url, options=None):
        """
            车辆检测-高空版
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__vehicle_detect_highUrl, data)



    def trafficFlow(self, image, case_id, case_init, area, options=None):
        """
            车流统计
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image).decode();
        data['case_id'] = case_id
        data['case_init'] = case_init
        data['area'] = area

        data.update(options)

        return self._request(self.__traffic_flowUrl, data)



    def trafficFlowUrl(self, url, case_id, case_init, area, options=None):
        """
            车流统计
        """
        options = options or {}

        data = {}
        data['url'] = url
        data['case_id'] = case_id
        data['case_init'] = case_init
        data['area'] = area

        data.update(options)

        return self._request(self.__traffic_flowUrl, data)



    def carDetectUrl(self, url, options=None):
        """
            车型识别
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__car_detectUrl, data)



    def vehicleDetectUrl(self, url, options=None):
        """
            车辆检测
        """
        options = options or {}

        data = {}
        data['url'] = url

        data.update(options)

        return self._request(self.__vehicle_detectUrl, data)



