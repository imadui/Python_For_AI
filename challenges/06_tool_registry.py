"""Challenge 06 — tiny tool registry."""


class Tool:
    def __init__(self, name: str, description: str):
        # TODO
        pass


class ToolRegistry:
    def __init__(self):
        # TODO
        pass

    def add(self, tool: Tool) -> None:
        # TODO
        pass

    def get(self, name: str) -> Tool | None:
        # TODO
        pass

    def list_names(self) -> list[str]:
        # TODO
        pass


# Requirements:
# - Add search, calculator, and weather tools.
# - Reject duplicate tool names with ValueError.
# - get("missing") returns None.
# - No inheritance is needed.
