## 01 - Main
#### How to initialize and start PARSEC:

 1. **Import the `PARSEC` module:**
    
        import PARSEC
    
 2. **Instantiate a new `Parsec` object:**

        parsec = PARSEC.Parsec()
    
 3. **Set the configuration file:**

        parsec.setConfigurationFile("/path/to/config.dat")

 4. **Add your custom user command modules to Parsec.**
    
    There are two commands for this, which may both be executed as often as needed:

     - Import an external module (or multiple modules) from a file:  
        You have to specify the exact package name, but you may use regular expressions to define patterns for matching the module names. I recommend that module names should start with `ParsecModule`, but that's not mandatory. The module has to contain one or more classes derived from `PARSEC.Interface.ConfigClasses.CommandModuleBaseClass`, which will all get loaded.

            parsec.add_module_from_file(package_name, module_pattern)
        
        `package_name` has to be a String like `"PARSEC.ModuleBuiltins"`  
        `module_pattern` has to be a String usable as regex like `"^ParsecModule.*"`
        
     - Add a locally defined class derived from `PARSEC.Interface.ConfigClasses.CommandModuleBaseClass`:

            parsec.add_module_from_class(module_class)
        
 5. **Let Parsec connect and login to the StackExchange networks:**
    
        parsec.connect()
        
    You may pass one of the following keyword-only arguments:
     - `timeout` (int, only positive values an 0): defaults to 15  
        Forces the function to abort with an error after the specified timeout in seconds.  
        Use 0 as timeout to run the connection process in a background thread and let the function return immediately without blocking (if running in foreground). To check the connecting progress and status, access the Parsec object's instance variable `connection_status` which holds a `ConnectionStatus` object defined in the module `PARSEC.Interface.StatusClasses`.
     - `on_success` (callback function, no arguments): defaults to `lambda: None`
        Will be called after all connections were successfully established and before the function returns and stops blocking (if running in foreground).
     - `on_error` (callback function, 1 argument of type `Exception`): defaults to `lambda exc: print(exc)`  
        Will be called after an error occurred during the connection process and before the function returns and stops blocking. If the callback function returns any value that converts to bool `False`, the Exception will be reraised afterwards. This implies `False`, `None` (or no return value), numeric representations of `0`, empty strings and collections, etc.
    
 6. **Start Parsec:**
    
    This will let it automatically enter the rooms that are specified to `auto_initialize` and start listening for events and handling them according to your loaded configuration. By default, this call blocks until Parsec fully exits because of the admin command `shutdown` received through a chat or the local interface (Terminal, later GUI maybe) or an incorrectable error.
    
        parsec.start()

    You can add the following keyword-only arguments to modify its behaviour:
     - `background` (bool): defaults to `False`:  
        If set to `True`, Parsec starts in an extra background thread and immediately returns after the function call.  
        The run status may always be monitored through Parsec's instance variable `run_status` which holds a `RunStatus` object defined in in the module `PARSEC.Interface.StatusClasses`.
     - `on_shutdown` (callback function, 1 argument of type PARSEC.Entities.Room): defaults to `lambda r: print("Shutdown successful after command invocation from {}.".format(r.info_string))`
        Will be called after all Parsec threads were successfully shut down and before the function returns and stops blocking (if running in foreground). The passed argument represents the room from which the `shutdown` command was executed. Note that the local interface (Terminal, later GUI maybe) also is treated as room.
     - `on_error` (callback function, 1 argument of type `Exception`): defaults to `lambda exc: print("Shutdown because of error!\n{}".format(exc))`  
        Will be called after an error occurred that may not be ignored and affects the whole Parsec system and before the function returns and stops blocking (if running in foreground). If the callback function returns any value that converts to bool `False`, the Exception will be reraised afterwards. This implies `False`, `None` (or no return value), numeric representations of `0`, empty strings and collections, etc.

 7. **Let Parsec tidy up all its remaining stuff:**
    
        parsec.tidy_up()

    This method should be called before the program ends to allow Parsec the correct termination and deinitialisation of all threads and modules, as well as flushing buffers, closing files and connections, etc.
