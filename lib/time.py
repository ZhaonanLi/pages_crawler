import datetime


class Time(object):
    @staticmethod
    def get_current_utc_datetime():
        return datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
