from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinate:
    lon: float
    lat: float

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not (-180 <= self.lon <= 180 and -90 <= self.lat <= 90):
            raise ValueError('invalid coordinate')
