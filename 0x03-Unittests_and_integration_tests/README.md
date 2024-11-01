unittests & Integration tests
### Summary of Unittests and Integration Tests in Python
Unittests and integration tests are two types of automated tests used in software development to ensure code correctness and reliability. **Unittests** focus on testing individual units or components of code in isolation, ensuring each function or method behaves as expected. **Integration tests**, on the other hand, verify that multiple components work together as intended. Python provides robust support for both types of testing through libraries like `unittest`, `pytest`, and other specialized tools.

### Main Points of Unittests in Python
1. **Purpose**:
   - Ensure that individual functions, methods, or classes perform as expected when tested in isolation.
   - Catch bugs at an early stage and make refactoring safer.

2. **Python's `unittest` Library**:
   - Part of Python's standard library and follows the structure of test case classes.
   - Provides a framework for defining test cases, test suites, and running tests.
   - Includes methods like `assertEqual()`, `assertTrue()`, and `assertRaises()` to check conditions.

3. **Test Structure**:
   - Test cases are organized into classes that inherit from `unittest.TestCase`.
   - Methods in test classes must start with `test_` to be recognized as test methods.
   - `setUp()` and `tearDown()` methods are used for initializing and cleaning up resources before and after each test.

4. **Running Tests**:
   - Tests can be run using the command line with `python -m unittest` or integrated into CI/CD pipelines for continuous testing.

5. **Advantages**:
   - Easy to write and maintain.
   - Quickly identifies issues at the unit level.
   - Can be extended with plugins and frameworks like `pytest` for enhanced functionality.

### Main Points of Integration Tests in Python
1. **Purpose**:
   - Validate that different parts of the system work together as expected.
   - Ensure that the interactions between integrated components (e.g., a database and a web server) function properly.

2. **Scope**:
   - Broader than unittests, covering a larger portion of the codebase.
   - Can involve multiple classes, functions, or even external services.

3. **Tools for Integration Testing**:
   - **`unittest`** can be adapted for integration tests by running higher-level tests that involve several components.
   - **`pytest`** offers powerful fixtures and plugins to set up integration tests easily.
   - Specialized libraries and frameworks like **`requests`** and **`selenium`** may be used for testing web applications and interactions.

4. **Best Practices**:
   - Keep integration tests as comprehensive as possible without replicating unit-level checks.
   - Ensure integration tests run in an environment that mimics production for accuracy (e.g., using Docker for consistency).
   - Use mock services or test databases where real components are not practical for testing.

5. **Challenges**:
   - Integration tests can be more complex to set up compared to unittests.
   - They may run slower due to the involvement of multiple components.
   - Debugging failures can be more complicated as they can stem from interactions between components.

6. **Benefits**:
   - Detect issues that unit testing may not catch, such as communication problems between components.
   - Provide confidence that the entire system functions as intended after integrating new code.

### Conclusion
Unittests and integration tests complement each other in ensuring code quality. Unittests provide fast, isolated testing of individual components, while integration tests validate the cooperation between components, offering broader assurance of code reliability. Python's built-in `unittest` library, enhanced by third-party tools like `pytest`, helps developers maintain a well-tested codebase.

Resources

https://docs.python.org/3/library/unittest.html
https://www.youtube.com/watch?v=6tNS--WetLI
https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock

### exemple Code

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def division(a, b):
    if b == 0:
        raise ValueError("La division par zéro n'est pas autorisée.")
    return a / b

### exemple Code

import unittest
from calcul import addition, soustraction, division

class TestCalcul(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)

    def test_soustraction(self):
        self.assertEqual(soustraction(10, 5), 5)
        self.assertEqual(soustraction(0, 7), -7)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertRaises(ValueError, division, 10, 0)

if __name__ == '__main__':
    unittest.main()

### exemple Code

class Utilisateur:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def est_majeur(self):
        return self.age >= 18

def bienvenue_utilisateur(utilisateur):
    if utilisateur.est_majeur():
        return f"Bienvenue, {utilisateur.nom} !"
    else:
        return "Accès réservé aux majeurs."

