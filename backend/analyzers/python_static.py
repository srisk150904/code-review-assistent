import ast
from typing import Any, Dict, List

def _cyclomatic_complexity(node: ast.AST) -> int:
    # crude approximation: count branching nodes
    branch_nodes = (ast.If, ast.For, ast.While, ast.And, ast.Or, ast.Try, ast.With, ast.BoolOp, ast.IfExp)
    return sum(isinstance(n, branch_nodes) for n in ast.walk(node)) + 1

def analyze_python(source: str) -> Dict[str, Any]:
    findings: Dict[str, Any] = {"functions": [], "module": {}}
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        findings["module"]["syntax_error"] = f"{e.msg} at line {e.lineno}"
        return findings

    # module-level heuristics
    lines = source.splitlines()
    findings["module"]["line_count"] = len(lines)
    findings["module"]["has_shebang"] = lines[0].startswith("#!") if lines else False
    findings["module"]["has_main_guard"] = any(
        isinstance(n, ast.If) and isinstance(n.test, ast.Compare)
        and getattr(getattr(n.test.left, "id", None), "lower", lambda: "" )() == "__name__"
        for n in ast.walk(tree)
    )

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            name = node.name
            args = len(getattr(node.args, "args", []))
            doc = ast.get_docstring(node)
            complexity = _cyclomatic_complexity(node)
            too_many_locals = len({n.id for n in ast.walk(node) if isinstance(n, ast.Name)}) > 12
            findings["functions"].append({
                "name": name,
                "args": args,
                "has_docstring": bool(doc),
                "cyclomatic_complexity": complexity,
                "too_many_locals_flag": too_many_locals,
                "line_start": getattr(node, "lineno", None),
            })

    # simple smells
    findings["module"]["long_lines_over_120"] = sum(len(l) > 120 for l in lines)
    findings["module"]["tabs_used"] = any("\t" in l for l in lines)
    return findings
