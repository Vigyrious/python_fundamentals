class Catalogue:
    products = []
    def __init__(self, name):
        self.name = name


    def add_product(self, product):
        self.product = product
        Catalogue.products.append(product)


    def get_by_letter(self, first):
        return [el for el in self.products if el.startswith(first)]


    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        result += f'\n'.join(sorted(Catalogue.products))
        return result

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
