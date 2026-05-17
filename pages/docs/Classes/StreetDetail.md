# StreetDetail

Street details, in the context of address.

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| addressGeneral | String | 0..1 | First line of a free form address or some additional address information (for example a mail stop). |
| addressGeneral2 | String | 0..1 | (if applicable) Second line of a free form address. |
| addressGeneral3 | String | 0..1 | (if applicable) Third line of a free form address. |
| buildingName | String | 0..1 | (if applicable) In certain cases the physical location of the place of interest does not have a direct point of entry from the street, but may be located inside a larger structure such as a building, complex, office block, apartment, etc. |
| code | String | 0..1 | (if applicable) Utilities often make use of external reference systems, such as those of the town-planner's department or surveyor general's mapping system, that allocate global reference codes to streets. |
| floorIdentification | String | 0..1 | The identification by name or number, expressed as text, of the floor in the building as part of this address. |
| name | String | 0..1 | Name of the street. |
| number | String | 0..1 | Designator of the specific location on the street. |
| prefix | String | 0..1 | Prefix to the street name. For example: North, South, East, West. |
| suffix | String | 0..1 | Suffix to the street name. For example: North, South, East, West. |
| suiteNumber | String | 0..1 | Number of the apartment or suite. |
| type | String | 0..1 | Type of street. Examples include: street, circle, boulevard, avenue, road, drive, etc. |
| withinTownLimits | Boolean | 0..1 | True if this street is within the legal geographical boundaries of the specified town (default). |

