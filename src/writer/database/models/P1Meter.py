from sqlalchemy import Column, ForeignKey, Integer, Float
from ..Base import Base

class P1Meter(Base):
    __tablename__ = 'p1meter'

    timestamp = Column(Integer, primary_key=True)
    total_high_energy = Column(Float)
    total_low_energy = Column(Float)
    current_energy = Column(Float)
    gas = Column(Float)

    def __repr__(self):
        return "(timestamp='%s', gas='%s', energy='%s')" % (
                                self.timestamp, self.gas, self.current_energy)