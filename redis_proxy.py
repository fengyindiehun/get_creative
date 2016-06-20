import json
import redis

class RedisProxy(object):

    feed_info_keys=['creative_type', 'cust_id', 'tag', 'text']
    cust_info_keys=['cust_type']

    def __init__(self, host, port, socket_timeout, socket_connect_timeout):
        self.host = host
        self.port = port
        self.socket_timeout = socket_timeout
        self.socket_connect_timeout = socket_connect_timeout
        self.connect()

    def connect(self):
        self.r = redis.StrictRedis(host=self.host, port=self.port,
                                   socket_timeout=self.socket_timeout,
                                   socket_connect_timeout=self.socket_connect_timeout)

    def get(self, feed_id, cust_id):
        print feed_id, cust_id
        try:
            feed_info = self.r.get('objectinfo_mid_' + feed_id)
            cust_info = self.r.get('objectinfo_custid_' + cust_id)
            return json.dumps(dict(feed_info=dict(zip(RedisProxy.feed_info_keys , feed_info.split(':'))),
                                  cust_info=dict(zip(RedisProxy.cust_info_keys, cust_info.split(':')))))
        except Exception as e:
            return 'Get error: {0}'.format(e.message)
