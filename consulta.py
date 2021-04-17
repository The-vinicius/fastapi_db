from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
import dados, banco


def test(db: Session, play: dados.Play):
    db_user = banco.Play(level=play.level, caracter=play.caracter)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return jsonable_encoder(db_user)

def get_play(db: Session, play_id: int):
    db_i = db.query(banco.Play).filter(banco.Play.id == play_id).first()
    db_i = jsonable_encoder(db_i)
    return db_i