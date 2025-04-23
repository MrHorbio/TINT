# 🕵️‍♂️ TINT: Target Information Gathering Tool

<p align="center">
  <img src="https://github.com/MrHorbio/TINT/TINT/static/banner.png" alt="TINT Banner" width="200px" />
</p>

<p align="center">
  <strong>Automate your recon tasks and gather valuable data from the internet.</strong>
</p>

<p align="center">
  📌 Developed by: <strong>Ankush Kumar Rajput</strong> <br>
  <img src="https://img.shields.io/badge/version-1.0-blue?style=flat-square" alt="Version">
  <img src="https://img.shields.io/badge/status-active-brightgreen?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/license-MIT-yellow?style=flat-square" alt="License">
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#️-installation">Install</a> •
  <a href="#-cli-usage">CLI Usage</a> •
  <a href="#-UI-Preview">UI-Preview</a> •
  <a href="#-license">License</a> •
  <a href="https://medium.com/@hrofficial62">Join Medium</a>
</p>


---

## 🧠 Description

**TINT** is a Python-based recon toolkit designed for ethical hackers, bug bounty hunters, and OSINT professionals. It simplifies reconnaissance tasks such as subdomain enumeration, DNS resolution, redirection tracking, WHOIS lookups, and more — all from your terminal.


---

## 🔍 Features

- 🧠 **Host Discovery** — Check if hosts are alive
- 🌐 **Subdomain Enumeration** — From `crt.sh` or brute-force
- 🔁 **Redirection Checker** — Track full redirection chains
- 📊 **Status Code Checker** — Filter by HTTP status (403, 200, 302, etc.)
- 📜 **WHOIS Lookup** — Get registration and ownership details
- 📡 **DNS Enumeration** — Fetch A, MX, TXT, NS, CNAME records
- ↩️ **Reverse DNS Lookup** — Get domain from IP address
- 🎯 **CLI Friendly** — Simple interface built with `argparse`


---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/MrHorbio/TINT.git
cd TINT

# Install dependencies
pip install -r requirements.txt

# Run the tool
python tint.py
```


---

## 💻 CLI Usage

```bash
python tint.py [module] [options]
```


### Host Discovery

```bash
python tint.py host -d example.com
python tint.py host -iL hosts.txt -t 10
```


### Subdomain Enumeration

```bash 
python tint.py sub -d example.com
python tint.py sub -d example.com -w wordlist.txt
```


### Redirection Check

```bash
python tint.py redir -u https://example.com
python tint.py redir -iL urls.txt
```


### Status Code Filtering

```bash
python tint.py code -u https://example.com -c 200
python tint.py code -i urls.txt -c 403
```


### WHOIS Lookup

```bash
python tint.py whois -d example.com
```


### DNS Records

```bash
python tint.py dns -d example.com
```


### Reverse DNS Lookup

```bash
python tint.py rdns -i 8.8.8.8
```


---

## 📸 UI Preview

| UI Preview | Terminal Mode |
|------------|---------------|
| <img src="https://your-desktop-screenshot-url.com" width="400"/> | <img src="https://your-terminal-screenshot-url.com" width="400"/> |


---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


---

## 🤝 Join the Community

Join our community on Discord for support and discussions: [Medium](https://medium.com/@hrofficial62)