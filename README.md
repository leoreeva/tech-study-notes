# Tech Study Notes

**URL: https://tech-study-notes.pages.dev/**

Data engineering / software engineering resources (or even personal interests, not directly related to tech). Useful for interviews or just personal knowledge.

It's built with [Quarkdown](https://github.com/iamgio/quarkdown).

> **Work in progress**: This is an ongoing collection based on my knowledge and interests. Many topics may be intentionally skipped or not yet covered. Contributions are welcome!


## About

This repository contains study notes, explanations, and resources for various technical topics including:

- Computer Science Fundamentals
- Databases and Data Engineering
- Software Design and Architecture
- System Design


## 🛠️ Getting Started

### Prerequisites

- Quarkdown >= 1.15.1

### Installation

```bash
# Install Quarkdown (follow instructions at https://quarkdown.com/wiki/installation)
# Clone this repository
git clone https://github.com/yourusername/tech-study-notes.git
cd tech-study-notes
```

### Compiling

```bash
# compile
quarkdown c main.qd

# preview
quarkdown c main.qd -p

# live preview while editing
quarkdown c main.qd -p -w
```

The compiled output will be in the `output/` directory.

Note: when working locally, before previewing, run `python _scripts/move_images.py`, otherwise media is not rendered correctly (at least on my pc)

### Publishing new release

- create and push new branch `release/vX.X.X`
- in Cloudflare pages:
    - check deployment preview
    - update production branch
    - re-run deployment

### License

Add a license...
