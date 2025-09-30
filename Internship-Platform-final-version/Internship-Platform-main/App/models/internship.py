from .model import db
from .student import Student
from .employer import Employer

class Internship(db.Model):
    __tablename__ = 'internships'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    employer_id = db.Column(db.Integer, db.ForeignKey('employers.id'))
    employer = db.relationship("Employer", backref="internships")

    def __repr__(self):
        return f"<Internship {self.id} - {self.title}>"


class Shortlist(db.Model):
    __tablename__ = 'shortlists'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    internship_id = db.Column(db.Integer, db.ForeignKey('internships.id'))
    status = db.Column(db.String(50), default="Pending")

    student = db.relationship("Student", backref="shortlists")
    internship = db.relationship("Internship", backref="shortlists")

    def __repr__(self):
        return f"<Shortlist student={self.student_id} internship={self.internship_id} status={self.status}>"
