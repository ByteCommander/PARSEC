## 02 - Specifications for custom command-modules
#### How custom commands may be defined for Parsec:

 1. **Command modules:**
    
    Command modules are just simple `*.py` Python 3 source files that contain one or more classes derived from `PARSEC.Interface.Programming.CommandBase.CommandBaseClass`.
    
    When Parsec loads such modules, it will first normally import it as standard Python module and then extract all classes defined in the first hierarchy level and derived from the appropriate base class. After that, each class will be separately passed to the command-class loading function.
    
 2. **Command classes:**
    
    Command classes are Python 3 classes derived from `PARSEC.Interface.Programming.CommandBase.CommandBaseClass`.  
    This base class defines the methods described below. Some of them must be overridden because they raise a `NotImplementedException` by default. Those methods are necessary. Others may, but don't have to be overriden to add more functionality. Those just `return True` by default.
    
    - **`CommandBaseClass`**:
        
        This is the raw base class. All methods that can be called by Parsec are defined here:

        The often used parameter `parsec_interface` is an instance of `PARSEC.Interface.Programming.CommandAPI.ParsecInterface` and is the command's only permitted way to interact with Parsec and the chat. It may not be cached, but you always have to use the instance given as argument.

        - `on_event(self, event, parsec_interface)`: **MUST override!**  
            Will be called whenever any kind of command-handleable event occurs.  
            `event` is an instance of `PARSEC.Interface.Status.EventBase.EventBaseClass`  
            You may throw a `PARSEC.Interface.Status.Exceptions.CommandRuntimeError` if the event handling failed. Parsec will log this and discard the event. All other `Exception` instances will be caught and logged and treated in the same way. Throwing an exception does not unsubscribe the instance from the event queue, so it will still receive the next events.


        - `on_init(self, parsec_interface)`: *overridable*  
            Will be called when the command class gets initialized. Can be used for initialization code that requires access to `parsec_interface`. It is therefore recommended to be preferred over `__init__(self)`.  
            You may throw a `PARSEC.Interface.Status.Exceptions.CommandInitError` if the initialization failed and the instance will not be able to handle events properly. Parsec will then abort the loading and skip this command. It will not call any method of this instance any more, not even `on_exit(...)`, so make sure you have already tidied up everything before raising that exception. All other `Exception` instances will be caught and logged and treated in the same way.
            `parsec_interface` is an instance of `PARSEC.Interface.Programming.CommandAPI.ParsecInterface`
        
        - `on_exit(self, parsec_interface)`: *overridable*  
            Will be called when the command class gets terminated. Can be used for code to tidy up that requires access to `parsec_interface`. It is therefore recommended to be preferred over `__del__(self)`.  
            You may throw a `PARSEC.Interface.Status.Exceptions.CommandExitError` if the tidying failed. Parsec will log this error as well as any other `Exception` instances and continue the program.
