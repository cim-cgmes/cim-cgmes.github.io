# ValueToAlias

Describes the translation of one particular value into a name, e.g. 1 as 'Open'.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    IdentifiedObject <|-- ValueToAlias
    IdentifiedObject : +DiagramObject DiagramObjects[0..n]
    IdentifiedObject : +String description[0..1]
    IdentifiedObject : +String energyIdentCodeEic[0..1]
    IdentifiedObject : +String mRID[1..1]
    IdentifiedObject : +String name[1..1]
    IdentifiedObject : +String shortName[0..1]
    click IdentifiedObject href "IdentifiedObject"
    ValueToAlias : +ValueAliasSet ValueAliasSet[1]
    ValueToAlias : +Integer value[1..1]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ValueAliasSet | [ValueAliasSet](ValueAliasSet.md) | 1 | The ValueAliasSet having the ValueToAlias mappings. |
| value | Integer | 1..1 | The value that is mapped. |

