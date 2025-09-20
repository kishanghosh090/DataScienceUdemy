class ChaiOrder:
    def __init__(self,type_,sweetness,size):
        self.type = type_
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls,order_data):
        return cls(
            order_data["type_"],
            order_data["sweetness"],
            order_data["size"]
        )        
    @classmethod
    def from_string(cls,order_str):
        type_,sweetness,size = order_str.split("-")

        return cls(
            type_,
            sweetness,
            size
        )


o1 = ChaiOrder.from_dict({
    "type_": "elychi",
    "sweetness": "mid",
    "size": "large"
})

o2 = ChaiOrder.from_string("ginger-low-small")

print(o1.__dict__)