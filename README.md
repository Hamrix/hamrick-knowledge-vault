# Hamrick Knowledge Vault

This repository is the canonical memory layer for ChatGPT Work, OpenClaw, and Obsidian.

## Operating model

- **Obsidian** stores durable knowledge, evidence, decisions, and project state.
- **ChatGPT Work** researches, reasons, audits, drafts, and creates finished artifacts.
- **OpenClaw** performs local capture, filing, scheduled summaries, and Git synchronization.
- **GitHub** provides version history, backup, review, and ChatGPT repository access.

## First launch

1. Extract this folder to a permanent location, such as:
   `C:\Users\<you>\Documents\Hamrick-Knowledge-Vault`
2. In Obsidian, choose **Open folder as vault**.
3. Run `Setup-Windows.ps1` in PowerShell.
4. Create a **private empty GitHub repository** named `hamrick-knowledge-vault`.
5. Follow the commands printed by the setup script.
6. Connect that repository to ChatGPT through the GitHub plugin/app.
7. Create a ChatGPT Project called **Knowledge Command Center** and paste the contents of `00 System/ChatGPT Work Instructions.md` into its project instructions.

## Core rule

ChatGPT memory is convenient. This vault is authoritative.
