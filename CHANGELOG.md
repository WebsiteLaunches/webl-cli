# Changelog

## [0.2.0] - 2025-11-15

### Breaking Changes
- Changed API field name from `domain_authority` to `site_authority` to align with rebrand to "WebL Site Authority" (WSA)
- This affects JSON and CSV output formats

### Changed
- Updated all formatter references to use `site_authority` field
- Updated README documentation to reflect new terminology

### Migration Guide
If you're parsing JSON or CSV output:
- Change `domain_authority` → `site_authority` in your code
- Change `data['domain_authority']` → `data['site_authority']` for JSON parsing
- Change column name in CSV parsing

## [0.1.0] - 2025-11-01

### Added
- Initial release
- Domain intelligence lookups
- Batch processing support
- Multiple output formats (pretty, JSON, CSV)
- Historical authority tracking
