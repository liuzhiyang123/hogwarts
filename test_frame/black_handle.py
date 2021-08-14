import inspect


def black_handle(timeout=3):
    def _wrapper(func):
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                for loc in self.black_list:
                    ele=self.finds(loc,timeout=timeout)
                    ele[0].click() if ele else ''
                    return func(self,*args,**kwargs)
        return wrapper
    return _wrapper