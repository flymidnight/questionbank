# questionbank

A content/data pipeline for a certification-exam practice app. It produces the
question-bank data (minified JSON, then encrypted `.enc` files) and image assets
that a **separate** frontend app consumes. There is no web server, database, or
UI in this repository — it is a set of Python CLI scripts plus image assets.

## Cursor Cloud specific instructions

### IMPORTANT: this remote branch (`origin/main`) contains only images

The remote `origin/main` (and the `latest`/`Latest` tags) contains **only image
assets** (`images/<exam-code>/*.png|jpg`) and no Python code. The actual
application code (`config.py`, `encrypt_question_bank.py`, `minify_json_*.py`,
`master.json`) lives on a **divergent local history with no common ancestor**
(local `main`, commit `d6e72d3`). That code history is **not present on the
remote** under any branch or tag, so a fresh clone will not contain it.

If you need to run the pipeline and the working tree only has `images/`, get the
code without disturbing the current branch by adding a worktree from the local
code commit, e.g.:

```bash
git worktree add --detach /home/ubuntu/qbank-run main   # or the code commit SHA
cd /home/ubuntu/qbank-run
```

If local `main` is also gone (e.g. on a brand-new VM), the code is unavailable
and must be restored by the repository owner — flag this rather than guessing.

### Runtime & dependencies

- Pure **Python 3** (tested with 3.12). The only third-party dependency is
  **PyCryptodome** (`Crypto` module), used by `encrypt_question_bank.py`. The
  startup update script installs it (`pip install --user pycryptodome`); the
  minify scripts use only the standard library.
- There is **no** `requirements.txt`, `package.json`, Dockerfile, test suite, or
  configured linter in this repo. "Lint" is just a syntax check
  (`python3 -m py_compile *.py`).

### Running the pipeline (non-obvious gotchas)

- The `JSON/` directory is **git-ignored** and is **not committed**, so input
  question-bank files are absent by default. You must place
  `JSON/<code>_<lang>_exam.json` files there before running anything (or create a
  sample to test). Language suffixes: `en`, `de`, `cn`, `jp`.
- `minify_json_<lang>.py` minifies **in place** — it overwrites the same
  `JSON/<code>_<lang>_exam.json` file. Pass the exam code as the first arg:
  `python3 minify_json_en.py saa-c03`. (With no arg it reads
  `config.exam_name_str`, which is not defined in `config.py`, so always pass the
  code.)
- `encrypt_question_bank.py` resolves its input relative to `./JSON/`, so pass
  only the filename: `python3 encrypt_question_bank.py saa-c03_en_exam.json`. It
  requires the `QUESTION_BANK_SECRET` env var (must match the frontend's
  `utils/cryptoKey.ts`), and writes `JSON/<name>.enc` (gzip of base64 of
  AES-256-ECB ciphertext; the file starts with the gzip magic `1f 8b`).
- Security note: `config.py` contains hardcoded plaintext third-party
  credentials. Avoid pushing it to new remote branches.
