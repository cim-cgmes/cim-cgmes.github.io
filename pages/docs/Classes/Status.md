# Status

Current status information relevant to an entity.

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| dateTime | DateTime | 0..1 | Date and time for which status 'value' applies. |
| reason | String | 0..1 | Reason code or explanation for why an object went to the current status 'value'. |
| remark | String | 0..1 | Pertinent information regarding the current 'value', as free form text. |
| value | String | 0..1 | Status value at 'dateTime'; prior status changes may have been kept in instances of activity records associated with the object to which this status applies. |

