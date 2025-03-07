
from pydantic import BaseModel


class InputData(BaseModel):
    asset_building_type: str
    year_financial_info: int
    iq_score: float
    building_quality: float
    O2020_W: float
    O2020_SD0001: float
    O2020_SD0002: float
    O2020_SD0003: float
    O2020_SD0004: float
    O2020_BS: float
    O2020_SD0005: float
    O2020_SD0006: float
    O2020_SD0007: float
    O2020_SD0008: float
    O2020_L: float
    O2020_SD0009: float
    O2020_SD0010: float
    O2020_SD0011: float

    def data_wrap(self):
        return [[value] for value in self.__dict__.values()]

    def get_info(self):
        return self.asset_building_type


"""    def __init__(self,values:list):
        # D'abord, créer un dictionnaire des attributs à partir des noms des champs et des valeurs.
        data_dict = dict(zip(self.__annotations__.keys(), values))
        
        # Utiliser le constructeur de BaseModel
        super().__init__(**data_dict)"""
