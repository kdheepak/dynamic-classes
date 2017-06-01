from ._factory import init_module_factory as __init_module_factory

_modules = __init_module_factory()

for _name, module in _modules.items():
    globals()[_name] = module
