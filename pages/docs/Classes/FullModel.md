# FullModel

It represents the full model header and its contents is described by the Model class.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Model <|-- FullModel
    Model : +Model DependentOn[0..n]
    Model : +Model Depending[0..n]
    Model : +Model SupersededBy[0..n]
    Model : +Model Supersedes[0..n]
    Model : +DateTime created[1..1]
    Model : +String description[1..1]
    Model : +URI modelingAuthoritySet[1..1]
    Model : +URI profile[1..n]
    Model : +DateTime scenarioTime[1..1]
    Model : +Integer version[1..1]
    click Model href "Model"
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| No attributes | | | |

