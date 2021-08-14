import inspect

class F:
    def func(self,a,b,c,d=1,e=3):
        print(a,b,c,d,e)

aa=inspect.signature(F.func).parameters

for _,parameter in aa.items():
    print(parameter.name,parameter.default)

def smart_wrapper(func):
    def wrapper(*args,**kwargs):
        smart_parameter={}
        func_parameters=inspect.signature(func).parameters.items()
        parameter_list=[ name
            for name,value in func_parameters if value is inspect._empty and name != 'self'
        ]
