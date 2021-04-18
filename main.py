from sqlalchemy.orm import Session
import uvicorn
import os
from fastapi import FastAPI, Depends

import banco, consulta, dados
from sql import sessionlocal, engine


banco.Base.metadata.create_all(bind=engine)


app = FastAPI()



def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/play/', response_model=dados.Play)
async def teste_play(play: dados.Play, db:  Session = Depends(get_db)):
    return consulta.test(db=db, play=play)

@app.get('/play/{id}', response_model=dados.Play)
async def read_play(play_id: int, db: Session= Depends(get_db)):
    return consulta.get_play(db=db, play_id=play_id)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run(app, host='0.0.0.0', port=port)
