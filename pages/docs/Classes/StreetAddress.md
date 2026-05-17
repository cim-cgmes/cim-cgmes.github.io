# StreetAddress

General purpose street and postal address information.

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| language | String | 0..1 | The language in which the address is specified, using ISO 639-1 two digit language code. |
| poBox | String | 0..1 | Post office box. |
| postalCode | String | 0..1 | Postal code for the address. |
| status | [Status](Status.md) | 0..1 | Status of this address. |
| streetDetail | [StreetDetail](StreetDetail.md) | 0..1 | Street detail. |
| townDetail | [TownDetail](TownDetail.md) | 0..1 | Town detail. |

