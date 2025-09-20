class BaseChai:
    def __init__(self,type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai...")


class MasalaChai(BaseChai):
    def __init__(self, type_):
        self.type = type_
    def add_spices(self,type_):
        print(f"Adding cardamom, giger, cloves.{type_}")


class ChaiShop:
    chai_cls = BaseChai
    def __init__(self):
        self.chai = self.chai_cls("Elychi")

    def server(self):
        print(f"Serving {self.chai.type}")


class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai
    # pass


shop = ChaiShop()
fancy = FancyChaiShop()

fancy.server()
shop.server()
fancy.chai.add_spices("ginger")
    