from sqlalchemy import Column, String, LargeBinary
from sqlalchemy.orm import relationship

from backend import db
from backend.models.utils import Entity


class Image(db.Model, Entity):
    def __repr__(self):
        return '<Image {self.id}>'.format(self=self)

    filename = Column(String)
    # Extention. EG 'png'.
    filetype = Column(String, nullable=False)
    # Binary data of image.
    file_data = Column(LargeBinary, nullable=False)

    product = relationship(
        'Product',
        back_populates='thumbnail_image',
    )

    festival = relationship(
        'Festival',
        back_populates='image',
    )
