#PARSEC API documentation

**Work in progress!**

Note that this documentation was written *before* the actual implementation, so it does not describe the current state of the project, but the aimed interface. 

## 1. Initialization:

 1. Import the `PARSEC` module:
    
        import PARSEC
    
 2. Instantiate a new `Parsec` object and set the configuration file.  
    Passing the config file name directly to the constructor is optional, you can also set it separately:
 
        parsec = PARSEC.Parsec("/path/to/config.dat")
        
    or:
        
        parsec = PARSEC.Parsec()
        parsec.setConfigurationFile("/path/to/config.dat")

 3. Add your custom user command modules to Parsec. There are two commands for this, which may both be executed as often as needed:
     - Import an external module (or multiple modules) from a file:  
        You have to specify the exact package name, but you may use regular expressions to define patterns for matching the module names. I recommend that module names should start with `ParsecModule`, but that's not mandatory. The module has to contain one or more classes derived from `PARSEC.Interface.ConfigClasses.CommandModuleBaseClass`, which will all get loaded.

            parsec.add_module_from_file(package_name, module_pattern)
        
        `package_name` has to be a String like `"PARSEC.ModuleBuiltins"`  
        `module_pattern` has to be a String usable as regex like `"^ParsecModule.*"`
        
     - Add a locally defined class derived from `PARSEC.Interface.ConfigClasses.CommandModuleBaseClass`:

            parsec.add_module_from_class(module_class)
        
 4. Let Parsec connect and log into the StackExchange networks specified in the configuration:
    
        parsec.connect()
        
    You may pass one of the following keyword-only arguments:
     - `timeout` (int, only positive values an 0): defaults to 15  
        Forces the function to abort with an error after the specified timeout in seconds.  
        Use 0 as timeout to run the connection process in a background thread and let the function return immediately without blocking (if running in foreground). To check the connecting progress and status, access the Parsec object's instance variable `connection_status` which holds a `ConnectionStatus` object defined in the module `PARSEC.Interface.StatusClasses`.
     - `on_success` (callback function, no arguments): defaults to `lambda: None`
        Will be called after all connections were successfully established and before the function returns and stops blocking (if running in foreground).
     - `on_error` (callback function, 1 argument of type `Exception`): defaults to `lambda exc: print(exc)`  
        Will be called after an error occurred during the connection process and before the function returns and stops blocking. If the callback function returns any value that converts to bool `False`, the Exception will be reraised afterwards. This implies `False`, `None` (or no return value), numeric representations of `0`, empty strings and collections, etc.
    
 5. Start Parsec. This will let it automatically enter the rooms that are specified to `auto_initialize` and start listening for events and handling them according to your loaded configuration. By default, this call blocks until Parsec fully exits because of the admin command `shutdown` received through a chat, an incorrectable error or a `shutdown` command from the local interface (Terminal, later GUI maybe).
    
        parsec.start()

    You can add the following keyword-only arguments to modify its behaviour:
     - `background` (bool): defaults to `False`:  
        If set to `True`, Parsec starts in an extra background thread and immediately returns after the function call.  
        The run status may always be monitored through Parsec's instance variable `run_status` which holds a `RunStatus` object defined in in the module `PARSEC.Interface.StatusClasses`.
     - `on_shutdown` (callback function, 1 argument of type PARSEC.Entities.Room): defaults to `lambda r: print("Shutdown successful after command invocation from {}.".format(r.info_string))`
        Will be called after all Parsec threads were successfully shut down and before the function returns and stops blocking (if running in foreground). The passed argument represents the room from which the `shutdown` command was executed. Note that the local interface (Terminal, later GUI maybe) also is treated as room.
     - `on_error` (callback function, 1 argument of type `Exception`): defaults to `lambda exc: print("Shutdown because of error!\n{}".format(exc))`  
        Will be called after an error occurred that may not be ignored and affects the whole Parsec system and before the function returns and stops blocking (if running in foreground). If the callback function returns any value that converts to bool `False`, the Exception will be reraised afterwards. This implies `False`, `None` (or no return value), numeric representations of `0`, empty strings and collections, etc.
