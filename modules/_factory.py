import types
import sys


schema = [
    {
        'name': 'Module1',
        'classes': [
            {'name': 'Class1'},
            {'name': 'Class2'},
            {'name': 'Class3'}
        ]
    },
    {
        'name': 'Module2',
        'classes': [
            {'name': 'Class4'},
            {'name': 'Class5'},
            {'name': 'Class6'},
        ]
    },
]


def init_module_factory():
    py_modules = dict()
    for name in set([m['name'] for m in schema]):
        py_modules[name] = types.ModuleType(str(name.encode('UTF-8')))

    for name, py_module in py_modules.items():
        sys.modules['modules.' + name] = py_module

    add_classes(py_modules)

    return py_modules


def add_classes(py_modules):

    for m in schema:
        module_name = m['name']
        for class_dict in m['classes']:
            class_name = class_dict['name']
            klass = create_class(class_name, module_name)
            setattr(py_modules[module_name], class_name, klass)


def create_class(class_name, module_name):
    c = type(class_name, (object, ), dict(attribute1=None, __doc__=class_name))
    c.__module__ = 'modules.{}'.format(module_name)
    return c
