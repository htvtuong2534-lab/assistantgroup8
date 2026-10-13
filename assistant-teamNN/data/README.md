# Data Sources and Ownership

## `offices.csv`

- **Purpose:** Stores office names, room locations, and opening hours for the assistant's office lookup feature.
- **Source:** Public information published by the official HCMUS website and its office directory.
- **Owner:** Retrieval-data component maintainer.
- **Update frequency:** Review monthly and whenever the university publishes changes.
- **Format:** UTF-8 CSV with the columns `name`, `room`, and `hours`.

### Reference sources

- HCMUS official website: https://hcmus.edu.vn/
- Internal office directory: https://hcmus.edu.vn/danh-ba-dien-thoai-noi-bo/
- Admissions contact page: https://tuyensinh.hcmus.edu.vn/lien-he/

### Data quality rules

1. Use publicly available information only.
2. Verify room locations and opening hours against official sources.
3. Do not invent missing details. Mark them as unavailable or contact the relevant office.
4. Preserve the CSV header and UTF-8 encoding.
5. Check for duplicate office names and run the tests after changing the data.

## Maintenance

The retrieval-data component maintainer is responsible for validating office records, reviewing source links, and updating this document when ownership, sources, or the review schedule changes.