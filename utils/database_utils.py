from sqlalchemy.orm import sessionmaker
from models_db.TreshStatTable import TrashStatTable
import pandas as pd
from sqlalchemy.orm import sessionmaker
from database import engine, Base

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()



def insert_TrashStatTable(list_id: list):
    l = []
    for id_object in list_id:
        l.append(TrashStatTable(id_object=int(id_object.item())))
    session.bulk_save_objects(l)
    session.commit()

def get_TrashStatTable():
    data = [{
        'id': obj.id,
        'id_object': obj.id_object,
        'date_detection': obj.date_detection
    } for obj in session.query(TrashStatTable).all()]

    df = pd.DataFrame(data)

    return df

# conn = st.connection("postgresql", type="sql")

# def get_time():
#     return datetime.now(pytz.timezone('Europe/Moscow'))

# def writing_trash_class_database(list_cls:list):
#     query = f"INSERT INTO tresh_stat VALUES "

#     for i in list_cls:
#         query += f"(DEFAULT, {int(i.item())}, '{get_time()}'), "
#     query = query[:-2]
#     print(query)

    
#     with conn.session as s:
#         s.execute(text(query))
#         s.commit()

# def get_data_table(name_table: str):
#     st.cache_data.clear()
#     conn = st.connection("postgresql", type="sql")

#     return conn.query(f"SELECT * FROM {name_table};")
