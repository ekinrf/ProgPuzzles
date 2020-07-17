def simplify_path(path: str):
    def find_section_end(path_section):
        if path_section:
            if path_section == '..':
                if canonical_path:
                    canonical_path.pop()
            elif path_section != '.':
                canonical_path.append(path_section)

    path_section = ''
    canonical_path = []
    for ch in path:
        if ch == '/':
            find_section_end(path_section)
            path_section = ''
        else:
            path_section += ch
    find_section_end(path_section)
    return '/' + '/'.join(canonical_path)


def simplify_path2(path: str):
    sections = [p for p in path.split('/') if p != '.']
    valid_paths = []
    for s in sections:
        if s == '..':
            if valid_paths:
                valid_paths.pop()
        else:
            valid_paths.append(s)
    return '/' + '/'.join(valid_paths)


print(simplify_path('/a/./b/../../c/'))
print(simplify_path('/a//b////c/d//././/..'))
print(simplify_path('/../'))
print(simplify_path("/..."))