from adskipper import db


class Show(db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id', ondelete="cascade", onupdate="cascade"))
    movie = db.relationship('Movie', backref='shows')
    cinema_id = db.Column(db.Integer, db.ForeignKey('cinema.id', ondelete="cascade", onupdate="cascade"))
    showtime = db.Column(db.DateTime)

    __table_args__ = (
        db.UniqueConstraint('movie_id', 'cinema_id', 'showtime', name='movie_id_cinema_id_showtime_unique'),
    )

    # Create base class for this
    def to_dict(self):
        result = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        result['showtime'] = result['showtime'].isoformat()
        return result