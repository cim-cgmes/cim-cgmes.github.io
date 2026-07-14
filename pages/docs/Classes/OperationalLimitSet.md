# OperationalLimitSet

A set of limits associated with equipment. Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain different severities of limit levels that would apply to the same equipment. The set may contain limits of different types such as apparent power and current limits or high and low voltage limits that are logically applied together as a set.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- OperationalLimitSet
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    OperationalLimitSet : +Equipment Equipment[0..1]
    OperationalLimitSet : +OperationalLimit OperationalLimitValue[0..n]
    OperationalLimitSet : +ACDCTerminal Terminal[1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| Equipment | [Equipment](Equipment.md) | 0..1 | The equipment to which the limit set applies. |
| OperationalLimitValue | [OperationalLimit](OperationalLimit.md) | 0..n | Values of equipment limits. |
| Terminal | [ACDCTerminal](ACDCTerminal.md) | 1 | The terminal where the operational limit set apply. |

