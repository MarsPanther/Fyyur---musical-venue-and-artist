#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from app import db
# from datetime import datetime

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    """ Venue Model """
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(500))
    genres = db.Column(db.ARRAY(db.String(120)))
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(800))
    website = db.Column(db.String(500))

    shows = db.relationship('Show', backref='Venue',
                            lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return '<Venue {}>'.format(self.name)


class Artist(db.Model):
    """ Artist Model"""
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.ARRAY(db.String(120)))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(500))
    website_link = db.Column(db.String(500))
    seeking_venue = db.Column(db.Boolean, default=False, nullable=False)
    seeking_description = db.Column(db.String(500), nullable=True)

    # Artist -> Show
    shows = db.relationship('Show', backref='Artist', lazy=True)

    def __repr__(self):
        return '<Artist {}>'.format(self.name)


class Show(db.Model):
    """ Show Model """
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)

    # Show -> Artist

    artist_id = db.Column(db.Integer, db.ForeignKey(
        'Artist.id'), nullable=False)
    # Show -> Venue
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)

    def __repr__(self):
        return '<Show Artist ID:{}, Venue ID:{}>'.format(self.artist_id, self.venue_id)