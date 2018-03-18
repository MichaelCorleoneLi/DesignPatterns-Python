#参考文件：  https://zhuanlan.zhihu.com/p/25086524
#           http://blog.csdn.net/u010843114/article/details/47857591

from abc import ABCMeta,abstractmethod

class Receiver:
    '''命令执行者(烧烤师傅)'''
    def yangrouchuan(self):
        print('烤羊肉串')
    def jichi(self):
        print('烤鸡翅')

class Command:
    '''命令父类'''

    __metaclass__ = ABCMeta

    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def excute(self):
        pass

class yangrouchuanCommand(Command):
    def excute(self):
        self.receiver.yangrouchuan()

class jichiCommand(Command):
    def excute(self):
        self.receiver.jichi()

class Invoker:
    '''调用者'''
    def setCommand(self, command):
        self.command = command
    def excuteCommand(self):
        self.command.excute()

if __name__ == '__main__':
    receiver = Receiver()

    command = yangrouchuanCommand(receiver)
    invoker = Invoker()
    invoker.setCommand(command)
    invoker.excuteCommand()

    command = jichiCommand(receiver)
    invoker.setCommand(command)
    invoker.excuteCommand()
