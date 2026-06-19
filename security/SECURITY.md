# Security

Report security concerns through repository issues only when they do not expose secrets.

Do not publish credentials, tokens, private keys, customer data, or private operational data.

qxvi is a public surface layer. It should not store production secrets.

Security boundary:

- public profile objects
- public manifests
- public schemas
- public documentation
- public workflow validation

No private runtime secret belongs in this repository.
