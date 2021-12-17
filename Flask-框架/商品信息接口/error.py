from enum import IntEnum


class Error(IntEnum):
    # 请求成功
    OK = 200

    # 未授权
    NOT_AUTHORIZATION = 1000

    # 缺少token
    MISS_TOKEN = 1010

    # 过期token
    EXPIRED_TOKEN = 1011

    # 无效token
    INVALID_TOKEN = 1012

    # 注册过期
    REGISTER_TIMEOUT = 1013

    # 缺少参数
    MISS_PARAMETER = 1020

    # 无效参数
    INVALID_PARAMETER = 1021

    # 空资源
    EMPTY_RESOURCE = 1030

    # 无权限
    FORBIDDEN = 9000

    # 未找到
    NOT_FOUND = 9010

    # 内部错误
    INTERNAL_ERROR = 9020

    # 未知异常
    UNEXPECTED = 9999


def success(data=None, message=''):
    """成功响应接口
    :param data: 返回携带数据
    :param message: 返回携带消息
    :return: 字典
    """
    res = {
        'code': Error.OK,
        'data': data,
        'message': message,
    }
    return res


def fail(code, data=None, message=''):
    """失败响应接口
    :param code: 必需参数，错误代码Error的属性值
    :param data: 返回携带数据
    :param message: 返回携带消息
    :return: 字典
    """
    res = {
        'code': code,
        'data': data,
        'message': message,
    }
    return res
