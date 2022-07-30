import unittest
from context import store
from context import state

class TestStoreFunctions(unittest.TestCase):

    def test_string_insertion(self):
        stor = store.store()
        stor.set("1", "B")
        self.assertEqual(stor.get("1"), 'B')

    def test_int_insertion(self):
        stor = store.store()
        stor.set(1, 2)
        self.assertEqual(stor.get(1), 2)
        
    def test_int_str_insertion(self):
        stor = store.store()
        stor.set(1, "2")
        self.assertEqual(stor.get(1), "2")

    def test_str_int_insertion(self):
        stor = store.store()
        stor.set("1", 2)
        self.assertEqual(stor.get("1"), 2)

    def test_unset(self):
        stor = store.store()
        stor.set("1", 2)
        stor.unset("1")
        self.assertEqual(stor.get("1"), "NULL")

    def test_numequalto(self):
        stor = store.store()
        stor.set("1", 2)
        stor.set("2", 2)
        stor.set("3", "c")
        self.assertEqual(stor.numequalto(2), 2)

class TestStateFunctions(unittest.TestCase):

    def test_state_transition(self):
        start = state.context(state.no_transaction())
        start.begin()
        self.assertEqual(type(start._state), type(state.in_transaction()))

    def test_no_transaction_cannot_commit(self):
        start = state.context(state.no_transaction())
        test = start.commit()
        self.assertEqual(test, 'error')

    def test_in_transaction_can_commit(self):
        start = state.context(state.in_transaction())
        test = start.commit()
        self.assertEqual(test, None)

if __name__ == '__main__':
    unittest.main()