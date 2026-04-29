# writes a short autobiography/story into mylife.txt
# uses a class to organize the sections and handle the file writing

class MyLifeWriter:
    def __init__(self, filename='mylife.txt'):
        self.filename = filename
        # these are the sections of the story - you can change the content to yours
        self.sections = [
            ("Introduction", [
                "My name is Juan dela Cruz, and I am a second year BS Computer Science student.",
                "I was born and raised in Manila, Philippines.",
                "I am the second among three siblings in our family.",
            ]),
            ("Early Life", [
                "I grew up in a small but lively neighborhood in Quezon City.",
                "As a kid I was always curious about how things worked.",
                "I remember taking apart old radios just to see what was inside.",
                "That habit of curiosity never really went away.",
            ]),
            ("School Days", [
                "I went to a public elementary school near our house.",
                "Math and Science were always my strongest subjects.",
                "In high school I joined the programming club and that changed everything.",
                "I built my first simple calculator program using Python and I was hooked.",
            ]),
            ("College Life", [
                "I am currently enrolled at Polytechnic University of the Philippines.",
                "College is tough but I genuinely enjoy what I am studying.",
                "I spend a lot of time on coding exercises and side projects.",
                "My favorite course so far has been Data Structures and Algorithms.",
            ]),
            ("Goals and Dreams", [
                "I want to become a software engineer after I graduate.",
                "Specifically I am interested in backend development and system design.",
                "Someday I hope to build something that actually helps people in my community.",
                "For now I just focus on learning as much as I can every single day.",
            ]),
        ]

    def write_to_file(self):
        # write each section with a header and the lines under it
        with open(self.filename, 'w') as f:
            f.write("MY LIFE\n")
            f.write("=" * 50 + "\n\n")

            for section_title, lines in self.sections:
                f.write(f"[ {section_title} ]\n")
                f.write("-" * 30 + "\n")
                for line in lines:
                    f.write(f"  {line}\n")
                # blank line between sections to keep it readable
                f.write("\n")

            f.write("=" * 50 + "\n")
            f.write("End of story. For now.\n")

        print(f"Successfully wrote to {self.filename}")

    def preview(self):
        # print the file contents to the terminal so you can check it
        print(f"\n--- Preview of {self.filename} ---\n")
        with open(self.filename, 'r') as f:
            print(f.read())

    def run(self):
        self.write_to_file()
        self.preview()


if __name__ == "__main__":
    writer = MyLifeWriter()
    writer.run()