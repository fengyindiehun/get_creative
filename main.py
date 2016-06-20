#! /usr/local/bin/python
#coding=utf-8

from flask import Flask
from flask import request
from redis_proxy import RedisProxy

app = Flask(__name__)
redis = RedisProxy(host='10.79.40.121', port='6379',
                   socket_timeout=1000,
                   socket_connect_timeout=1000)

@app.route('/get', methods=['GET', 'POST'])
def get():
    feed_id = ''
    cust_id = ''
    if request.method == 'POST':
        feed_id = request.form.get('feedId').encode('utf-8')
        cust_id = request.form.get('custId').encode('utf-8')
    else:
        feed_id = request.args.get('feedId').encode('utf-8')
        cust_id = request.args.get('custId').encode('utf-8')

    return redis.get(feed_id, cust_id)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
