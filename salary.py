"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        """
        初始化方法

        :param name: 姓名
        """
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        """
        获得月薪

        :return: 月薪
        """
        pass


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self._working_hour =working_hour


    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return 150.0 * self._working_hour


class Salesman(Employee):
    """销售员"""
    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales =sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self,sales):
        self._sales = sales if sales>0 else 0

    def get_salary(self):
        return 1200.0 + self._sales *0.05

def main():
    emps =[Manager('miya'), Programmer('nana'), Salesman("wanwan")]
    for people in emps:
        if isinstance(people, Programmer):
            people.working_hour = int(input('hallo %s, bitte die arbeitszeit eigebn:'% people.name))
        elif isinstance(people, Salesman):
            people.sales = float(input('hallo %s, bitte deinen Umsatz eingeben: '%people.name))
        print('das Gehalt von %s ist %.1f.'%(people.name, people.get_salary()))


if __name__ == '__main__':
    main()