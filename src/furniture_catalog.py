class Material:
    def __init__(self, code: str, name: str, price_per_m2: float, is_kitchen_safe: bool = True):
        self.code = code              
        self.name = name              
        self.price_per_m2 = price_per_m2
        self.is_kitchen_safe = is_kitchen_safe

    def __repr__(self) -> str:
        return f"<Material {self.code} ({self.name}), {self.price_per_m2} RUB/m2>"

class MaterialCatalog:
    def __init__(self):
        self._materials = {}

    def add_material(self, material: Material) -> None:
        if material.code in self._materials:
            raise ValueError(f"Material with code '{material.code}' already exists in catalog")
        self._materials[material.code] = material

    def get_material(self, code: str) -> Material | None:
        return self._materials.get(code)

    def list_materials(self) -> list[Material]:
        return list(self._materials.values())
