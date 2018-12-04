from mylib.https_push_test import https_push
from threadpool import ThreadPool, makeRequests

if __name__ == '__main__':
    pool = ThreadPool(45)
    arg = []
    for x in range(0, 45):
        arg.append('https://bjgirls.cn')
    request = makeRequests(https_push, arg)
    [pool.putRequest(req) for req in request]
    pool.wait()
