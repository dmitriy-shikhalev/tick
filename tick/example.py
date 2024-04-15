from .operator import Operator


class Sum(Operator):
    async def apply(self):
        return self.data[0][0] + self.data[0][1]

    async def reverse(self):
        pass
