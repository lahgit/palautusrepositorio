class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _stringify_list(self, items):
        return "\n".join(f"- {item}" for item in items) if items else "-"

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description or '-'}\n"
            f"License: {self.license}\n\n"
            f"Authors:\n{self._stringify_list(self.authors)}\n\n"
            f"Dependencies:\n{self._stringify_list(self.dependencies)}\n\n"
            f"Development dependencies:\n{self._stringify_list(self.dev_dependencies)}"
        )
