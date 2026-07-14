# DifferenceModel

It represents the difference model header. The content is described by the Model class, the association role forwardDifferences and association role reverseDifferences. Both association roles may have one set of Statements.

## Inheritance

```mermaid
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
    Model <|-- DifferenceModel
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
    DifferenceModel : +N/A forwardDifferences[1..n]
    DifferenceModel : +N/A preconditions[1..n]
    DifferenceModel : +N/A reverseDifferences[1..n]
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| forwardDifferences | N/A | 1..n | A property of the difference model whose value is a collection of statements (i.e., resources of type rdf:Statement) representing the forward difference statements. |
| preconditions | N/A | 1..n | A property of the difference model whose value is the collection of precondition statements. |
| reverseDifferences | N/A | 1..n | A property of the difference model whose value is the collection of reverse difference statements. |

