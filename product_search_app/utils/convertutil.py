import sys
from datetime import datetime, timedelta
import calendar

class EntitiesConvert:
    @staticmethod
    def obj2dict(model):
        if model is None:
            return None
        return {col.name: getattr(model, col.name) for col in model.__table__.columns}

    @staticmethod
    def listobj2dict(model_list):
        if model_list is None:
            return None

        res = []
        for i in model_list:
            res.append(EntitiesConvert.obj2dict(i))
        return res


class TimeConvert:
    @staticmethod
    def ts2dt(ts, time_zone=0):
        return datetime.utcfromtimestamp(ts) + timedelta(hours=time_zone)

    @staticmethod
    def dt2ts(dt, time_zone=0):
        dt = dt - timedelta(hours=time_zone)
        return calendar.timegm(dt.utctimetuple())   

def main():
    print TimeConvert.ts2dt(1505895288)
    # print TimeConvert.dt2ts(TimeConvert.ts2dt(1505895288))


if __name__ == "__main__":
    sys.exit(main())

