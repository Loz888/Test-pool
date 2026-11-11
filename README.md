# Test-pool

A public sandbox containing only synthetic, dependency-free test code.

This tiny sample provides a reproducible repository snapshot and a safe target
for later branch, pull-request, and CI experiments. It does not contain the
application under test, production data, credentials, or recorded webhooks.

## Run locally

Requires Python 3.10 or newer. No packages need to be installed.

```sh
python -m unittest discover -s tests -v
```

The sample totals integer point values for a made-up game. Booleans and
non-integers are rejected to keep its behavior explicit.

## Scope of these tests

The tests verify only this synthetic sample. Passing them does **not** verify
a GitHub App, webhook signatures, installation permissions, event delivery,
identity attribution, replay handling, or any SA05 acceptance gate.

No Actions workflow, GitHub App, webhook, deployment, Issue, or pull request is
configured or created by these files. Live platform experiments need their own
configuration, authorization, and evidence. Do not put secrets, private source,
personal data, or raw delivery payloads in this public repository.
