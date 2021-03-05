class Element:
    name = None
    state = None

    def __init__(self, name=None, state=None):
        self.name = name
        self.state = state

    def sum(a, b):
        return a + b

elemento = Element('nome', 'active')
