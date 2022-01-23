# Installing gh on Linux and BSD

Packages downloaded from https://cli.github.com or from https://github.com/cli/cli/releases are considered official binaries. We focus on popular Linux distros and the following CPU architectures: i386, amd64, arm64, armhf.

Other sources for installation are community-maintained and thus might lag behind our release schedule.

## Official sources

### Debian, Ubuntu Linux, Raspberry Pi OS (apt)

**Install:**

```bash
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
```
**Upgrade:**

```bash
sudo apt update
sudo apt install gh
```
