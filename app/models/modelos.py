"""Modelo entity module"""
@dataclasses.dataclass
class Modelo(db.Model):
    """Modelo class"""
    __bind_key__ = DB_CONFIG.validate_bind('autogestion_prod')
    __table_args__ = {"schema": 'public'}
    __tablename__ = 'modelos'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(255), nullable=False)
    marca_id = db.Column(db.BigInteger, db.ForeignKey('marcas.id', ondelete='CASCADE'))
    cilindrada_id = db.Column(db.BigInteger, db.ForeignKey('cilindradas.id', ondelete='CASCADE'))
    origen_id = db.Column(db.BigInteger, db.ForeignKey('origenes.id', ondelete='CASCADE'))
    tipo_id = db.Column(db.BigInteger, db.ForeignKey('tipos.id', ondelete='CASCADE'))
    categoria_id = db.Column(db.BigInteger, db.ForeignKey('categorias.id', ondelete='CASCADE'))

    def __init__(self, descripcion: str, marca_id: int, cilindrada_id: int, origen_id: int, tipo_id: int, categoria_id: int):
        self.descripcion = DataTransformer.nan_to_none(descripcion)
        self.marca_id = DataTransformer.nan_to_none(marca_id)
        self.cilindrada_id = DataTransformer.nan_to_none(cilindrada_id)
        self.origen_id = DataTransformer.nan_to_none(origen_id)
        self.tipo_id = DataTransformer.nan_to_none(tipo_id)
        self.categoria_id = DataTransformer.nan_to_none(categoria_id)

    def __repr__(self):
        public_attributes = {key: value for key, value in self.__dict__.items() if not key.startswith('_')}
        attributes = ', '.join(f"{key}: {value}" for key, value in public_attributes.items())
        return f"{self.__class__.__name__} -> {attributes}"
