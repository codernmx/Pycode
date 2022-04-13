class News():
    def __init__(self,id,pushDateStr,title,summary,infoSource,sourceUrl):
        self.id = id,
        self.pushDateStr = pushDateStr
        self.title = title,
        self.summary = summary,
        self.infoSource =infoSource,
        self.sourceUrl =sourceUrl
    def c2dict(std):
        return {
            'id':std.id,
            'pushDateStr':std.pushDateStr,
            'title':std.std,
            'summary':std.summary,
            'infoSource':std.infoSource,
            'sourceUrl':std.sourceUrl
        }