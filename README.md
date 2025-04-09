CS2006-P1: Distorted Integer Set Operations
This project explores mathematical structures using custom-defined integer sets and operations. It includes implementations for distorted integers and sets, as well as various properties and behaviors such as associativity, commutativity, and more.

Contents
distorted_ints.py — Defines the behavior of "distorted integers."

distorted_int_set.py — Implements a set-like structure for distorted integers.

large_set.py — Optimizations or extensions for handling large sets.

test_*.py — A suite of unit tests checking mathematical properties:

associative, commutative, idempotent, quasi, iterator, roots_of_one, etc.

test_equation.py tests expression evaluation logic.

Getting Started
Requirements
Python 3.x

No external dependencies (uses only standard libraries)

Running Tests
You can run all tests using the test_all.py script:

bash
Copy
Edit
python code/test_all.py
Or run individual test files like so:

bash
Copy
Edit
python code/test_commutative.py
Purpose
Originally developed for the CS2006 module, this project investigates the behavior of mathematical operations under non-standard definitions, making it useful for exploring theoretical computer science or mathematical logic topics.

License
This project is provided for educational purposes and does not currently include a license. Contact the authors for reuse or distribution.
