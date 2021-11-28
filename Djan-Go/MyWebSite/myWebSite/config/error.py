def success(data=None, message=''):
    """成功响应接口
	:param data: 返回携带数据
	:param message: 返回携带消息
	:return: 字典
	"""
    res = {
        'CODE': 200,
        'DATA': data,
        'MESSAGE': message,
    }
    return res


def fail(code, data=None, message=''):
    res = {
        'CODE': code,
        'DATA': data,
        'MESSAGE': message,
    }
    return res
