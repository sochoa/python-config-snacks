import copy
import dataclasses
import os
import re


@dataclasses.dataclass
class Placeholder:
    base: str
    placeholder_start: str = "${"
    placeholder_end: str = "}"

    def wrap_as_placeholder(self, k):
        return "".join([self.placeholder_start, k, self.placeholder_end])

    def get_possible_matches(self):
        matches = [
            self.wrap_as_placeholder(self.base),
            self.wrap_as_placeholder(self.base.lower()),
            self.wrap_as_placeholder(self.base.upper()),
        ]
        return set(matches)


def parse(d, **kwargs) -> dict:

    def should_include(i): return any(regexp.search(i) for regexp in whitelist)
    whitelist_patterns = kwargs.get('whitelist_patterns', ['.+'])
    whitelist = [re.compile(p) for p in whitelist_patterns]

    placeholder_dict = {}
    placeholder_start = kwargs.get("placeholder_start", "${")
    placeholder_end = kwargs.get("placeholder_end", "}")
    for k, v in d.items():
        if should_include(k):
            placeholder_kwargs = {
                "base": k,
                "placeholder_start": placeholder_start,
                "placeholder_end": placeholder_end,
            }
            for m in Placeholder(**placeholder_kwargs).get_possible_matches():
                placeholder_dict[m] = v

    return placeholder_dict


def render(d, placeholders):
    n = copy.deepcopy(d)
    for k, v in n.items():

        if hasattr(v, 'items'):
            n[k] = render(v, placeholders)
            continue

        if isinstance(v, str):
            for placeholder, new_val in placeholders.items():
                if placeholder in v:
                    n[k] = v.replace(placeholder, new_val)
    return n
