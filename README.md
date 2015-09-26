# P.A.R.S.E.C.
<sub>**P**ython **A**ll-round **R**obot for the **S**tack**E**xchange **C**hat</sub>

**This project is not functioning at all yet. There's still a lot more to do than done!**

PARSEC is a modular chatbot core written in Python3 for the StackExchange network's chat sites that works as ultra-high level interface for the ChatExchange-API.   
It contains ChatExchange6 as a submodule, my personal fork of the Python2 ChatExchange API by Manishearth, rewritten to support both Python2 and Python3.

PARSEC simplifies interacting with any SE chat by encapsulating all API methods in one well-structured global object. Furthermore it provides simple hook methods that allow you to easily code an object-orientated, event-driven chatbot. You don't have to care about how to send a message, identify an user, detect commands or pings. Instead, you just activate a room and pass your callback function that handles the event together with the trigger you want to react on (message with either prefixed command, ping, reply, name mentioned or matching any RegEx; message edits; user events; room events; star events;...).  
The interface also allows you to get a bunch of information about SE users like their nicknames, network reputation, moderator status, about-me section, etc. Rooms have a lot to know as well, like their titles, descriptions, activity, and so on.

The second great tool PARSEC provides is its fabulous configuration system. It lets you to have a main configuration, but allows you to override parts of it both per room and per user it interacts with!

#### Build status:
<table>
  <tr>
    <th align=left>PARSEC:</th>
    <td><a href="https://travis-ci.org/ByteCommander/PARSEC"><!--<img src="https://travis-ci.org/ByteCommander/PARSEC.svg?branch=master" alt="Travis-CI build status of PARSEC">-->no tests available yet</a></td>
  </tr>
  <tr>
    <td align=left>ChatExchange6<br>(external dependency):</td>
    <td><a href="https://travis-ci.org/ByteCommander/ChatExchange6"><img src="https://travis-ci.org/ByteCommander/ChatExchange6.svg?branch=master" alt="Travis-CI build status of ChatExchange6"></td>
  </tr>
</table>
