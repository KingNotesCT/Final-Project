
---

## ✅ `reflection.md`

```markdown
# Project Reflection

### What part of the project was hardest?
The hardest part of this project was organizing the code across multiple files while keeping everything connected. At first, it was confusing to decide which functions belonged in which file. I had to make sure that imports were correct and that each file only handled one responsibility. Debugging import errors between `main.py`, `inventory_manager.py`, and `file_manager.py` took time, but once I understood how Python modules work, it became much easier.

### What bug took the longest to solve?
The longest bug to fix was the “cannot import load_data from file_manager” error. It turned out that I had accidentally pasted browser metadata into my Python file, which broke the syntax. I learned that even a few stray lines of invalid text can stop Python from reading the file correctly. After cleaning up the file and checking that the function names matched exactly, the program finally ran without errors.

### How did you organize your code across multiple files?
I divided the program by purpose:
- `models.py` defines the data structures (Product, Vendor, PurchaseOrder).
- `file_manager.py` handles loading and saving data.
- `inventory_manager.py` manages all user actions like adding or editing products and vendors.
- `reports.py` generates summaries and statistics.
- `main.py` controls the menu and connects everything together.
This structure made the program easier to read, test, and maintain.

### How does your save/load system work?
The save/load system uses JSON to store all data. When the program starts, `load_data()` reads `sample_data.json` and converts each dictionary into a class object. When saving, `save_data()` converts those objects back into dictionaries and writes them to the file. This approach keeps the data human-readable and easy to edit if needed. It also prevents data loss between sessions.

### What would you improve if you had another week?
If I had another week, I would add input validation and a search feature that lets users find products by name or category more easily. I’d also improve the user interface by formatting reports into tables and adding color-coded output for low-stock warnings. Another improvement would be adding vendor email integration so the program could automatically send purchase orders. Finally, I’d refactor the code to include more error handling and possibly a graphical interface using Tkinter.

---

**Word Count:** ~430 words  
**Author:** Connor Tipton  
**Course:** CIS IT-070
