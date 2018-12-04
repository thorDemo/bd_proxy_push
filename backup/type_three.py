from mylib.https_push import https_push
from threadpool import ThreadPool, makeRequests

if __name__ == '__main__':
    pool = ThreadPool(32)
    arg = []
    for x in range(0, 32):
        arg.append('https://www.chhxdz.com/lsj')
    request = makeRequests(https_push, arg)
    [pool.putRequest(req) for req in request]
    pool.wait()
