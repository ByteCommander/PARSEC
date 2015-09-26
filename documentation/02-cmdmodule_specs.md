## 02 - Specifications for custom command-modules
#### How custom commands may be defined for Parsec:

 1. **Command modules:**
    
    Command modules are just simple `*.py` Python 3 source files that contain one or more class definitions derived from `PARSEC.Interface.ConfigClasses.CommandModuleBaseClass`.
    
    When Parsec loads such modules, it will first normally import it as standard Python module and then extract all classes defined in the first hierarchy level and derived from the appropriate base class. After that, each class will be separately passed to the command-class processing function.
    
 2. **Command classes:**
    
    Command classes are Python 3 classes derived from `PARSEC.Interface.ConfigClasses.CommandModuleBaseClass`.  
    This base class defines the following methods and implements them to raise a `NotImplementedException`, therefore you really should make sure you override all of them.
    
    *to be continued...*
