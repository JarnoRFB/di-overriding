class Component:
    def __init__(self, param):
        if param is None:
            raise ValueError()
        self.param = param

    def __str__(self):
        return f"param={self.param}"


class AllCaps(Component):

    def __str__(self):
        return f"param={str(self.param).upper()}"
