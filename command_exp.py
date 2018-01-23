class Command_Exp:
    TYPES=["skip","assign"]
    def __init__(self,function_to_execute,representation,type):
        self.to_execute=function_to_execute
        self.representation=representation
        if type in Command_Exp.TYPES:
            self.type=type

    def execute(self,variables):
        return self.to_execute(variables)


    def __repr__(self):
        return self.representation

if __name__=="__main__":
    def fun1(variables):
        variables['X']=variables['X']-variables['Y']
        return variables

    C=Command_Exp(fun1,"X:=X-Y")

    print({'X':3,'Y':2})
    print(C.execute({'X':3,'Y':2}))
    print(C)