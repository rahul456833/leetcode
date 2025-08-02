class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]  # Start with homepage
        self.current = 0  # Pointer to current page

    def visit(self, url: str) -> None:
        # Erase forward history
        self.history = self.history[:self.current + 1]
        # Add new page and move pointer
        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        # Move back but don't go below 0
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        # Move forward but don't go past the end
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]
