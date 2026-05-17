# PFVArType2IEEEVArController

IEEE VAR controller type 2 which is a summing point type controller. It makes up the outside loop of a two-loop system. This controller is implemented as a slow PI type controller, and the voltage regulator forms the inner loop and is implemented as a fast controller. Reference: IEEE 421.5-2005, 11.5.

## Inheritance

```mermaid
classDiagram
    PFVArControllerType2Dynamics <|-- PFVArType2IEEEVArController
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| exlon | Boolean | 1..1 | Overexcitation or under excitation flag (EXLON) true = 1 (not in the overexcitation or underexcitation state, integral action is active) false = 0 (in the overexcitation or underexcitation state, so integral action is disabled to allow the limiter to play its role). |
| ki | Float | 1..1 | Integral gain of the pf controller (KI). |
| kp | Float | 1..1 | Proportional gain of the pf controller (KP). |
| qref | Float | 1..1 | Reactive power reference (QREF). |
| vclmt | Float | 1..1 | Maximum output of the pf controller (VCLMT). |
| vref | Float | 1..1 | Voltage regulator reference (VREF). |
| vs | Float | 1..1 | Generator sensing voltage (VS). |

