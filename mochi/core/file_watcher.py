"""File watcher for solution monitoring."""

import time
from pathlib import Path
from typing import Callable, Optional
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent


class SolutionWatcher(FileSystemEventHandler):
    """Watch solution file for changes."""

    def __init__(self, file_path: Path, on_change: Callable):
        self.file_path = file_path.resolve()
        self.on_change = on_change
        self.last_modified = time.time()
        self.debounce_seconds = 1.0  # Avoid multiple triggers

    def on_modified(self, event):
        """Handle file modification events."""
        if isinstance(event, FileModifiedEvent):
            event_path = Path(event.src_path).resolve()
            if event_path == self.file_path:
                current_time = time.time()
                if current_time - self.last_modified > self.debounce_seconds:
                    self.last_modified = current_time
                    self.on_change()


class FileWatcher:
    """Manage file watching."""

    def __init__(self, file_path: Path, on_change: Callable):
        self.file_path = file_path
        self.on_change = on_change
        self.observer: Optional[Observer] = None

    def start(self):
        """Start watching the file."""
        event_handler = SolutionWatcher(self.file_path, self.on_change)
        self.observer = Observer()
        self.observer.schedule(event_handler, str(self.file_path.parent), recursive=False)
        self.observer.start()

    def stop(self):
        """Stop watching the file."""
        if self.observer:
            self.observer.stop()
            self.observer.join()
