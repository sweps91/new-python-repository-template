# Security Policy

## Reporting a Vulnerability

...

---

## Development Security Practices

This section describes how the project maintains supply chain and code security internally.

### 1. Dependency Locking — `uv.lock`

All dependencies are locked via `uv.lock`, which records exact versions and hashes for every
package in the dependency tree. This ensures fully reproducible installs and protects against
silent dependency changes.

```sh
uv sync   # installs exact versions from uv.lock
```

### 2. Version Pinning — `pyproject.toml`

Direct dependencies are pinned to exact versions using the `==` specifier in `pyproject.toml`.
This prevents unintended upgrades during environment setup.

```toml
[project]
dependencies = [
    "httpx==0.27.0",
    "pydantic==2.7.1",
]
```

### 3. Capped Dependency Resolution — `uv.toml`

The `uv.toml` configuration uses the `exclude-newer` parameter to prevent resolving packages
published after a specified date. This reduces exposure to recently introduced malicious or
broken packages.

```toml
[pip]
exclude-newer = "14 days"
```

### 4. Dependency Auditing — `pip-audit`

Dependencies should be regularly audited for known CVEs using
[`pip-audit`](https://github.com/pypa/pip-audit):

```sh
uv run pip-audit
```

It is recommended to run `pip-audit` as part of CI on every pull request.

### 5. Static Code Analysis — Ruff (Security Rules)

The project uses [Ruff](https://docs.astral.sh/ruff/) with the `S` (flake8-bandit) ruleset
enabled in `ruff.toml` to catch common security anti-patterns at lint time.

```toml
[lint]
select = ["S"]
```

This covers issues such as hardcoded secrets, unsafe deserialization, shell injection risks,
and use of deprecated cryptographic functions. 

It is recommended to enforce linting rules in CI on every pull request.

### 6. Requirements File Generation — `uv export`

If a `requirements.txt` file is needed (e.g. for deployment or tooling that does not support
`uv.lock`), it **must always be generated directly from `uv.lock`** — never maintained by hand
or produced via `pip freeze`.

```sh
# create/update requirements.txt
uv sync
uv export --locked --format requirements-txt --no-dev --output-file requirements.txt
```

This guarantees that `requirements.txt` is always consistent with the locked dependency tree,
including verified hashes.
