from django.core.management.base import BaseCommand
from student.models import Student
from professor.models import Professor, Subject


class Command(BaseCommand):
    help = "Seed the database with sample students, professors, and subjects."

    def handle(self, *args, **options):
        students = [
            {"roll_no": "S001", "name": "Aarav Shah", "email": "aarav@example.com", "course": "BCA", "year": 2, "phone": "9998887771"},
            {"roll_no": "S002", "name": "Diya Patel", "email": "diya@example.com", "course": "BCA", "year": 3, "phone": "9998887772"},
            {"roll_no": "S003", "name": "Kabir Mehta", "email": "kabir@example.com", "course": "BSc IT", "year": 1, "phone": "9998887773"},
            {"roll_no": "S004", "name": "Ananya Joshi", "email": "ananya@example.com", "course": "MCA", "year": 1, "phone": "9998887774"},
        ]
        for s in students:
            Student.objects.update_or_create(roll_no=s["roll_no"], defaults=s)

        professors = [
            {"emp_id": "P001", "name": "Dr. Rakesh Verma", "email": "rakesh.verma@example.com", "department": "Computer Science", "phone": "9887776661"},
            {"emp_id": "P002", "name": "Dr. Sunita Rao", "email": "sunita.rao@example.com", "department": "Information Technology", "phone": "9887776662"},
        ]
        prof_objs = {}
        for p in professors:
            obj, _ = Professor.objects.update_or_create(emp_id=p["emp_id"], defaults=p)
            prof_objs[p["emp_id"]] = obj

        subjects = [
            {"code": "CS101", "name": "Data Structures", "credits": 4, "professor": prof_objs["P001"]},
            {"code": "CS102", "name": "Database Management Systems", "credits": 4, "professor": prof_objs["P001"]},
            {"code": "IT201", "name": "Web Application Development", "credits": 3, "professor": prof_objs["P002"]},
            {"code": "IT202", "name": "Mobile App Development", "credits": 3, "professor": prof_objs["P002"]},
        ]
        for sub in subjects:
            Subject.objects.update_or_create(code=sub["code"], defaults=sub)

        self.stdout.write(self.style.SUCCESS(
            f"Seeded {len(students)} students, {len(professors)} professors, {len(subjects)} subjects."
        ))
