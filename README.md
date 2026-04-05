# 🧮 Modular Advanced Calculator

A **fully featured, modular arithmetic calculator** written in Python.  
It evaluates expressions like `(3 + 5) * 2 - 4 / 2` with correct operator precedence and parentheses.

> **Complex yet useful** – supports `+`, `-`, `*`, `/`, `%`, `**` (power), and nested parentheses.

---

## ✨ Features

- **Full expression evaluation** – not limited to two numbers  
- **Operator precedence** – follows standard math rules (`**` > `*/%` > `+-`)  
- **Parentheses** – arbitrary nesting, e.g. `(2 + (3 * 4)) / 5`  
- **Error handling** – division by zero, syntax errors, missing parentheses  
- **Modular architecture** – tokenizer, parser (shunting‑yard), evaluator, CLI  
- **No external dependencies** – pure Python standard library  

---

## 📁 Project Structure

```
calculator/
├── calc/
│   ├── __init__.py          # Makes calc a package
│   ├── tokenizer.py         # Converts string → tokens
│   ├── parser.py            # Tokens → AST (shunting‑yard)
│   └── evaluator.py         # AST → numeric result
├── main.py                  # Interactive CLI entry point
├── requirements.txt         # Empty (no 3rd‑party libs)
└── README.md                # This file
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher

### Installation

1. **Clone or download** the repository  
   ```bash
   git clone https://github.com/yourusername/calculator.git
   cd calculator
   ```

2. **Run the calculator**  
   ```bash
   python main.py
   ```

---

## 🎮 Usage

Type any arithmetic expression and press `Enter`. Type `quit`, `exit`, or `q` to leave.

### Examples

```
>>> 1 + 1
1 + 1 = 2.0

>>> (3 + 5) * 2 - 4 / 2
(3 + 5) * 2 - 4 / 2 = 14.0

>>> 2 ** 3 + 1
2 ** 3 + 1 = 9.0

>>> 10 / 3
10 / 3 = 3.3333333333333335

>>> (2 + 3) * (4 - 1) ** 2
(2 + 3) * (4 - 1) ** 2 = 45.0
```

### Error Handling

```
>>> 5 / 0
Error: Division by zero

>>> (2 + 3
Error: Missing closing parenthesis
```

---

## 🧠 How It Works (Modular Breakdown)

| Module        | Responsibility                                                                 |
|---------------|--------------------------------------------------------------------------------|
| `tokenizer.py`| Splits input into tokens: numbers, operators `+ - * / % **`, parentheses `( )` |
| `parser.py`   | Implements the **Shunting‑yard algorithm** to build an Abstract Syntax Tree (AST) respecting precedence and associativity |
| `evaluator.py`| Recursively walks the AST and performs the arithmetic operations               |
| `main.py`     | Handles user input/output, loops until quit, and prints results or errors      |

This separation allows easy extension (e.g., adding unary minus, functions like `sqrt`, or variables).

---

## 🔧 Extending the Calculator

Want to add a new operator, like factorial (`!`)?

1. **Tokenizer** – add `!` to the regex pattern.
2. **Parser** – assign precedence and associativity.
3. **Evaluator** – add a new `if` branch for `!` in `evaluator.py`.

The modular design keeps changes isolated.

---

## 📜 License

This project is open‑source and available under the **MIT License**.

---

## 🤝 Contributing

Pull requests, bug reports, and feature suggestions are welcome!  
Please follow the existing modular structure.

---

## 📬 Contact

Maintainer: [LelexTB] – [lelextb@gmail.com]  
GitHub: [@lelextb](https://github.com/lelextb)

