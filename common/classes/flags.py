class Flags:
    def __init__(self, flags=None) -> None:
        self.flags = flags or []

    def set(self, flag):
        existing = self.get(flag)

        if existing:
            self.flags.remove(flag)

        self.flags.append(flag)

    def get(self, flag):
        try:
            existing = self.flags.index(flag)
        except ValueError:
            existing = None

        return False if existing is None else True

    def remove(self, flag):
        existing = self.get(flag)
        if not existing:
            return False
        else:
            return self.flags.pop(self.flags.index(flag))
