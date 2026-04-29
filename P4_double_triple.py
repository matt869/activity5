# reads integers.txt and splits the work into two output files
# double.txt gets the square of every even number
# triple.txt gets the cube of every odd number
# i added a visual table output to make the terminal output readable

class IntegerProcessor:
    def __init__(self, source_file):
        self.source_file = source_file
        self.integers = []
        self.even_data = []   # stores (original, squared) tuples
        self.odd_data = []    # stores (original, cubed) tuples

    def read_integers(self):
        try:
            with open(self.source_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        self.integers.append(int(line))
        except FileNotFoundError:
            print(f"Cannot open {self.source_file} - file not found.")
            raise
        except ValueError as e:
            print(f"Found a non-integer value in the file: {e}")
            raise

    def process(self):
        # go through all integers and compute what we need for each
        for num in self.integers:
            if num % 2 == 0:
                # even numbers: compute the square
                self.even_data.append((num, num ** 2))
            else:
                # odd numbers: compute the cube
                self.odd_data.append((num, num ** 3))

    def write_double(self, output_file='double.txt'):
        # double.txt contains the squared values of even numbers
        with open(output_file, 'w') as f:
            f.write("Square of Even Numbers\n")
            f.write("=" * 30 + "\n")
            f.write(f"{'Original':<15} {'Squared'}\n")
            f.write("-" * 30 + "\n")
            for original, squared in self.even_data:
                f.write(f"{original:<15} {squared}\n")
            f.write(f"\nTotal even numbers processed: {len(self.even_data)}\n")
        print(f"Wrote {len(self.even_data)} squared values to {output_file}")

    def write_triple(self, output_file='triple.txt'):
        # triple.txt contains the cubed values of odd numbers
        with open(output_file, 'w') as f:
            f.write("Cube of Odd Numbers\n")
            f.write("=" * 30 + "\n")
            f.write(f"{'Original':<15} {'Cubed'}\n")
            f.write("-" * 30 + "\n")
            for original, cubed in self.odd_data:
                f.write(f"{original:<15} {cubed}\n")
            f.write(f"\nTotal odd numbers processed: {len(self.odd_data)}\n")
        print(f"Wrote {len(self.odd_data)} cubed values to {output_file}")

    def print_terminal_table(self):
        # shows everything in one table so you can see results without opening files
        print("\n--- Processing Results ---")
        print(f"{'Number':<10} {'Type':<8} {'Result':<15} {'Operation'}")
        print("-" * 50)
        for num in self.integers:
            if num % 2 == 0:
                result = num ** 2
                num_type = "Even"
                op = f"{num}^2"
            else:
                result = num ** 3
                num_type = "Odd"
                op = f"{num}^3"
            print(f"{num:<10} {num_type:<8} {result:<15} {op}")

    def run(self):
        self.read_integers()
        self.process()
        self.write_double()
        self.write_triple()
        self.print_terminal_table()


class IntegerFileGenerator:
    # generates a sample integers.txt for testing
    def __init__(self, filename='integers.txt'):
        self.filename = filename

    def generate(self):
        import random
        integers = random.sample(range(1, 51), 20)
        with open(self.filename, 'w') as f:
            for num in integers:
                f.write(f"{num}\n")
        print(f"Generated {self.filename} with 20 random integers.")


if __name__ == "__main__":
    generator = IntegerFileGenerator()
    generator.generate()

    processor = IntegerProcessor("integers.txt")
    processor.run()