# GovHydroPelton

Detailed hydro unit - Pelton model. This model can be used to represent the dynamic related to water tunnel and surge chamber. The DetailedHydroModelHydraulicSystem diagram, located under the GovHydroFrancis class, provides a schematic of the hydraulic system of detailed hydro unit models, such as Francis and Pelton.

## Inheritance

```mermaid
classDiagram
    TurbineGovernorDynamics <|-- GovHydroPelton
```
<button class="mermaid-enlarge-button">Enlarge Diagram</button>

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| av0 | Float | 1..1 | Area of the surge tank (AV0). Unit = m2. Typical value = 30. |
| av1 | Float | 1..1 | Area of the compensation tank (AV1). Unit = m2. Typical value = 700. |
| bp | Float | 1..1 | Droop (bp). Typical value = 0,05. |
| db1 | Float | 1..1 | Intentional dead-band width (DB1). Unit = Hz. Typical value = 0. |
| db2 | Float | 1..1 | Intentional dead-band width of valve opening error (DB2). Unit = Hz. Typical value = 0,01. |
| h1 | Float | 1..1 | Head of compensation chamber water level with respect to the level of penstock (H1). Unit = km. Typical value = 0,004. |
| h2 | Float | 1..1 | Head of surge tank water level with respect to the level of penstock (H2). Unit = km. Typical value = 0,040. |
| hn | Float | 1..1 | Rated hydraulic head (Hn). Unit = km. Typical value = 0,250. |
| kc | Float | 1..1 | Penstock loss coefficient (due to friction) (Kc). Typical value = 0,025. |
| kg | Float | 1..1 | Water tunnel and surge chamber loss coefficient (due to friction) (Kg). Typical value = 0,025. |
| qc0 | Float | 1..1 | No-load turbine flow at nominal head (Qc0). Typical value = 0,05. |
| qn | Float | 1..1 | Rated flow (Qn). Unit = m3/s. Typical value = 250. |
| simplifiedPelton | Boolean | 1..1 | Simplified Pelton model simulation (Sflag). true = enable of simplified Pelton model simulation false = enable of complete Pelton model simulation (non-linear gain). Typical value = true. |
| staticCompensating | Boolean | 1..1 | Static compensating characteristic (Cflag). It should be true if simplifiedPelton = false. true = enable of static compensating characteristic false = inhibit of static compensating characteristic. Typical value = false. |
| ta | Float | 1..1 | Derivative gain (accelerometer time constant) (Ta) (>= 0). Typical value = 3. |
| ts | Float | 1..1 | Gate servo time constant (Ts) (>= 0). Typical value = 0,15. |
| tv | Float | 1..1 | Servomotor integrator time constant (Tv) (>= 0). Typical value = 0,3. |
| twnc | Float | 1..1 | Water inertia time constant (Twnc) (>= 0). Typical value = 1. |
| twng | Float | 1..1 | Water tunnel and surge chamber inertia time constant (Twng) (>= 0). Typical value = 3. |
| tx | Float | 1..1 | Electronic integrator time constant (Tx) (>= 0). Typical value = 0,5. |
| va | Float | 1..1 | Maximum gate opening velocity (Va). Unit = PU / s. Typical value = 0,06. |
| valvmax | Float | 1..1 | Maximum gate opening (ValvMax) (> GovHydroPelton.valvmin). Typical value = 1,1. |
| valvmin | Float | 1..1 | Minimum gate opening (ValvMin) (< GovHydroPelton.valvmax). Typical value = 0. |
| vav | Float | 1..1 | Maximum servomotor valve opening velocity (Vav). Typical value = 0,1. |
| vc | Float | 1..1 | Maximum gate closing velocity (Vc). Unit = PU / s. Typical value = -0,06. |
| vcv | Float | 1..1 | Maximum servomotor valve closing velocity (Vcv). Typical value = -0,1. |
| waterTunnelSurgeChamberSimulation | Boolean | 1..1 | Water tunnel and surge chamber simulation (Tflag). true = enable of water tunnel and surge chamber simulation false = inhibit of water tunnel and surge chamber simulation. Typical value = false. |
| zsfc | Float | 1..1 | Head of upper water level with respect to the level of penstock (Zsfc). Unit = km. Typical value = 0,025. |

