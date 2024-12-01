"""Patentamiento entity module"""
@dataclasses.dataclass
class Patentamiento(db.Model):
    """Patentamiento class"""
    __bind_key__ = DB_CONFIG.validate_bind('autogestion_prod')
    __table_args__ = {"schema": 'public'}
    __tablename__ = 'patentamiento'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    modelo_id = db.Column(db.BigInteger, db.ForeignKey('modelos.id', ondelete='CASCADE'))
    localidad_id = db.Column(db.BigInteger, db.ForeignKey('localidades.id', ondelete='SET NULL'))
    direccion = db.Column(db.String(255))
    fecha = db.Column(db.Date, nullable=False)

    def __init__(self, modelo_id: int, localidad_id: int, direccion: str, fecha: str):
        self.modelo_id = DataTransformer.nan_to_none(modelo_id)
        self.localidad_id = DataTransformer.nan_to_none(localidad_id)
        self.direccion = DataTransformer.nan_to_none(direccion)
        self.fecha = DataTransformer.nan_to_none(fecha)

    def __repr__(self):
        public_attributes = {key: value for key, value in self.__dict__.items() if not key.startswith('_')}
        attributes = ', '.join(f"{key}: {value}" for key, value in public_attributes.items())
        return f"{self.__class__.__name__} -> {attributes}"
