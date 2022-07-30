from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
from kvstore.store import store

kvstore = store() 

class context:
    """
    Defines the functions of the subclasses, maintains a referenc to the state it is in.
    """
    _state = None

    def __init__(self, state: state) -> None:
        self.transition_to(state)

    def transition_to(self, state: state) -> None:
        """
        Switch states. the current state defines the behaviour of the methods.
        """
        self._state = state
        self._state.commands = []
        self._state.context = self
       
    def begin(self):
        """
        Transition to in_transaction state if not already in that state.
        """
        return self._state.begin()

    def commit(self):
        """
        Make the changes since the beginning of the transaction permanent, and close the transaction.
        Return 'error' if not in a transaction.
        """
        return self._state.commit()

    def set(self, command):
        """
        Save a key value combo to the store if not in a transaction.
        """
        return self._state.set(command)

    def unset(self, command):
        """
        Remove a key value combo from the store if not in a transaction.
        """
        return self._state.unset(command)

    def get(self, command):
        """
        Get a value based on key from the store.
        """
        return self._state.get(command)

    def rollback(self):
        """
        Revert back to the beginning of the transaction, and close it.
        If not in a transaction, return 'error'
        """
        return self._state.rollback()

    def numequalto(self, command):
        """
        Return the number of keys that have the given value.
        """
        return self._state.numequalto(command)

    def list(self):
        """
        Return the contents of the store.
        """
        return self._state.list()


class state(ABC):
    
    """
    Defines the methods all subclasses (the 'states' of the machine) need to implement.
    """

    @property
    def context(self) -> context:
        return self._context

    @context.setter
    def context(self, context: context) -> None:
        self._context = context

    @abstractmethod
    def begin(self) -> str:
        pass

    @abstractmethod
    def commit(self) -> str:
        pass

    @abstractmethod
    def set(self, command) -> None:
        pass

    @abstractmethod
    def unset(self, command) -> None:
        pass

    @abstractmethod
    def get(self, command) -> str:
        pass

    @abstractmethod
    def rollback(self) -> str or None:
        pass

    @abstractmethod
    def numequalto(self) -> str:
        pass

    @abstractmethod
    def list(self) -> dict:
        pass

class in_transaction(state):
    """
    The behaviour the program should have when in a transaction. 
    Mutations are not caried out directly, but stored until a 'commit' has taken place.
    Information requests (i.e. 'get') are caried out directly.
    """

    def begin(self) -> str:
        return "Already in a transaction"

    def commit(self) -> list:
        for i in self.commands:
            if str(i).split(" ")[0] == "SET":
                c,k,v = str(i).split(" ")
                kvstore.set(k,v )
            if str(i).split(" ")[0] == "UNSET":
                kvstore.unset(str(i).split(" ")[1])
        return self.context.transition_to(no_transaction())

    def rollback(self) -> None:
        self.context.transition_to(no_transaction())

    def set(self,command) -> None:
        self.commands.append(command)

    def unset(self,command) -> None:
        self.commands.append(command)
    
    def get(self,command) -> Any:
        c,k = str(command).split(" ")
        return kvstore.get(k)

    def numequalto(self, command) -> str:
        c,v = str(command).split(" ")
        return kvstore.numequalto(v)

    def list(self) -> dict:
        return kvstore.storage

class no_transaction(state):
    """
    The default behaviour the program should have when not in a transaction 
    Mutations are caried out directly, information requests (i.e. 'get') are caried out directly.
    """

    def begin(self) -> None:
        return self.context.transition_to(in_transaction())

    def commit(self) -> str:
        return "error"
        
    def rollback(self) -> str:
        return "error"

    def set(self,command) -> None:
        c,k,v = str(command).split(" ")
        kvstore.set(k,v)

    def unset(self,command) -> None:
        c,k = str(command).split(" ")
        kvstore.unset(k)

    def get(self,command) -> Any:
        c,k = str(command).split(" ")
        return kvstore.get(k)

    def numequalto(self, command) -> str:
        c,v = str(command).split(" ")
        return kvstore.numequalto(v)

    def list(self) -> dict:
        return kvstore.storage


