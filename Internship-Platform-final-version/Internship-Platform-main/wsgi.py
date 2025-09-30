import click
from flask import Flask
from App.models.model import db
from App.models.student import Student
from App.models.employer import Employer
from App.models.internship import Internship, Shortlist

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///internship.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@click.group()
def cli():
    pass

@cli.command()
def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        click.echo("Database initialized.")

# ---- Students ----
@cli.command()
@click.argument("name")
def add_student(name):
    with app.app_context():
        student = Student(name=name)
        db.session.add(student)
        db.session.commit()
        click.echo(f"Added student: {student}")

@cli.command()
@click.argument("student_id", type=int)
def view_shortlisted(student_id):
    with app.app_context():
        student = Student.query.get(student_id)
        if not student:
            click.echo("Student not found.")
            return
        entries = Shortlist.query.filter_by(student_id=student.id).all()
        if not entries:
            click.echo("No shortlisted positions.")
            return
        for entry in entries:
            click.echo(f"{entry.internship.title} at {entry.internship.employer.name} → {entry.status}")

# ---- Employers ----
@cli.command()
@click.argument("name")
def add_employer(name):
    with app.app_context():
        employer = Employer(name=name)
        db.session.add(employer)
        db.session.commit()
        click.echo(f"Added employer: {employer}")

@cli.command()
@click.argument("employer_id", type=int)
@click.argument("title")
def create_internship(employer_id, title):
    with app.app_context():
        employer = Employer.query.get(employer_id)
        if not employer:
            click.echo("Employer not found.")
            return
        internship = Internship(title=title, employer=employer)
        db.session.add(internship)
        db.session.commit()
        click.echo(f"Created internship: {internship}")

@cli.command()
@click.argument("employer_id", type=int)
@click.argument("internship_id", type=int)
@click.argument("student_id", type=int)
@click.argument("decision")
def respond(employer_id, internship_id, student_id, decision):
    with app.app_context():
        internship = Internship.query.get(internship_id)
        if not internship or internship.employer_id != employer_id:
            click.echo("Invalid employer or internship.")
            return
        entry = Shortlist.query.filter_by(internship_id=internship_id, student_id=student_id).first()
        if not entry:
            click.echo("Student not shortlisted for this internship.")
            return
        entry.status = decision.capitalize()
        db.session.commit()
        click.echo(f"Updated shortlist: Student {student_id} → {decision}")

# ---- Staff ----
@cli.command()
@click.argument("internship_id", type=int)
@click.argument("student_id", type=int)
def shortlist_student(internship_id, student_id):
    with app.app_context():
        internship = Internship.query.get(internship_id)
        student = Student.query.get(student_id)
        if not internship or not student:
            click.echo("Invalid internship or student.")
            return
        existing = Shortlist.query.filter_by(internship_id=internship.id, student_id=student.id).first()
        if existing:
            click.echo("Student already shortlisted.")
            return
        shortlist = Shortlist(student_id=student.id, internship_id=internship.id)
        db.session.add(shortlist)
        db.session.commit()
        click.echo(f"Shortlisted {student.name} for {internship.title}")

if __name__ == "__main__":
    cli()
