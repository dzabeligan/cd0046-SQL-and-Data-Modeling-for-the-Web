from app_config import db
from datetime import datetime


class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))
    website = db.Column(db.String(500))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.Text)
    genres = db.Column(db.ARRAY(db.String()), nullable=False)
    shows = db.relationship('Show', backref='venue', lazy=True)
    created_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return (f'<Venue {self.id} {self.name} {self.address} {self.phone} '
                f'{self.image_link} {self.facebook_link}>')

    @property
    def serialize_name_with_upcoming_shows_count(self):
        return {'id': self.id,
                'name': self.name,
                'num_upcoming_shows': Show.query.filter(
                    Show.start_time > datetime.now(),
                    Show.venue_id == self.id).count()
                }

    @property
    def filter_on_area(self):
        return {'city': self.city,
                'state': self.state,
                'venues': [v.serialize_name_with_upcoming_shows_count
                           for v in Venue.query.filter(
                               Venue.city == self.city,
                               Venue.state == self.state).all()]}


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))
    website = db.Column(db.String(500))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.Text)
    genres = db.Column(db.ARRAY(db.String()), nullable=False)
    show = db.relationship('Show', backref='artist', lazy=True)
    created_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return (f'<Artist {self.id} {self.name} {self.city} {self.state}'
                f' {self.phone} {self.image_link} {self.facebook_link}>')


class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(
        db.Integer, db.ForeignKey('Artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
    start_time = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Show {self.id} {self.name}, venue {self.artist_id}>'
