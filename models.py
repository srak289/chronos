import json

from datetime import datetime, timezone

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import as_declarative, declarative_base, declared_attr

def timenow():
    return datetime.now(timezone.utc)

@as_declarative()
class Base(object):

    id = Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        cls_name = ''
        for i,x in enumerate(cls.__name__):
            if i > 0 and x.isupper():
                cls_name += f'_{x.lower()}'
            elif i == 0:
                cls_name += x.lower()
            else:
                cls_name += x
        return cls_name

    @declared_attr
    def timestamp(self):
        return Column(DateTime, default=timenow)

    def as_dict(self):
        r = dict()
        for c in self.__table__.columns:
            v = getattr(self, c.name)
            if v:
                if type(c.type) is DateTime:
                    r[c.name] = v.isoformat()
                else:
                    r[c.name] = v
        return r

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"

class Billable(Base):
    name = Column(String, unique=True)

    relationship("Job")

class Job(Base):
    name = Column(String, unique=True)
    billing_code = Column(String)

    relationship("Tracker")

class Tracker(Base):
    name = Column(String)
    in_progress = Column(Boolean, default=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime)
    total_time = Column(DateTime)

class InProgress(Base):
    tracker_id = Column(ForeignKey("tracker.id"))
    tracker_name = Column(ForeignKey("tracker.name"))
