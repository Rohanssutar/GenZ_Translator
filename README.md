# GenZ Translator

**GenZ Translator** is a Python library that converts **Gen Z slang** into plain English.

## Features
- Translates popular Gen Z slang into clear English
- Supports **single-word slang** (`lit -> fun`) and **phrases** (`no cap -> truth`)
- Works both as a **Python library** and (optionally) as a **CLI tool**

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install GenZ Translator
```bash
pip install genztranslator
```

## Usage

```python
import genztranslator

#returns single-word slang meaning
user_input = "This is lit"
print(genztranslator.translate(user_input)) # output: This is fun

#returns phrases meaning
user_input = "This party is lit, fr fr"
print(genztranslator.translate(user_input)) # output: This party is fun, for real for real
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what would you like to change.
