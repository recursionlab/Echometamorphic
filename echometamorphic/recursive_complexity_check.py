import ast
import sys


def _node_depth(node: ast.AST, level: int = 0) -> int:
    """Return the depth of nested function definitions within a node."""
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
        level += 1
    max_child = level
    for child in ast.iter_child_nodes(node):
        max_child = max(max_child, _node_depth(child, level))
    return max_child


def check_file(filename: str, max_depth: int = 10) -> int:
    with open(filename, "r", encoding="utf-8") as fh:
        try:
            tree = ast.parse(fh.read(), filename=filename)
        except SyntaxError as err:
            print(f"{filename}: failed to parse ({err})")
            return 1
    depth = _node_depth(tree)
    if depth > max_depth:
        print(f"{filename}: recursive complexity {depth} > {max_depth}")
        return 1
    return 0


def main(argv: list[str] | None = None) -> None:
    argv = argv or sys.argv[1:]
    status = 0
    for path in argv:
        status |= check_file(path)
    sys.exit(status)


if __name__ == "__main__":
    main()
