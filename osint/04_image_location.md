# 4. Image & Location OSINT

## Part 1: Reverse Image Search

### Overview
Reverse image search allows you to:
- Find where an image appears online
- Identify fake/catfish profiles
- Find similar images
- Trace image origins

### Primary Tools

| Tool | URL | Best Feature |
|------|-----|--------------|
| **Google Images** | images.google.com | Most comprehensive results |
| **Yandex** | yandex.com/images | **Best for similar faces/images** |
| **TinEye** | tineye.com | Good for finding image origins |

### How to Use

**Google Images:**
1. Go to images.google.com
2. Click camera icon (search by image)
3. Upload image or paste URL
4. Review results

**Yandex:**
1. Go to yandex.com
2. Click Images
3. Upload or drag image
4. Check "Similar images" section

### Key Differences

**Google:**
- Best for exact matches
- Good for identifying people/objects
- Shows similar sized images

**Yandex:**
- **Superior for finding similar faces**
- Finds variations of the same photo
- Useful for missing persons cases
- Can identify same person in different contexts

**TinEye:**
- Good for finding earliest instances
- Shows where image first appeared
- Different algorithm than Google/Yandex

### Use Cases

**1. Catfish Investigation:**
- Receive suspicious dating profile photo
- Reverse search on all three engines
- Find real owner of photo
- Confirm fake profile

**2. Social Media Verification:**
- Check if influencer photos are stolen
- Verify authenticity of images
- Find original source

**3. Finding Additional Photos:**
- Start with one photo of target
- Use Yandex to find similar photos
- Discover more instances/images of person

## Part 2: EXIF Data Analysis

### What is EXIF Data?

EXIF (Exchangeable Image File Format) contains metadata embedded in images:
- Device type (camera/phone model)
- GPS coordinates
- Date/time taken
- Camera settings
- Software used

### Privacy Warning

EXIF data can reveal:
- **Exact location** where photo was taken
- **Device information** (model, serial numbers)
- **Personal habits** (time patterns)

### Tools for EXIF Analysis

**Web-based:**
- [exif.regex.info](https://exif.regex.info) (Jeffrey's Image Metadata Viewer)

**Command line (Linux):**
- `exiftool` - Professional EXIF reader

### What to Look For

**Critical Fields:**
- **GPS Latitude/Longitude** - Exact location
- **Date/Time Original** - When photo taken
- **Make/Model** - Device information
- **Software** - Editing software used

### Example Findings

**Real Case Study:**
- Photo uploaded to website
- EXIF data revealed:
  - Device: Apple iPhone 4S
  - Date: March 11, 2012
  - Location: Wildwood, Toledo, Ohio (exact coordinates)
  - Context: Walking dog in park

**Information extracted:**
1. Had a dog
2. Owned iPhone 4S at some point
3. Was in Toledo, Ohio on specific date
4. Regular visitor to that park

### Limitations

**Modern Protection:**
- Facebook, Instagram, Twitter strip EXIF data
- Most platforms now remove GPS data automatically

**Still vulnerable:**
- Photos sent via email
- Photos uploaded to personal blogs/websites
- Raw/unprocessed images

**Best practice:** Always check EXIF data on any photo obtained during investigation.

## Part 3: Location OSINT (GeoGuessing)

### Overview
Identifying geographical locations from photos without EXIF data.

### Key Indicators to Analyze

#### 1. Vehicle Analysis
- **Car brand/model** - Some brands regional
- **Steering wheel position** - Left = right-hand traffic countries
- **Parking side** - Indicates traffic direction
- **License plates** - Country/state specific formats

#### 2. Environmental Clues
- **Snow/weather** - Rules out certain regions
- **Vegetation** - Plant types indicate climate
- **Architecture style** - Building designs vary by region
- **Street signs** - Language, design, colors

#### 3. Infrastructure
- **Road markings** - Different by country
- **Traffic lights** - Design variations
- **Street signs** - Language and style
- **Power lines/poles** - Design differences

#### 4. Cultural Elements
- **Language on signs**
- **Store names/brands**
- **Clothing styles**
- **Advertising**

### Practice Tool: GeoGuessr

**Website:** [geoguessr.com](https://geoguessr.com)

**How it works:**
- Places you in random Google Street View location
- You guess the location on a map
- Score based on distance from actual location

**Benefits:**
- Trains pattern recognition
- Learn regional differences
- Practice without real investigation pressure

### Regional Clues Guide

**Road Markings:**
- Yellow center line: North/South America
- White center line: Europe, most of world
- Dashed patterns vary by country

**Driving Side:**
- Right side: ~75% of world
- Left side: UK, Japan, Australia, India, etc.

**License Plates:**
- EU: Blue stripe on left
- US: State-specific designs
- UK: Yellow rear, white front

**Architecture:**
- European churches: Distinctive steeples
- Asian temples: Pagoda styles
- US suburbs: Similar house designs

### Practice Challenge

**"Where in the World is TCM?"**

Three photos provided:
1. Photo of instructor and wife on bench
2. Rooftop hotel view
3. Street view with building

**Solution approach:**
1. Reverse image search first photo
   - Result: Copley Square, Boston
2. Analyze second photo (rooftop view)
   - Identify: Westin Copley Place hotel
3. Third photo (different location)
   - Look for unique building: PSFS building
   - Result: Philadelphia

**Key takeaway:** Multiple photos together provide context and verification.

## Summary: Image OSINT Workflow

1. **Always check EXIF data first** - Quick win if present
2. **Reverse image search** on all three engines
3. **Analyze visual elements** for location clues
4. **Cross-reference** multiple photos for context
5. **Use GeoGuessr** to practice pattern recognition
