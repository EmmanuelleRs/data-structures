from Ques_and_stacks.stack import Stack

stack = Stack()

stack.push(1)
stack.push(3)
stack.push(2)
stack.push(10)
stack.push(0)
stack.pop()
stack.push(100)
stack.pop()
stack.push(9)
stack.push(8)

def test_getMax():
    assert  stack.getMax() == 10

def test_getMin():
    assert stack.getMin() == 1

