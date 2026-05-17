# PowerSystemStabilizerDynamics

Power system stabilizer function block whose behaviour is described by reference to a standard model or by definition of a user-defined model.

## Inheritance

```mermaid
classDiagram
    DynamicsFunctionBlock <|-- PowerSystemStabilizerDynamics
    PowerSystemStabilizerDynamics <|-- PssSH
    PowerSystemStabilizerDynamics <|-- PssELIN2
    PowerSystemStabilizerDynamics <|-- Pss1A
    PowerSystemStabilizerDynamics <|-- PowerSystemStabilizerUserDefined
    PowerSystemStabilizerDynamics <|-- PssWECC
    PowerSystemStabilizerDynamics <|-- PssPTIST3
    PowerSystemStabilizerDynamics <|-- Pss2ST
    PowerSystemStabilizerDynamics <|-- Pss1
    PowerSystemStabilizerDynamics <|-- PssIEEE3B
    PowerSystemStabilizerDynamics <|-- Pss2B
    PowerSystemStabilizerDynamics <|-- PssIEEE2B
    PowerSystemStabilizerDynamics <|-- Pss5
    PowerSystemStabilizerDynamics <|-- PssSB4
    PowerSystemStabilizerDynamics <|-- PssRQB
    PowerSystemStabilizerDynamics <|-- PssSK
    PowerSystemStabilizerDynamics <|-- PssPTIST1
    PowerSystemStabilizerDynamics <|-- PssIEEE1A
    PowerSystemStabilizerDynamics <|-- PssIEEE4B
    PowerSystemStabilizerDynamics <|-- PssSTAB2A
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| ExcitationSystemDynamics | [ExcitationSystemDynamics](ExcitationSystemDynamics.md) | 1 | Excitation system model with which this power system stabilizer model is associated. |
| RemoteInputSignal | [RemoteInputSignal](RemoteInputSignal.md) | 0..n | Remote input signal used by this power system stabilizer model. |

