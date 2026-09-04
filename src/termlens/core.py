import re
_ANSI=re.compile(r'\x1b\[[0-?]*[ -/]*[@-~]')
def visible_length(text: str) -> int:
    """Return terminal-visible character count, excluding ANSI escape sequences."""
    return len(_ANSI.sub('',text))
