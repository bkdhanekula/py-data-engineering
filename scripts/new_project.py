import os, sys, textwrap

slug = sys.argv[1] if len(sys.argv) > 1 else "new-project"
pkg  = sys.argv[2] if len(sys.argv) > 2 else slug.replace("-", "_")

root = os.path.join("projects", slug, "src", pkg)
tests= os.path.join("projects", slug, "tests")
os.makedirs(root, exist_ok=True)
os.makedirs(tests, exist_ok=True)

readme = f"# {slug}\n\nShort description.\n\n## How to run\n\n```bash\npython -m {pkg} --help\n```\n"
open(os.path.join("projects", slug, "README.md"), "w").write(readme)

pyproject = textwrap.dedent(f"""
[project]
name = "{pkg}"
version = "0.1.0"
requires-python = ">=3.10"
""")
open(os.path.join("projects", slug, "pyproject.toml"), "w").write(pyproject)

open(os.path.join(root, "__init__.py"), "w").write("")
open(os.path.join(tests, "test_sample.py"), "w").write("def test_truth():\n    assert True\n")

print(f"Created projects/{{slug}}")
