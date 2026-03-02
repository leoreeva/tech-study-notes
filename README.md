# Tech Study Notes - Quarkdown Edition

A comprehensive knowledge base for software engineering, data engineering, and related topics, built with [Quarkdown](https://github.com/iamgio/quarkdown).

## 🚀 About

This repository contains study notes, explanations, and resources for various technical topics including:

- Computer Science Fundamentals
- Databases and Data Engineering
- Software Design and Architecture
- System Design
- Cloud Certifications
- OSINT (Open Source Intelligence)
- Deep Web Technologies
- Data Visualization

The content is organized as a Quarkdown-based wiki, providing a structured and navigable knowledge base.

## 📚 Content Structure

```
tech-study-notes/
├── computer_science_fundamentals/  # Core CS concepts
├── databases/                      # Database theories and practices
├── software_design/                 # Design patterns and principles
├── system_design/                   # System architecture
├── data_engineering/                # Data pipelines and infrastructure
├── devops_cicd/                     # DevOps practices
├── cloud_certifications/           # Cloud platform certifications
├── osint/                          # OSINT techniques
├── deep_web/                       # Deep web technologies
├── data_visualization/              # Data presentation techniques
├── images/                         # Shared images
├── output/                         # Compiled output (generated)
├── _nav.qd                         # Navigation structure
├── _setup.qd                       # Global setup
├── main.qd                         # Homepage
└── README.md                       # This file
```

## 🛠️ Getting Started

### Prerequisites

- [Quarkdown installed](https://quarkdown.com/wiki/installation)
- Java 17+ (required for Quarkdown)
- Node.js (required for PDF export)

### Installation

```bash
# Install Quarkdown (follow instructions at https://quarkdown.com/wiki/installation)
# Clone this repository
git clone https://github.com/yourusername/tech-study-notes.git
cd tech-study-notes
```

### Compiling

Compile the entire knowledge base:
```bash
quarkdown c main.qd
```

For live preview during editing:
```bash
quarkdown c main.qd -p -w
```

The compiled output will be in the `output/` directory.

### Viewing

After compilation, open `output/tech-study-notes/index.html` in your browser, or use the preview server:
```bash
quarkdown c main.qd -p
```

## 📖 Navigation

The knowledge base uses Quarkdown's navigation system:

- **Sidebar**: Automatically generated from `_nav.qd`
- **Cross-references**: Links between related topics
- **Search**: Full-text search across all content

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Adding Content

1. Create a new `.qd` file in the appropriate directory
2. Add Quarkdown headers:
   ```markdown
   .docname {Your Title}
   .include {docs}
   ```
3. Write your content using Quarkdown syntax
4. Add your file to `_nav.qd`

### Improving Existing Content

- Fix errors or typos
- Add examples or explanations
- Improve formatting
- Add images or diagrams

### Migration Help

Help migrate Markdown files to Quarkdown format:
- Convert syntax where beneficial
- Add Quarkdown-specific features
- Update internal links

### For AI Agents and Developers

Please refer to [AGENTS.md](AGENTS.md) for comprehensive guidelines on:
- Build/lint/test commands
- Code style guidelines
- File organization
- Version control practices
- Testing approach

## 📝 Writing Guidelines

### Quarkdown Features to Use

- **Document structure**: Use `.docname` and `.include {docs}`
- **Images**: Use `!(widthxheight)[alt text](path)` for sized images
- **Cross-references**: Use `.seealso` for related content
- **Admonitions**: Use `.note`, `.warning`, `.important` etc.
- **Tables**: Enhanced table formatting

### Content Standards

- Use clear, concise language
- Provide practical examples
- Include code samples where relevant
- Reference sources when appropriate
- Use consistent terminology

## 🔧 Technical Details

### Quarkdown Configuration

- **Document Type**: Docs (wiki-style)
- **Theme**: Default Quarkdown theme
- **Output**: HTML with search and navigation

### Build Process

1. Quarkdown compiles `.qd` files to HTML
2. Assets are copied to output directory
3. Navigation is generated from `_nav.qd`
4. Search index is created

## 📄 License

This content is provided for educational purposes. See individual files for specific attribution requirements.

## 🙏 Acknowledgments

- Built with [Quarkdown](https://github.com/iamgio/quarkdown)
- Inspired by various study guides and documentation
- Contributions from the open-source community

## 📬 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Happy learning!** 🚀