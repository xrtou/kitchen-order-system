MIN_KITCHEN_WIDTH = 1.5   
MAX_KITCHEN_WIDTH = 10.0

MIN_KITCHEN_LENGTH = 1.5  
MAX_KITCHEN_LENGTH = 15.0


class KitchenSizeError(ValueError):
    
def validate_kitchen_size(width_m: float, length_m: float) -> None:
    
    if width_m <= 0 or length_m <= 0:
        raise KitchenSizeError("Размеры кухни должны быть положительными.")

    if not (MIN_KITCHEN_WIDTH <= width_m <= MAX_KITCHEN_WIDTH):
        raise KitchenSizeError(
            f"Ширина кухни должна быть от {MIN_KITCHEN_WIDTH} до {MAX_KITCHEN_WIDTH} м."
        )

    if not (MIN_KITCHEN_LENGTH <= length_m <= MAX_KITCHEN_LENGTH):
        raise KitchenSizeError(
            f"Длина кухни должна быть от {MIN_KITCHEN_LENGTH} до {MAX_KITCHEN_LENGTH} м."
        )


def can_create_order(width_m: float, length_m: float) -> bool:
    
    try:
        validate_kitchen_size(width_m, length_m)
        return True
    except KitchenSizeError:
        return False
