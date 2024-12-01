"""Provincia entity module"""
@dataclasses.dataclass
class Provincia(db.Model):
    """Provincia class"""
    __bind_key__ = DB_CONFIG.validate_bind('autogestion_prod')
    __table_args__ = {"schema": 'public'}
    __tablename__ = 'provincias'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(255), nullable=False)
    pais_id = db.Column(db.BigInteger, db.ForeignKey('paises.id', ondelete='CASCADE'))

    def __init__(self, descripcion: str, pais_id: int):
        self.descripcion = DataTransformer.nan_to_none(descripcion)
        self.pais_id = DataTransformer.nan_to_none(pais_id)

    def __repr__(self):
        public_attributes = {key: value for key, value in self.__dict__.items() if not key.startswith('_')}
        attributes = ', '.join(f"{key}: {value}" for key, value in public_attributes.items())
        return f"{self.__class__.__name__} -> {attributes}"
