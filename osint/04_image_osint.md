# 4. Image OSINT

## Reverse Image Search

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
| **Yandex** | yandex.com/images | Best for similar faces/images |
| **TinEye** | tineye.com | Good for finding image origins |


## EXIF Data Analysis

**EXIF** (Exchangeable Image File Format) contains metadata embedded in images:
- Device type (camera/phone model, serial numbers)
- GPS coordinates (where photo was taken)
- Date/time taken (when photo was taken)
- Camera settings
- Software used

EXIF data can be viewed:
- on the web, e.g. [exif.regex.info](https://exif.regex.info) (Jeffrey's Image Metadata Viewer)
- with command line, e.g. on Linux with `exiftool` command

### Example case study

Photo uploaded to website has these EXIF data:
  - Device: Apple iPhone 4S
  - Date: March 11, 2012
  - Location: Wildwood, Toledo, Ohio (exact coordinates)
  - Context: Walking dog in park

Information extracted:
1. Had a dog
2. Owned iPhone 4S at some point
3. Was in Toledo, Ohio on specific date
4. Regular visitor to that park

### Limitations

Most modern platforms (e.g. Facebook, Instagram, Twitter) now remove EXIF data automatically. This does not happen on photos sent via email, for example.



## Location OSINT (GeoGuessing)

Identifying geographical locations from photos without EXIF data.

### Key Indicators to Analyze

- **Vehicle Analysis**
   - Car brand/model - Some brands regional
   - Steering wheel position - Left = right-hand traffic countries
   - Parking side - Indicates traffic direction
   - License plates - Country/state specific formats

- **Environmental Clues**
   - Snow/weather - Rules out certain regions
   - Vegetation - Plant types indicate climate
   - Architecture style - Building designs vary by region
   - Street signs - Language, design, colors

- **Infrastructure**
   - Road markings - Different by country
   - Traffic lights - Design variations
   - Street signs - Language and style
   - Power lines/poles - Design differences

- **Cultural Elements**
   - Language on signs
   - Store names/brands
   - Clothing styles
   - Advertising

Using Google Earth can be useful to look at older imagery.

Practice on [GeoGuessr](https://geoguessr.com)
