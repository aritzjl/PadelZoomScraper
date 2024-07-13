class Store:
    def __init__(self, name: str, price: int, url: str,
                 promoCode: str, imageUrl: str) -> None:
        self.name = name
        self.price = price
        self.url = url
        self.imageUrl = imageUrl


class Paddle:
    def __init__(self, url: str) -> None:
        self.url = url
        self.slug = url.split('/')[-2]

        # Details
        self.image_url = ''
        self.name = ''
        self.brand = ''
        self.season = 0
        self.frameMaterial = ''
        self.surfaceMaterial = ''
        self.rubberMaterial = ''
        self.touch = ''
        self.shape = ''
        self.weight = ''

        # Statistics
        self.total = 0
        self.power = 0
        self.control = 0
        self.output = 0
        self.maneuverability = 0
        self.sweetSpot = 0

        # Prices
        self.originalPrice = 0
        self.bestPrice = 0
        self.discountPercentage = 0
        # self.stores = []

    def __str__(self) -> str:
        return f'{self.name} - {self.originalPrice}€'

    """def addStore(self, store: Store) -> None:
        self.stores.append(store)"""
