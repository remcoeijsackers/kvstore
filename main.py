import cmd

from kvstore.state import context, no_transaction

state = context(no_transaction())

def handle_output(outp):
    """
    Only prints if the value is not None.
    """
    if outp:
        print(outp)

class cli(cmd.Cmd):
    """
    Handles the user input.
    """
    prompt = '(kvstore) '

    #CORE COMMANDS
    def do_GET(self, arg) -> None:
        """
        Get a value from a given key.

        Arg: Key to retrieve value from.
        """
        command = "GET " + str(arg)
        handle_output(state.get(command))

    def do_SET(self,arg) -> None: 
        """
        Store a key/ value combination.

        Arg: Key/ Value to store.
        """
        command = "SET " + str(arg)
        handle_output(state.set(command))

    def do_UNSET(self,arg) -> None:
        """
        Remove a Key/value combination.

        Arg: The key to remove.
        """
        command = "UNSET " + str(arg)
        handle_output(state.unset(command))

    def do_NUMEQUALTO(self,arg) -> None:
        """
        Return the number of keys that have the given value.

        Arg: The value to search for.
        """
        command = "NUMEQUALTO " + str(arg)
        handle_output(state.numequalto(command))

    def do_END(self,arg) -> None:
        """
        End the program.
        """
        exit()
    
    def do_BEGIN(self, arg) -> None:
        """
        Begin a transaction.
        Mutating commands (SET, UNSET) are stored until 'COMMIT' is called, then they will be excecuted. 
        State can be reverted with 'ROLLBACK'.
        """
        handle_output(state.begin())
        
    def do_COMMIT(self, arg) -> None:
        """
        Commit a transaction.
        Carry out the commands made during the transaction. 
        A transaction needs to have been started with 'BEGIN'
        """
        handle_output(state.commit())
    
    def do_ROLLBACK(self, arg) -> None:
        """
        Rollback to the beginning of the transaction.
        A transaction needs to have been started with 'BEGIN'
        """
        handle_output(state.rollback())
        
    def do_LIST(self, arg) -> None:
        """
        List the contents of the kv store.
        """
        handle_output(state.list())
        
    def default(self, line: str) -> None:
        """
        Default response when a command is unknown.
        """
        handle_output("error")

if __name__ == "__main__":
    while 1:
        cli().cmdloop()