from app import db
from .favorite import Favorite
from .partner import Partner  # Importa la definición de Partner

promotion_categories = db.Table('promotion_categories',
    db.Column('promotion_id', db.Integer, db.ForeignKey('promotions.promotion_id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.category_id'), primary_key=True)
)

class Promotion(db.Model):
    __tablename__ = 'promotions'

    promotion_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
    qr_code = db.Column(db.Text, nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branches.branch_id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    partner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    available_quantity = db.Column(db.Integer, nullable=True)
    discount_percentage = db.Column(db.Float, nullable=False) 
    status_id = db.Column(db.Integer, db.ForeignKey('statuses.id'), nullable=False, default=1)

    images = db.relationship('PromotionImage', backref='promotion', lazy=True)
    categories = db.relationship('Category', secondary=promotion_categories, backref=db.backref('promotions', lazy=True))
    favorites = db.relationship('Favorite', back_populates='promotion', cascade='all, delete-orphan', overlaps='favorited_by')
    status = db.relationship('Status', backref=db.backref('promotions', lazy=True)) 
    # estado activa en caso de cargarse un estado
    
    def serialize(self):

        partner_details = None
        if self.partner_id:
            partner = Partner.query.get(self.partner_id)
            if partner:
                partner_details = partner.serialize()

        return {
            "promotion_id": self.promotion_id,
            "title": self.title,
            "description": self.description,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "expiration_date": self.expiration_date.isoformat() if self.expiration_date else None,
            "qr_code": self.qr_code,
            "branch_id": self.branch_id,
            "partner_id": self.partner_id,
            "available_quantity": self.available_quantity,
            "discount_percentage": self.discount_percentage,
            "status": {
                "id": self.status.id,
                "name": self.status.name,
                "description": self.status.description
            },
            "images": [image.serialize() for image in self.images],
            "categories": [{"category_id": category.category_id, "name": category.name} for category in self.categories],
            "favorites": [{"user_id": fav.user_id, "created_at": fav.created_at.isoformat()} for fav in self.favorites],
            "partner_details": partner_details  # Agregando detalles del partner
        }

    def __repr__(self):
        return f'<Promotion {self.title}>'

class PromotionImage(db.Model):
    __tablename__ = 'promotion_images'

    image_id = db.Column(db.Integer, primary_key=True)
    promotion_id = db.Column(db.Integer, db.ForeignKey('promotions.promotion_id'))
    image_path = db.Column(db.Text, nullable=False)

    def serialize(self):
        return {
            "image_id": self.image_id,
            "promotion_id": self.promotion_id,
            "image_path": self.image_path
        }

    def __repr__(self):
        return f'<PromotionImage {self.image_path}>'
