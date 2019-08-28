# py-release-test
python-semantic-release-testing


## Usage

You need to create a setup.cfg to configure, where you set the software version.

Also define, which git user you want to use.

Commands:

```bash
semantic-release version --patch  # (increments lateste 1.0.1 -> 1.0.2)
semantic-release version --minor  # (increments middle 1.0.1 -> 1.1.0)
semantic-release version --major  # (increments first 1.0.1 -> 2.0.0)
```