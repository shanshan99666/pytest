# TestWebScoket
# 2022/10/14
from lib.apilib.mywebscoket import WebsocketUtil


class TestWsDemo:
    def setup(self):
        url = 'ws://echo.websocket.org'
        self.wss = WebsocketUtil()
        self.wss.conn(url)

    def teardown(self):
        self.wss.close()

    def test_demo(self):
        data = {'a': 'hello', 'b': 'world'}
        self.wss.send(data)
        res = self.wss.recv()
        assert 'hello' == res['a']

if __name__ == '__main__':
    testdemo = TestWsDemo()
    testdemo.setup()
    testdemo.test_demo()