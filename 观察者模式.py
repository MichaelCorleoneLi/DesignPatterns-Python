#观察者模式，参考文件：https://www.cnblogs.com/lizhitai/p/4459126.html

from abc import ABC, abstractmethod

class Publisher:
    def __init__(self, name):
        self._SubscriberList = []
        self.name = name
    def register(self, subscriber):
        if subscriber not in self._SubscriberList:
            self._SubscriberList.append(subscriber)
    def unregister(self, subscriber):
        self._SubscriberList.remove(subscriber)
    def notifyAll(self):
        for subscriber in self._SubscriberList:
            subscriber.notify(self.name)


class Subscriber(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def notify(self):
        pass

class SubscriberA(Subscriber):
    def notify(self, publisherName):
       print('我是{0},我收到了来自{1}的消息！'.format(self.name, publisherName))

if __name__ == '__main__':
    publisher = Publisher('消息源A')
    subscriber1 = SubscriberA('订阅者1')
    subscriber2 = SubscriberA('订阅者2')
    subscriber3 = SubscriberA('订阅者3')
    publisher.register(subscriber1)
    publisher.register(subscriber2)
    publisher.register(subscriber3)
    publisher.notifyAll()
