import unittest

from main import VM, load_bytecode


class VMTestCase(unittest.TestCase):
    def test_1_bytecode_file(self):
        # [5]
        vm = VM()
        bytes = load_bytecode('bytecode_1.vm')
        vm.perform_actions(bytes)
        self.assertEqual(vm._stack, [5])

    def test_2_bytecode_file(self):
        # [23, 68]
        vm = VM()
        bytes = load_bytecode('bytecode_2.vm')
        vm.perform_actions(bytes)
        self.assertEqual(vm._stack, [23, 68])


    def test_3_bytecode_file(self):
        # [22, 33, 46]
        vm = VM()
        bytes = load_bytecode('bytecode_3.vm')
        vm.perform_actions(bytes)
        self.assertEqual(vm._stack, [22, 33, 46])


if __name__ == '__main__':
    unittest.main()
