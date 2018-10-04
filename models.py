from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base


class Meter(Base):
    __tablename__ = 'meter'

    id = Column(Integer, primary_key=True)
    label = Column(String)


class MeterData(Base):
    __tablename__ = 'meter_data'

    id = Column(Integer, primary_key=True)
    meter_id = Column(Integer, ForeignKey('meter.id'))
    timestamp = Column(DateTime)
    value = Column(Integer)

    def to_json_dict(self):
        return {
            'id': self.id,
            'meter_id': self.meter_id,
            'timestamp': self.timestamp.isoformat(),
            'value': self.value
        }
