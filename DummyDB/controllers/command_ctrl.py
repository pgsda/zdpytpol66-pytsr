import re


class CommandCtrl:
    def analyze_command(self, command):
        patterns = {
            'CD': r'CREATE DOCUMENT (\w+) \(([\w\s\,]+)\)'
        }

        found_command = None
        match = None
        doc, cols = None, None

        for c, p in patterns.items():
            match = re.search(p, command)
            if match is not None:
                found_command = c
                break

        if found_command == 'CD':
            doc = match.group(1)
            cols = re.split(r'\s+,\s+', match.group(2))

        return found_command, doc, cols
