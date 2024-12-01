"""Marca entity module"""
from __future__ import annotations
import dataclasses
from services.data_transformer import DataTransformer
from config import DB_CONFIG, DB as db


@dataclasses.dataclass
class Marca(db.Model):
    """Marca class"""
    __bind_key__ = DB_CONFIG.validate_bind('autogestion_prod')
    __table_args__ = {"schema": 'public'}
    __tablename__ = 'marcas'
    id = db.Column(
        db.BigInteger, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(255), nullable=False)

    def __init__(self, descripcion: str):
        self.descripcion = DataTransformer.nan_to_none(descripcion)

    def __repr__(self):
        """String representation"""
        public_attributes = {
            key: value for key, value in self.__dict__.items() if not key.startswith('_')}
        attributes = ', '.join(
            f"{key}: {value}" for key, value in public_attributes.items()
        )
        return f"{self.__class__.__name__} -> {attributes}"
