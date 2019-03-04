#
# Main
#

# import global modules
import importlib
import init

# initialize all modules configuration options
init.init()

# dynamically load backend modules
backend_modules = init.config['DEFAULT']['BACKEND_MODULES']
backend_modules = backend_modules.split(",")
for moduleName in backend_modules:
    moduleName = moduleName.strip()
    module = importlib.import_module(
        '.' + moduleName,
        'modules.backend.' + moduleName
    )

# dynamically load command modules
command_modules = init.config['DEFAULT']['COMMAND_MODULES']
command_modules = command_modules.split(",")
for moduleName in command_modules:
    moduleName = moduleName.strip()
    module = importlib.import_module(
        '.' + moduleName,
        'modules.command.' + moduleName
    )

# config overrides
