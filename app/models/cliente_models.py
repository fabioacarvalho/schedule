from app import db
from sqlalchemy_utils import ChoiceType

class Cliente(db.Model):
    __tablename__ = 'cliente'

    SEXO_CHOICES = [
        (u'M', u'Masculino'),
        (u'F', u'Feminino'),
        (u'O', u'Outro'),
    ]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    data_nascimento = db.Column(db.Date, nullable=False)
    profissao = db.Column(db.String(200), nullable=False)
    sexo = db.Column(ChoiceType(SEXO_CHOICES))
    telefone = db.Column(db.String(200), nullable=False)
