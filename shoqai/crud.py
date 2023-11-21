from sqlalchemy.orm import Session

def create_entry(models:list, engine):
    with Session(engine) as session:
        session.add_all(models)
        session.commit()

def delete(model_object:object, engine):
    pass

def update(model_object:object, new_value, engine):
    pass