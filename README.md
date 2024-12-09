# Transaction Challenge

## Ho to run:
#### Setup virtual environment
```python
# Ensure Python is installed and create the virtual env
python -m venv venv
source venv/bin/activate
```

#### Install dependencies
```python
pip install -r requirements.txt
```

#### Run the app
```python
#Make sure you are in the right folder
python main.py
```

## How to Test

#### Run command
```python
pytest
```

# The App Design

Given my experience in building APIs and implementing architecture patterns like Domain-Driven Design (DDD), Hexagonal Architecture, and Object-Oriented Programming (OOP), I followed a modular and maintainable approach. Here’s an overview:

### Structure:
- Modular Design: The app is split into different modules to handle domain logic, API requests, and other responsibilities separately.

- Domain Layer: Contains business logic and validations using DTOs (Data Transfer Objects) and abstract base classes for consistency.
### Flow: 
- Endpoint Execution:
The `POST /event` endpoint triggers the `EventHandler`. It determines the type of transaction (e.g., "deposit" or "withdrawal") and loops through various checks implemented in the `CheckBase` subclasses.

- Checks Execution:
Each check method validates specific business rules. The results are aggregated and returned as part of the response object.
### Validation: 
- Input Validation:
The `ClientTransactionDTO` ensures the request payload is structured correctly and enforces type checks (e.g., event.type is always "deposit" or "withdrawal").

- Code Validation:
Abstract base classes (e.g., `CheckBase`) standardize the structure of the `.check()` methods for maintainability and scalability.

### Benefits:
- Maintainability:
Code is modular and easy to modify. For instance, updating a specific check in `CheckEvents.py` does not require changes to the API layer.

- Scalability:
New checks can be added without affecting the core flow.

- Readability and Debugging:
Clear separation of concerns allows debugging in smaller, manageable files instead of monolithic codebases.

# Challenges Encountered

Here are some challenges I faced during this project:

- First-Time Python Experience:
Despite being new to Python, I leveraged my experience with languages like Java, C#, TypeScript, and JavaScript to pick it up quickly. Python’s clean syntax and powerful features made this process enjoyable.

- Virtual Environments:
Setting up and managing the virtual environment within VSCode was initially tricky. Understanding how it isolates dependencies and integrates with tools like Flask was a valuable learning experience.

- Syntax and Features:
Python's use of decorators (@), type annotations, and return types (e.g., -> dict) was fascinating to learn and use. The use of whitespace for code blocks (instead of braces) and minimal parentheses in control flow statements provided a refreshing perspective.

# Future Improvements
- Enhanced Logging: Add detailed logs for each step in the transaction handling process for better traceability.
- Error Handling: Implement more robust error handling to provide informative responses for invalid requests.
- Performance Optimization: Profile the code to ensure efficient processing of large transaction datasets.