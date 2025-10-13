# Python To‑Do List Application

A simple, fast, and dependency‑light **to‑do list app in Python**. Use it from the terminal to add tasks, mark them done, edit, delete, and filter by status or due date. Data is stored locally so your tasks persist between runs.

> Repo: https://github.com/Jonathanch2022/Plython-To-Do-List-Application

---

## Features

- Add tasks with optional **due date** and **priority**
- List tasks (all / active / done)
- Mark tasks **done/undone**
- Edit task title, notes, priority, or due date
- Delete tasks (single or bulk remove done)
- Persistent local storage (JSON or SQLite—see config)
- Clean, testable structure (separate core + CLI)

---

## Quick Start

> Requires **Python 3.10+**

```bash
# 1) Clone
git clone https://github.com/Jonathanch2022/Plython-To-Do-List-Application.git
cd Plython-To-Do-List-Application

# 2) (Optional) Create a virtual environment
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate

# 3) Install dependencies (if requirements.txt is present)
pip install -r requirements.txt

# 4) Run
python app.py --help
```

If your entry file is named differently (e.g., `main.py`), run `python main.py --help`.

---

## CLI Usage

```bash
# Show help
python app.py --help

# Add a task
python app.py add "Buy groceries" --due 2025-10-12 --priority high --note "Milk, eggs, spinach"

# List tasks (default: all)
python app.py list
python app.py list --status active
python app.py list --status done
python app.py list --overdue

# Mark as done / undone
python app.py done 3
python app.py undone 3

# Edit a task
python app.py edit 5 --title "Email recruiter" --note "Attach portfolio" --priority medium --due 2025-10-14

# Delete a task
python app.py delete 7

# Bulk cleanup (remove all done tasks)
python app.py cleanup
```

Typical command output:

```
# ID  Title              Due         Pri  Status
1     Buy groceries      2025-10-12  H    active
2     Finish blog post   -           M    done
3     Read 'Clean Code'  2025-10-20  L    active
```

---

## Configuration

Create a `.todo.cfg` (optional) to choose the storage backend and file locations.

```ini
[storage]
backend = json         # json | sqlite
path = ./data/todos.json

[display]
date_format = %Y-%m-%d
show_ids = true
```

- **JSON backend**: zero‑setup, human‑readable.
- **SQLite backend**: scalable, safe for bigger lists.

---

## Project Structure (suggested)

```
Plython-To-Do-List-Application/
├─ app.py                 # CLI entry-point
├─ todo/
│  ├─ __init__.py
│  ├─ models.py           # Task dataclass / ORM model
│  ├─ storage.py          # JSON/SQLite implementations
│  ├─ services.py         # business logic (add/edit/list/complete)
│  └─ cli.py              # argparse/typer commands
├─ tests/                 # unit tests
├─ requirements.txt
└─ README.md
```

> If your current repo layout differs, this README still applies—the commands and flags are examples that you can align to your code.

---

## Development

```bash
# Lint & format (if using ruff/black)
pip install -r requirements-dev.txt
ruff check .
black .

# Run tests (if pytest configured)
pytest -q
```

---

## Common Issues

- **`ModuleNotFoundError`**: Activate your venv (`.\.venv\Scripts\Activate.ps1`) and reinstall deps.
- **`PermissionError` on Windows**: Avoid saving the database file inside protected folders; try `./data/`.
- **Emoji or Unicode not showing**: Ensure your terminal is UTF‑8 and use a compatible font.

---

## Roadmap

- Recurring tasks
- Natural language due dates (“tomorrow 5pm”)
- Export/Import (CSV/Markdown)
- Optional TUI with `textual` or `urwid`
- Sync to cloud (optional)

---

## License

MIT (recommended). Add your license file to the repo root.

---

## Credits

Built by **Jonathan Hubbard**. Thanks for checking out the project!
