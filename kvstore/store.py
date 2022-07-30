from operator import countOf

class store:
    """
    The store class both handles storage and mutations of the kv store. 
    """
    def __init__(self) -> None:
        self.storage = {}

    def set(self, k, v) -> dict:
        """
        Handle a SET command.

        Args: the key to retrieve the value from.
        """
        self.storage.update({k:v})
        return self.storage

    def get(self, k) -> (int or str):
        """
        Handle a GET command.

        Args: the key to retrieve the value from.
        """ 
        return self.storage.get(k,"NULL")

    def unset(self, k) -> (int or str):
        """
        Handle a UNSET command.
        Returns the value if found, else None

        Args: the key to retrieve the value from.
        """
        return self.storage.pop(k, None)

    def numequalto(self, v) -> int:
        """
        Handle a NUMEQUALTO 'scan' of the storage.
        Returns the count of values that match.

        Arg: the value to count.
        """
        values = countOf(self.storage.values(),v)
        if values == 0 :
            return countOf(self.storage.values(),int(v))
        return values
    