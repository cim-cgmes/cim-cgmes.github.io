# WorkLocation

Information about a particular location for various forms of work.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Location <|-- WorkLocation
    Location : +CoordinateSystem CoordinateSystem[1]
    Location : +PositionPoint PositionPoints[0..n]
    Location : +PowerSystemResource PowerSystemResources[1]
    Location : +StreetAddress mainAddress[0..1]
    click Location href "Location"
    WorkLocation <|-- ServiceLocation
    click ServiceLocation href "ServiceLocation"
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| No attributes | | | |

