from sqlalchemy import create_engine, Column, INTEGER, FLOAT, String
from sqlalchemy.orm import declarative_base, sessionmaker

# ایجاد اتصال به دیتابیس
engine = create_engine('sqlite:///CarData.db', echo=True)

Base = declarative_base()

class Car(Base):
    __tablename__ = 'carsinfo'

    __table_args__ = {'extend_existing': True} 
    # ------------------------------------------------------

    id = Column(INTEGER, primary_key=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    price = Column(FLOAT)
    quantity = Column(INTEGER)

class Customer(Base):
    __tablename__ = 'customers'
    __table_args__ = {'extend_existing': True} # برای این کلاس هم اضافه کنید

    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False)

# ساخت جداول در دیتابیس
Base.metadata.create_all(engine)

# ایجاد Session برای کار با داده‌ها
Session = sessionmaker(bind=engine)
sessionLocal = Session()


# car1 = Car(brand='Benz', model='G class', price=2000, quantity=5)
# car2 = Car(brand='BMW', model='AMG', price=1500, quantity=10)

# sessionLocal.add(car1)
# sessionLocal.add(car2)
# sessionLocal.commit()

# print("save")
cars_obj = sessionLocal.query(Car).all()  # list of car objects
#print(cars_obj)
# for item in cars_obj:
#     print(item.brand)
#     print(item.model)
#     print(item.price)
#     print(item.quantity)
#     print('--'*30)
#################################3

# car1 = sessionLocal.query(Car).filter_by(id=1).first()  # object
# print(car1.brand)
# print(car1.model)
# print(car1.price)
###########################################3

# car_bmw = sessionLocal.query(Car).filter_by(price=1500).all()  # list of car objects
# for item in car_bmw:
#     print(item.brand)
#     print(item.model)
#     print(item.price)
#     print(item.quantity)
#     print('--'*30)
#####################################

# car_bmw = sessionLocal.query(Car).filter(Car.price > 1500).all()
# for item in car_bmw:
#     print(item.brand)
#     print(item.model)
#     print(item.price)
#     print(item.quantity)
#     print('--'*30)

################################

# car_bmw = sessionLocal.query(Car).filter(Car.model.like('amg%')).all()
# for item in car_bmw:
#     print(item.brand)
#     print(item.model)
#     print(item.price)
#     print(item.quantity)
#     print('--'*30)

#############################

car_temp = sessionLocal.query(Car).filter(Car.model.like('AMG%')).first()

# car_temp.brand = 'AUDI'
# sessionLocal.commit()

if car_temp != None:
    sessionLocal.delete(car_temp)
    sessionLocal.commit()

