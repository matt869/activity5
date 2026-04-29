# this program reads numbers from a file and splits them into even and odd
# i added a summary report at the end just to make it more useful

class NumberSorter:
    def __init__(self, source_file):
        self.source_file = source_file
        self.numbers = []
        self.even_numbers = []
        self.odd_numbers = []

    def read_numbers(self):
        # open the source file and pull in each number line by line
        try:
            with open(self.source_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        self.numbers.append(int(line))
        except FileNotFoundError:
            print(f"Could not find {self.source_file}. Make sure the file exists.")
            raise
        except ValueError as e:
            print(f"There's something in the file that isn't a number: {e}")
            raise

    def sort_numbers(self):
        # go through each number and put it in the right bucket
        for num in self.numbers:
            if num % 2 == 0:
                self.even_numbers.append(num)
            else:
                self.odd_numbers.append(num)

    def write_even(self, output_file='even.txt'):
        with open(output_file, 'w') as f:
            f.write("Even Numbers\n")
            f.write("=" * 20 + "\n")
            for num in self.even_numbers:
                f.write(f"{num}\n")
            f.write(f"\nTotal: {len(self.even_numbers)} even numbers\n")
        print(f"Written {len(self.even_numbers)} even numbers to {output_file}")

    def write_odd(self, output_file='odd.txt'):
        with open(output_file, 'w') as f:
            f.write("Odd Numbers\n")
            f.write("=" * 20 + "\n")
            for num in self.odd_numbers:
                f.write(f"{num}\n")
            f.write(f"\nTotal: {len(self.odd_numbers)} odd numbers\n")
        print(f"Written {len(self.odd_numbers)} odd numbers to {output_file}")

    def print_summary(self):
        # just a nice recap so you can see what happened at a glance
        print("\n--- Summary ---")
        print(f"Total numbers read : {len(self.numbers)}")
        print(f"Even numbers found : {len(self.even_numbers)} -> {self.even_numbers}")
        print(f"Odd numbers found  : {len(self.odd_numbers)} -> {self.odd_numbers}")

    def run(self):
        self.read_numbers()
        self.sort_numbers()
        self.write_even()
        self.write_odd()
        self.print_summary()


class NumberFileGenerator:
    # helper class to create a sample numbers.txt so you can test right away
    def __init__(self, filename='numbers.txt'):
        self.filename = filename

    def generate(self):
        import random
        numbers = random.sample(range(-50, 101), 20)
        with open(self.filename, 'w') as f:
            for num in numbers:
                f.write(f"{num}\n")
        print(f"Generated {self.filename} with 20 random integers.")


if __name__ == "__main__":
    # generate the test file first, then run the sorter
    generator = NumberFileGenerator()
    generator.generate()

    sorter = NumberSorter("numbers.txt")
    sorter.run()