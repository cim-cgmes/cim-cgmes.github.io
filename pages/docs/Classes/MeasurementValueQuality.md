# MeasurementValueQuality

Measurement quality flags. Bits 0-10 are defined for substation automation in IEC 61850-7-3. Bits 11-15 are reserved for future expansion by that document. Bits 16-31 are reserved for EMS applications.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Quality61850 <|-- MeasurementValueQuality
    Quality61850 : +Boolean badReference[0..1]
    Quality61850 : +Boolean estimatorReplaced[0..1]
    Quality61850 : +Boolean failure[0..1]
    Quality61850 : +Boolean oldData[0..1]
    Quality61850 : +Boolean operatorBlocked[0..1]
    Quality61850 : +Boolean oscillatory[0..1]
    Quality61850 : +Boolean outOfRange[0..1]
    Quality61850 : +Boolean overFlow[0..1]
    Quality61850 : +Source source[0..1]
    Quality61850 : +Boolean suspect[0..1]
    Quality61850 : +Boolean test[0..1]
    Quality61850 : +Validity validity[0..1]
    click Quality61850 href "Quality61850"
    MeasurementValueQuality : +MeasurementValue MeasurementValue[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| MeasurementValue | [MeasurementValue](MeasurementValue.md) | 1 | A MeasurementValue has a MeasurementValueQuality associated with it. |

