from sqlalchemy import select, create_engine
from crud import *
from connection import *
from models import User

def available_users(engine):
    with Session(engine) as session:
        query = select(User.login)
        for user in session.scalars(query):
            yield user

def main():
    engine = get_engine()
    create_table_ddl(engine)
    
    user = User(login=input("Login:\t"), 
                user_fname=input("First Name:\t"),
                user_sname=input("Second Name:\t"),
                password = input("Password:\t")
                )
    create_entry([user], engine)
    print(f"Available user ids are: {list(available_users(engine))}")
    
    

    with Session(engine) as session:
        query = select(User)

        for user in session.scalars(query):
            print(user)

if __name__=="__main__":
    main()