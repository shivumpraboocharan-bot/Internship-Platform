# Internship Platform CLI

This project implements the **Internship Platform** using a Flask MVC structure with a **CLI interface** (via `wsgi.py`).  
It allows Employers, Staff, and Students to interact with internship positions through command-line commands.

---

## Features

### Employer
- Create internship positions
- Accept/Reject students from shortlist

### Staff
- Shortlist students to internship positions

### Student
- View shortlisted positions and employer responses

---

## Setup

1. Clone the repository:
   ```bash
   git clone <your_repo_url>.git
   cd Internship-Platform-main
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database:
   ```bash
   python wsgi.py init-db
   ```

This creates a SQLite database `internship.db`.

---

## CLI Commands

### Database
```bash
python wsgi.py init-db
```
Reset and initialize the database.

### Student Commands
```bash
python wsgi.py add-student "Alice"
python wsgi.py view-shortlisted 1
```

### Employer Commands
```bash
python wsgi.py add-employer "TechCorp"
python wsgi.py create-internship 1 "Software Intern"
python wsgi.py respond 1 1 1 "Accepted"
```

### Staff Commands
```bash
python wsgi.py shortlist-student 1 1
```

---

## Example Workflow

```bash
python wsgi.py init-db
python wsgi.py add-student "Alice"
python wsgi.py add-student "Bob"
python wsgi.py add-employer "TechCorp"
python wsgi.py create-internship 1 "Software Intern"
python wsgi.py shortlist-student 1 1
python wsgi.py respond 1 1 1 "Accepted"
python wsgi.py view-shortlisted 1
```

Expected output:
```
Software Intern at TechCorp → Accepted
```

---

## Notes
- Update the GitHub repo link in the assignment PDF.
- Ensure `wsgi.py` is used as the entry point for CLI commands.
