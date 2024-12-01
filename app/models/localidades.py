"""Localidad entity module"""
@dataclasses.dataclass
class Localidad(db.Model):
    """Localidad class"""
    __bind_key__ = DB_CONFIG.validate_bind('autogestion_prod')
    __table_args__ = {"schema": 'public'}
    __tablename__ = 'localidades'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(255), nullable=False)
    provincia_id = db.Column(db.BigInteger, db.ForeignKey('provincias.id', ondelete='CASCADE'))
    codigo_postal = db.Column(db.String(8))

    def __init__(self, descripcion: str, provincia_id: int, codigo_postal: str):
        self.descripcion = DataTransformer.nan_to_none(descripcion)
        self.provincia_id = DataTransformer.nan_to_none(provincia_id)
        self.codigo_postal = DataTransformer.nan_to_none(codigo_postal)

    def __repr__(self):
        public_attributes = {key: value for key, value in self.__dict__.items() if not key.startswith('_')}
        attributes = ', '.join(f"{key}: {value}" for key, value in public_attributes.items())
        return f"{self.__class__.__name__} -> {attributes}"
