from app import app
from models import Meter, MeterData
from database import init_db, db_session
from datetime import datetime


def merge_fake_data():
    db_session.merge(Meter(id=0, label='Meter A'))
    db_session.merge(Meter(id=1, label='Meter B'))
    db_session.merge(Meter(id=2, label='Meter C'))
    db_session.merge(MeterData(id=0, meter_id=0, timestamp=datetime.fromordinal(10000), value=10))
    db_session.merge(MeterData(id=1, meter_id=0, timestamp=datetime.fromordinal(40000), value=20))
    db_session.merge(MeterData(id=2, meter_id=0, timestamp=datetime.fromordinal(20000), value=30))
    db_session.merge(MeterData(id=3, meter_id=0, timestamp=datetime.fromordinal(30000), value=10))
    db_session.merge(MeterData(id=4, meter_id=1, timestamp=datetime.fromordinal(60000), value=100))
    db_session.merge(MeterData(id=5, meter_id=1, timestamp=datetime.fromordinal(50000), value=10))
    db_session.commit()


def main():
    init_db()
    merge_fake_data()
    app.run()


if __name__ == '__main__':
    main()
