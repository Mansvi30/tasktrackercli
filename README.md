# Task Tracker CLI

A simple command-line task tracker built with Python.

## Features

- Add tasks
- Update tasks
- Delete tasks
- Mark tasks as todo, in-progress, or done
- List all tasks
- List tasks by status
- Stores tasks in a JSON file
- Automatically creates tasks.json if it doesn't exist

## Requirements

Python 3.x

## Commands

### Add

```bash
python task_cli.py add "Buy groceries"
```

### Update

```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
```

### Delete

```bash
python task_cli.py delete 1
```

### Mark In Progress

```bash
python task_cli.py mark-in-progress 1
```

### Mark Done

```bash
python task_cli.py mark-done 1
```

### List All

```bash
python task_cli.py list
```

### List Todo

```bash
python task_cli.py list todo
```

### List In Progress

```bash
python task_cli.py list in-progress
```

### List Done

```bash
python task_cli.py list done
```

