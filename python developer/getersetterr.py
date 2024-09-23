class student:
    def _init_(self):
        self._name=""
    def getname(self):
        return  self._name
    def setname(self,name):
        self._name=name



obj=student()
obj.setname("testing")
name=obj.getname()
print(name)