# 🔐 S-DES Encryption

> The full Simplified-DES cipher in ~100 lines of pure Python — key schedule, both Feistel rounds, S-boxes, and a decrypt round-trip check. No installs, no dependencies. 🔑➡️🔒

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Deps](https://img.shields.io/badge/Dependencies-none-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen)

## ✨ What is this?

An interactive implementation of **S-DES** (Simplified Data Encryption Standard, the teaching cipher from Stallings' *Cryptography and Network Security*): a 10-bit key encrypts one 8-bit block through initial permutation, two Feistel rounds with S-box substitution, and a final inverse permutation — then decrypts it back to prove the round-trip.

| Step | Details |
|---|---|
| 🔑 Key schedule | P10 → split → LS-1 → K1 via P8 → LS-2 → K2 via P8 (verified: `10100100` / `01000011` for the example key) |
| 🔄 Round function | Expand (E/P) → XOR subkey → S0/S1 lookup → P4 |
| 🔁 Feistel | IP → round(K1) → swap → round(K2) → IP⁻¹ (swap only *between* rounds) |
| ✅ Self-check | Every run decrypts the ciphertext and prints it next to the plaintext |
| 🛡️ Input validation | Rejects non-binary keys, wrong lengths, and out-of-range permutation entries |

## ⚡ Try it in 60 seconds

```bash
cd S-DES-Encryption
python S_DES_Algorithm.py
```

Answer the four prompts (or pipe the bundled example non-interactively with PowerShell):

```powershell
"1010000010`n3 5 2 7 4 10 1 9 8 6`n6 3 7 4 8 5 10 9`n10010111" | python S_DES_Algorithm.py
```

## 🔍 Sample output

Using the inputs from `Examples.txt`:

```
Enter 10-bit key (eg. 1010101010): 1010000010
Enter P10 permutation (10 numbers 1-10): 3 5 2 7 4 10 1 9 8 6
Enter P8 permutation (8 numbers 1-10): 6 3 7 4 8 5 10 9
Enter 8-bit plaintext (eg. 10101010): 10010111
Ciphertext: 00111000
Decrypted: 10010111
```

Ciphertext verified against an independent spec-written reference implementation (12 random key/plaintext vectors, all matching), and the subkeys match the textbook values. Decrypting with the wrong key does *not* return the plaintext — the cipher is genuinely key-dependent.

> 📚 S-DES is a **teaching cipher**, not real security — 10-bit keys fall to brute force in milliseconds. Never protect real data with it.

## 🛠️ Tech stack

| Layer | Tech | Why |
|---|---|---|
| Language | Python 3 (stdlib only) | Zero installs — runs anywhere Python exists |
| Cipher | S-DES (Stallings) | The classic classroom Feistel cipher |
| I/O | Interactive `input()` + validation loops | Beginner-friendly, typo-proof prompts |

## 🚀 Quickstart

```bash
cd S-DES-Encryption
python S_DES_Algorithm.py
# 1. enter a 10-bit key, e.g. 1010000010
# 2. enter the P10 permutation (10 numbers 1-10)
# 3. enter the P8 permutation (8 numbers 1-10)
# 4. enter 8-bit plaintext, e.g. 10010111
# → Ciphertext + Decrypted round-trip check
```

## 📁 Project structure

```
S-DES-Encryption/
├── S_DES_Algorithm.py   # Key schedule + encrypt/decrypt + CLI prompts (~100 lines)
├── Examples.txt         # Sample inputs with verified expected output
└── README.md            # You are here 👋
```

## 🗺️ Roadmap

- [ ] Machine-checkable test suite (known-answer vectors)
- [ ] File encrypt/decrypt mode (block chaining over real files)
- [ ] CBC mode option alongside ECB
- [ ] ASCII text helper (string ↔ bits conversion)

## 📄 License

MIT — see [LICENSE](LICENSE). Built by Razen-ByteMaster as a portfolio project. PRs welcome! 🎉