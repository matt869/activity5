# reads a file with student names and their GWA
# finds and prints the one with the highest GWA
# i also added a full leaderboard display because why not

class Student:
    def __init__(self, name, gwa):
        self.name = name
        self.gwa = gwa

    def __repr__(self):
        # easier to debug when you can just print the object
        return f"Student(name='{self.name}', gwa={self.gwa})"


class StudentRecordReader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load_records(self):
        # each line in the file should be: Name, GWA
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(',')
                    if len(parts) != 2:
                        print(f"Skipping badly formatted line: '{line}'")
                        continue
                    name = parts[0].strip()
                    gwa = float(parts[1].strip())
                    self.students.append(Student(name, gwa))
        except FileNotFoundError:
            print(f"File not found: {self.filename}")
            raise

    def get_top_student(self):
        # lower GWA is better in PH grading (1.0 is highest)
        # but this handles both conventions - just finds the minimum value
        if not self.students:
            return None
        return min(self.students, key=lambda s: s.gwa)

    def display_leaderboard(self):
        # sort from best to worst and print the whole board
        sorted_students = sorted(self.students, key=lambda s: s.gwa)
        print("\n--- Student Leaderboard (Best to Lowest GWA) ---")
        print(f"{'Rank':<6} {'Name':<25} {'GWA'}")
        print("-" * 40)
        for rank, student in enumerate(sorted_students, start=1):
            marker = " <-- TOP" if rank == 1 else ""
            print(f"{rank:<6} {student.name:<25} {student.gwa:.2f}{marker}")

    def display_top(self):
        top = self.get_top_student()
        if top:
            print("\n=== Highest GWA ===")
            print(f"Student : {top.name}")
            print(f"GWA     : {top.gwa:.2f}")
        else:
            print("No student records found.")

    def run(self):
        self.load_records()
        self.display_leaderboard()
        self.display_top()


class StudentFileGenerator:
    # creates a sample students.txt for testing purposes
    def __init__(self, filename='students.txt'):
        self.filename = filename

    def generate(self):
        records = [
            ("Juan dela Cruz", 1.50),
            ("Maria Santos", 1.25),
            ("Carlo Reyes", 1.75),
            ("Ana Gonzales", 1.00),
            ("Nico Bautista", 2.00),
            ("Liza Mendoza", 1.50),
            ("Ryan Torres", 1.25),
            ("Claire Villanueva", 1.75),
            ("Mark Ramos", 2.25),
            ("Jenny Flores", 1.50),
            ("James Castillo", 1.00),
            ("Rachel Aquino", 2.50),
            ("Paolo Aguilar", 1.25),
            ("Trish Morales", 1.75),
            ("Kevin Dela Pena", 1.50),
            ("Sophia Navarro", 1.00),
            ("Andrei Lim", 2.00),
            ("Camille Cruz", 1.75),
            ("Ethan Ong", 1.25),
            ("Dana Pascual", 1.50),
        ]
        with open(self.filename, 'w') as f:
            for name, gwa in records:
                f.write(f"{name}, {gwa}\n")
        print(f"Generated {self.filename} with 20 student records.")


if __name__ == "__main__":
    generator = StudentFileGenerator()
    generator.generate()

    reader = StudentRecordReader("students.txt")
    reader.run()