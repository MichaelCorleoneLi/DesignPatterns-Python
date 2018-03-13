#参考资料：https://www.cnblogs.com/huchong/p/8244279.html
#https://www.jianshu.com/p/ec6589e02e2f

class Singleton():
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    print(s1)
    print(s2)
