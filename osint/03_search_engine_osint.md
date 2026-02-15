# 3. Search Engine OSINT

## Overview

Search engines are typically the **first step** in any OSINT investigation. This section covers operators and techniques for effective searching.

## Major Search Engines

| Engine | Best For | Notes |
|--------|----------|-------|
| **Google** | General OSINT, people, businesses | Most comprehensive for US/European content |
| **DuckDuckGo** | Privacy-focused searches | Less precise than Google |
| **Bing** | Alternative results | Good secondary source |
| **Yandex** | **Image search** | Russian-based, excellent for finding similar images |
| **Baidu** | Asian content | Chinese-based, limited Western content |

**Recommendation:** Always check multiple search engines - they return different results.

## Google Search Operators

### Basic Operators

| Operator | Function | Example |
|----------|----------|---------|
| `" "` | Exact phrase search | `"John Smith"` |
| `AND` | Both terms required | `john AND smith` |
| `OR` | Either term | `john OR jonathan` |
| `*` | Wildcard | `the * mentor` |
| `-` | Exclude term | `john -doe` |

### Site-Specific Operators

| Operator | Function | Example |
|----------|----------|---------|
| `site:` | Search specific domain | `site:reddit.com` |
| `filetype:` | Specific file format | `filetype:pdf` |
| `inurl:` | Word in URL | `inurl:password` |
| `intext:` | Word in page text | `intext:password` |
| `intitle:` | Word in page title | `intitle:admin` |

### Practical Examples

**1. Search specific site only:**
```
WGU C958 site:reddit.com
```

**2. Exclude subdomains:**
```
site:tesla.com -www
```

**3. Find file types:**
```
password filetype:pdf site:tesla.com
```

**4. Find specific document types:**
```
tesla password filetype:xlsx
```

**5. Find subdomains:**
```
site:tesla.com -www -shop -forms
```

## Advanced Search Techniques

### Finding Passwords & Sensitive Data

**Real-world example:** A bug bounty hunter found Tesla credentials by searching:
```
site:tesla.com password
```

This led to exposed ServiceNow credentials in the ticketing system.

**Other search patterns:**
```
filetype:docx password
tesla filetype:csv pwd
site:company.com confidential filetype:pdf
```

### Finding Subdomains

```
site:target.com -www
site:target.com -www -shop -blog
```

This reveals:
- api.target.com
- dev.target.com
- admin.target.com

### Eliminating Results

**Example - Remove specific terms:**
```
"Heath Adams" -"cyber mentor" -mentor
```

This shows different "Heath Adams" people (lawyers, doctors, etc.)

## Time-Based Searching

Use Google's **Tools** menu to filter by time:
- Past hour
- Past 24 hours
- Past week
- Custom range

**Useful for:**
- Finding recent posts
- Monitoring ongoing situations
- Tracking when information first appeared

## Google Advanced Search

Alternative to operators: [google.com/advanced_search](https://google.com/advanced_search)

**Features:**
- Fill-in form (no operators needed)
- Language filters
- Region filters
- File type selection
- Last update filters

## Image Search Integration

Search operators work with Google Images too:
- Filter by time
- Filter by usage rights
- Tools for reverse image search

## Pro Tips

1. **Combine operators** for precise results
2. **Use quotes** for exact phrases
3. **Always verify** across multiple search engines
4. **Check cached versions** if pages are removed
5. **Use Google Advanced Search** when operators are complex
6. **Practice on yourself first** - search your own name and see what you find

## Real-World Application

**Bug Bounty Example:**
1. Search: `site:tesla.com password filetype:pdf`
2. Found: Exposed password document
3. Reported: Credentials for internal system
4. Result: Valid bug bounty

**Investigation Example:**
1. Search: `site:twitter.com "target name"`
2. Combine: `intext:password "target name"`
3. Analyze: Cross-reference results
4. Report: Compile findings

## Google Dorking (Advanced)

**Warning:** These searches can reveal sensitive data. Use ethically and legally.

**Common dorks:**
```
intitle:"index of" "config.json"
inurl:admin.php
filetype:sql "INSERT INTO"
site:pastebin.com "password"
```
