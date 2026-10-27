# laun

A small, safe launch workflow scaffold.

The included launcher validates token metadata and produces a dry-run plan. It does not accept private keys, sign transactions, trade, snipe, or distribute assets.

## Run

```bash
python3 launcher.py --name Example --symbol EX
```

The browser UI is deployable as a static Vercel site with a serverless validation endpoint.
