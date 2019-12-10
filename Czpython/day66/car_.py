#使用类和实例
#修改实例属性，1，直接修改实例的属性 2，通过编写方法以特定的方式进行修改

#Car类
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' +self.make + ' ' +self.model
        return long_name.title()
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

#为了是这个类更有趣，下面给它添加一个随时间变化的属性，它存储在汽车的总里程中
#给属性指定默认值，类中每个属性都必须有初始值，哪怕这个值是0或空字符串。若在方法__init()__中给属性指定默认值，就无需包含为它提供初始值的形参
class Carplus():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading =0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' +self.make + ' ' +self.model
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Carplus('audi','a4',2016)
my_new_car.read_odometer()

#修改属性的值
#3种方法修改属性的值: 直接通过实例进行修改；通过方法设置；通过方法进行递增（增加特定的值）.

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

