class InfectedPerson():
    def __init__(self, id,privince,city,confirmedCount,suspectedCount,curedCount,deadCount):
        self.id = id
        self.privince = privince
        self.city = city
        self.confirmedCount = confirmedCount
        self.suspectedCount = suspectedCount
        self.curedCount = curedCount
        self.deadCount = deadCount
    def infp2dict(std):
        return {
            'id':std.id,
            'privince': std.privince,
            'city':std.city,
            'confirmedCount': std.confirmedCount,
            'suspectedCount': std.suspectedCount,
            'curedCount': std.curedCount,
            'deadCount': std.deadCount,
        }
