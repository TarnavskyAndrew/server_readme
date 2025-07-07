# README Markdown Server

A simple Python HTTP server for previewing your `README.md` files in the browser with clean GitHub-like styles.

<details>
<summary><strong>Show more details</strong></summary>

---

## Features

- Renders Markdown content styled similar to GitHub
- "Refresh" button to reload the content manually
- Minimal dependencies (`markdown` library)
- Simple startup with one command
- Graceful server shutdown with `Ctrl+C`

---

## Installation

Install the `markdown` library:

```bash
pip install markdown
```

---

## How to Run

Navigate to the folder containing the script:

```bash
cd path/to/your/project
```

Start the server:

```bash
python server_readme.py
```

You will see a message:

```
Serving README_dev.md  at http://localhost:8000
```

Open your browser and go to:

```
http://localhost:8000/
```

The rendered Markdown will appear.

---

## Refreshing

Use the **"Refresh"** button at the top-right corner of the page to reload the latest content from `README_dev.md` without restarting the server.

---

## Stopping the Server

To stop the server, focus the terminal window and press:

```
Ctrl + C
```

The server will shut down gracefully.

---

## Project Structure

```
project/
├── server_readme.py   # Main Python server script
├── README_dev.md      # Working file
├── README.md          # This file
```

---

## Possible Enhancements

- Auto-reload when `README_dev.md` changes
- Inline editing and saving from the browser
- Configurable port and file path via command-line arguments

---

Created to simplify Markdown preview during development.

</details>
