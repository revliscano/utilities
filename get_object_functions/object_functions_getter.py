class ObjectFunctionsGetter:
    def __init__(self, object_):
        self.object_ = object_

    def get_functions(self):
        object_attrs = self.__get_object_attrs()
        functions = [attr_name for attr_name in object_attrs
                     if self.__is_function_or_method(attr_name)]
        return functions

    def __get_object_attrs(self):
        return dir(self.object_)

    def __is_function_or_method(self, name):
        attr_name_of_type = str(self.__get_attr_type(name))
        return attr_name_of_type in ("<class 'function'>", "<class 'method'>")

    def __get_attr_type(self, name):
        actual_attr = getattr(self.object_, name)
        return type(actual_attr)


def get_object_functions(object_):
    functions = ObjectFunctionsGetter(object_).get_functions()
    return functions
