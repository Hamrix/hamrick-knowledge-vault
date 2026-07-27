# Connect GitHub, Obsidian, and ChatGPT Work

## 1. Create the repository

On GitHub, create a **private** repository:

`Hamrix/hamrick-knowledge-vault`

Do not initialize it with a README, license, or `.gitignore`; those files are already included.

## 2. Push the vault

From PowerShell inside the vault folder:

```powershell
git remote add origin https://github.com/Hamrix/hamrick-knowledge-vault.git
git push -u origin main
```

## 3. Open in Obsidian

Choose **Open folder as vault**, then select the extracted folder.

Recommended community plugins:
- Obsidian Git
- Dataview
- Templater
- Tasks

Install only what you need. Do not place authentication tokens in notes.

## 4. Connect to ChatGPT

In ChatGPT:
1. Open plugin/app settings.
2. Connect GitHub.
3. Grant access only to `hamrick-knowledge-vault`.
4. Create a Project named **Knowledge Command Center**.
5. Add the GitHub repository as a source where available.
6. Paste `00 System/ChatGPT Work Instructions.md` into the Project instructions.

## 5. Test

Ask ChatGPT:

> Read the vault operating manual and project dashboard. Summarize the architecture, identify the next three setup actions, and cite the repository files used.

Then ask:

> Draft a new capture note for today's setup session. Do not modify evidence notes.

## 6. OpenClaw

Give OpenClaw access to the local vault path and begin with the policy in `.openclaw/openclaw-policy.yaml`. Keep automatic commits and pushes disabled until inbox-only writes have been tested.
