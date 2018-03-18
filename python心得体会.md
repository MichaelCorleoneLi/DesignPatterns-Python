# Python心得体会
在用python实现23种设计模式时，对python有了更深的了解，记录如下：

## 1. 继承object  
3.x版本之后，定义类时不需要显式继承object；

## 2. 子类要实现__init__函数 
如果子类和父类都实现了__init__函数，则子类需要显式调用父类的构造函数，不然父类的构造函数就不会被执行。      参考“https://www.cnblogs.com/nerrissa/articles/5607291.html”
c#不同，会自动调用父类的构造函数。
python调用父类构造函数有两种方法：Father.__init__(self) 和 super(Son, self).__init__(),两种方法区别详见“https://www.zhihu.com/question/20040039/answer/57883315”，使用时规范参考“Python中既然可以直接通过父类名调用父类方法为什么还会存在super函数？ - 松鼠奥利奥的回答 - 知乎
https://www.zhihu.com/question/20040039/answer/13772641”

## 3.  @abstractmethod
python没有接口类(interface)和抽象类(abstract)，因此如果需要约束子类必须实现父类方法，需要在父类方法前加上@abstractmethod
***子类方法的参数列表可以和父类不同，但名字必须一样***
参考“http://blog.csdn.net/xiemanr/article/details/72629164”

## 4. 类普通方法、@staticmethod、@classmethod三者的区别：
* 普通方法，需要类的实例去调用；
* staticmethod，可以用类直接去调用，类似c#的static方法；
* classmethod，参数列表(cls,...)的第一个参数cls代表类自身，其实这用staticmethod也可以实现，但涉及到继承时，cls可以智能地代表当前子类，但如果用staticmethod只能采用硬编码。classmethod的出现也许是为了解决这个问题。
参考“Python 中的 classmethod 和 staticmethod 有什么具体用途？ - bravez的回答 - 知乎
https://www.zhihu.com/question/20021164/answer/64413438”

## 5. methclass
参考“https://zhuanlan.zhihu.com/p/23887627”
廖雪峰python教程

