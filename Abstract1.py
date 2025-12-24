
from abc import ABC , abstractmethod

class Absclass(ABC):


    def print(self,x):
        print("passed value: ", x)
        
        
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")
class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")




tes_obj = test_class()
tes_obj.task()
tes_obj.print(100)
