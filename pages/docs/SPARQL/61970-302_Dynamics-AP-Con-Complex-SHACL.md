# 61970-302_Dynamics-AP-Con-Complex-SHACL

## dy302c:AsynchronousMachineEquivalentCircuit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AsynchronousMachineEquivalentCircuit

## dy302c:AsynchronousMachineTimeConstantReactance

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AsynchronousMachineTimeConstantReactance

## dy302c:AsynchronousMachineUserDefined

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AsynchronousMachineUserDefined

## dy302c:DiscExcContIEEEDEC1A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DiscExcContIEEEDEC1A

## dy302c:DiscExcContIEEEDEC2A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DiscExcContIEEEDEC2A

## dy302c:DiscExcContIEEEDEC3A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DiscExcContIEEEDEC3A

## dy302c:ExcAC1A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAC1A

## dy302c:ExcAC2A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAC2A

## dy302c:ExcAC3A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAC3A

## dy302c:ExcAC4A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAC4A

## dy302c:ExcAC5A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAC5A

## dy302c:ExcAC6A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAC6A

## dy302c:ExcAC8B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAC8B

**Nested Properties:**

### dy302c:ExcAC8B.kpr-valueRange

**Path:** `cim:ExcAC8B.kpr`  
**Name:** C:302:DY:ExcAC8B.kpr:valueRange  
Voltage regulator proportional gain (Kpr) (> 0 if ExcAC8B.kir = 0).  Typical value = 80.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:ExcAC8B.kir ?kir .
        FILTER (?kir=0 && ?value<=0) .        
			}
```
  - Messages: `["The value negative or zero when ExcAC8B.kir = 0."]`

## dy302c:ExcANS

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcANS

## dy302c:ExcAVR1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAVR1

## dy302c:ExcAVR2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAVR2

## dy302c:ExcAVR3

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAVR3

## dy302c:ExcAVR4

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAVR4

## dy302c:ExcAVR5

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAVR5

## dy302c:ExcAVR7

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcAVR7

## dy302c:ExcBBC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcBBC

**Nested Properties:**

### dy302c:ExcBBC.k-valueRange

**Path:** `cim:ExcBBC.k`  
**Name:** C:302:DY:ExcBBC.k:valueRange  
Steady state gain (K) (not = 0).  Typical value = 300.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        FILTER (?value=0) .        
			}
```
  - Messages: `["The value is 0."]`

## dy302c:ExcCZ

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcCZ

## dy302c:ExcDC1A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcDC1A

## dy302c:ExcDC2A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcDC2A

## dy302c:ExcDC3A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcDC3A

## dy302c:ExcDC3A1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcDC3A1

## dy302c:ExcELIN1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcELIN1

## dy302c:ExcELIN2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcELIN2

## dy302c:ExcHU

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcHU

## dy302c:ExcIEEEAC1A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEAC1A

## dy302c:ExcIEEEAC2A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEAC2A

## dy302c:ExcIEEEAC3A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEAC3A

## dy302c:ExcIEEEAC4A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEAC4A

## dy302c:ExcIEEEAC5A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEAC5A

## dy302c:ExcIEEEAC6A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEAC6A

## dy302c:ExcIEEEAC7B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEAC7B

**Nested Properties:**

### dy302c:ExcIEEEAC7B.kpa-valueRange

**Path:** `cim:ExcIEEEAC7B.kpa`  
**Name:** C:302:DY:ExcIEEEAC7B.kpa:valueRange  
Voltage regulator proportional gain (K<sub>PA</sub>) (> 0 if ExcIEEEAC7B.kia = 0).  Typical value = 65,36.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:ExcIEEEAC7B.kia ?kia .
        FILTER (?kia=0 && ?value<=0) .        
			}
```
  - Messages: `["The value negative or zero when ExcIEEEAC7B.kia = 0."]`

### dy302c:ExcIEEEAC7B.kpr-valueRange

**Path:** `cim:ExcIEEEAC7B.kpr`  
**Name:** C:302:DY:ExcIEEEAC7B.kpr:valueRange  
Voltage regulator proportional gain (K<sub>PR</sub>) (> 0 if ExcIEEEAC7B.kir = 0).  Typical value = 4,24.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:ExcIEEEAC7B.kir ?kir .
        FILTER (?kir=0 && ?value<=0) .        
			}
```
  - Messages: `["The value negative or zero when ExcIEEEAC7B.kir = 0."]`

## dy302c:ExcIEEEAC8B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEAC8B

**Nested Properties:**

### dy302c:ExcIEEEAC8B.kpr-valueRange

**Path:** `cim:ExcIEEEAC8B.kpr`  
**Name:** C:302:DY:ExcIEEEAC8B.kpr:valueRange  
Voltage regulator proportional gain (K<sub>PR</sub>) (> 0 if ExcIEEEAC8B.kir = 0).  Typical value = 80.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:ExcIEEEAC8B.kir ?kir .
        FILTER (?kir=0 && ?value<=0) .        
			}
```
  - Messages: `["The value negative or zero when ExcIEEEAC8B.kir = 0."]`

## dy302c:ExcIEEEDC1A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEDC1A

## dy302c:ExcIEEEDC2A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEDC2A

## dy302c:ExcIEEEDC3A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEDC3A

## dy302c:ExcIEEEDC4B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEDC4B

**Nested Properties:**

### dy302c:ExcIEEEDC4B.td-valueRange

**Path:** `cim:ExcIEEEDC4B.td`  
**Name:** C:302:DY:ExcIEEEDC4B.td:valueRange  
Regulator derivative filter time constant (T<sub>D</sub>) (> 0 if ExcIEEEDC4B.kd > 0).  Typical value = 0,01.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:ExcIEEEDC4B.kd ?kd .
        FILTER (?kd>0 && ?value<=0) .        
			}
```
  - Messages: `["The value negative or zero when ExcIEEEDC4B.kd > 0."]`

## dy302c:ExcIEEEST1A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEST1A

## dy302c:ExcIEEEST2A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEST2A

## dy302c:ExcIEEEST3A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEST3A

## dy302c:ExcIEEEST4B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEST4B

## dy302c:ExcIEEEST5B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEST5B

## dy302c:ExcIEEEST6B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEST6B

## dy302c:ExcIEEEST7B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcIEEEST7B

## dy302c:ExcNI

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcNI

## dy302c:ExcOEX3T

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcOEX3T

## dy302c:ExcPIC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcPIC

## dy302c:ExcREXS

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcREXS

## dy302c:ExcRQB

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcRQB

## dy302c:ExcSCRX

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcSCRX

## dy302c:ExcSEXS

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcSEXS

**Nested Properties:**

### dy302c:ExcSEXS.kc-valueRange

**Path:** `cim:ExcSEXS.kc`  
**Name:** C:302:DY:ExcSEXS.kc:valueRange  
PI controller gain (Kc) (> 0 if ExcSEXS.tc > 0).  Typical value = 0,08.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:ExcSEXS.tc ?tc .
        FILTER (?tc>0 && ?value<=0) .        
			}
```
  - Messages: `["The value negative or zero when ExcSEXS.tc > 0."]`

## dy302c:ExcSK

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcSK

## dy302c:ExcST1A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcST1A

## dy302c:ExcST2A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcST2A

## dy302c:ExcST3A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcST3A

## dy302c:ExcST4B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcST4B

## dy302c:ExcST6B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcST6B

## dy302c:ExcST7B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcST7B

## dy302c:GovCT1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovCT1

## dy302c:GovCT2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovCT2

## dy302c:GovGAST

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovGAST

## dy302c:GovGAST1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovGAST1

## dy302c:GovGAST2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovGAST2

## dy302c:GovGAST3

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovGAST3

## dy302c:GovGAST4

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovGAST4

## dy302c:GovGASTWD

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovGASTWD

## dy302c:GovHydro1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydro1

## dy302c:GovHydro2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydro2

## dy302c:GovHydro3

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydro3

## dy302c:GovHydro4

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydro4

**Nested Properties:**

### dy302c:GovHydro4.bgv0-valueRange

**Path:** `cim:GovHydro4.bgv0`  
**Name:** C:302:DY:GovHydro4.bgv0:valueRange  
Kaplan blade servo point 0 (Bgv0) (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 0.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        FILTER ((?model=cim:GovHydro4ModelKind.simple || ?model=cim:GovHydro4ModelKind.francisPelton) && ?value!=0) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple or francisPelton."]`

### dy302c:GovHydro4.bgv1-valueRange

**Path:** `cim:GovHydro4.bgv1`  
**Name:** C:302:DY:GovHydro4.bgv1:valueRange  
Kaplan blade servo point 1 (Bgv1) (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 0.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        FILTER ((?model=cim:GovHydro4ModelKind.simple || ?model=cim:GovHydro4ModelKind.francisPelton) && ?value!=0) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple or francisPelton."]`

### dy302c:GovHydro4.bgv2-valueRange

**Path:** `cim:GovHydro4.bgv2`  
**Name:** C:302:DY:GovHydro4.bgv2:valueRange  
Kaplan blade servo point 2 (Bgv2) (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 0,1.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        FILTER ((?model=cim:GovHydro4ModelKind.simple || ?model=cim:GovHydro4ModelKind.francisPelton) && ?value!=0) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple or francisPelton."]`

### dy302c:GovHydro4.bgv3-valueRange

**Path:** `cim:GovHydro4.bgv3`  
**Name:** C:302:DY:GovHydro4.bgv3:valueRange  
Kaplan blade servo point 3 (Bgv3) (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 0,667.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        FILTER ((?model=cim:GovHydro4ModelKind.simple || ?model=cim:GovHydro4ModelKind.francisPelton) && ?value!=0) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple or francisPelton."]`

### dy302c:GovHydro4.bgv4-valueRange

**Path:** `cim:GovHydro4.bgv4`  
**Name:** C:302:DY:GovHydro4.bgv4:valueRange  
Kaplan blade servo point 4 (Bgv4) (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 0,9.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        FILTER ((?model=cim:GovHydro4ModelKind.simple || ?model=cim:GovHydro4ModelKind.francisPelton) && ?value!=0) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple or francisPelton."]`

### dy302c:GovHydro4.bgv5-valueRange

**Path:** `cim:GovHydro4.bgv5`  
**Name:** C:302:DY:GovHydro4.bgv5:valueRange  
Kaplan blade servo point 5 (Bgv5) (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 1.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        FILTER ((?model=cim:GovHydro4ModelKind.simple || ?model=cim:GovHydro4ModelKind.francisPelton) && ?value!=0) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple or francisPelton."]`

### dy302c:GovHydro4.bmax-valueRange

**Path:** `cim:GovHydro4.bmax`  
**Name:** C:302:DY:GovHydro4.bmax:valueRange  
Maximum blade adjustment factor (Bmax)  (= 0 for simple, = 0 for Francis/Pelton).  Typical value for Kaplan = 1,1276.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        FILTER ((?model=cim:GovHydro4ModelKind.simple || ?model=cim:GovHydro4ModelKind.francisPelton) && ?value!=0) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple or francisPelton."]`

### dy302c:GovHydro4.gv0-valueRange

**Path:** `cim:GovHydro4.gv0`  
**Name:** C:302:DY:GovHydro4.gv0:valueRange  
Nonlinear gain point 0, PU gv (Gv0) (= 0 for simple).  Typical for Francis/Pelton = 0,1, Kaplan = 0,1.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        FILTER (?model=cim:GovHydro4ModelKind.simple && ?value!=0) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple."]`

### dy302c:GovHydro4.gv1-valueRange

**Path:** `cim:GovHydro4.gv1`  
**Name:** C:302:DY:GovHydro4.gv1:valueRange  
Nonlinear gain point 1, PU gv (Gv1) (= 0 for simple, > GovHydro4.gv0 for Francis/Pelton and Kaplan). Typical value for Francis/Pelton = 0,4, Kaplan = 0,4.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        $this cim:GovHydro4.gv0 ?gv0 .
        FILTER ((?model=cim:GovHydro4ModelKind.simple && ?value!=0) || ((?model=cim:GovHydro4ModelKind.francisPelton || ?model=cim:GovHydro4ModelKind.kaplan) && ?value<=?gv0)) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple or it is not greater than GovHydro4.gv0 when GovHydro4.model is francisPelton or kaplan."]`

### dy302c:GovHydro4.gv2-valueRange

**Path:** `cim:GovHydro4.gv2`  
**Name:** C:302:DY:GovHydro4.gv2:valueRange  
Nonlinear gain point 2, PU gv (Gv2) (= 0 for simple, > GovHydro4.gv1 for Francis/Pelton and Kaplan). Typical value for Francis/Pelton = 0,5, Kaplan = 0,5.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        $this cim:GovHydro4.gv1 ?gv1 .
        FILTER ((?model=cim:GovHydro4ModelKind.simple && ?value!=0) || ((?model=cim:GovHydro4ModelKind.francisPelton || ?model=cim:GovHydro4ModelKind.kaplan) && ?value<=?gv1)) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple or it is not greater than GovHydro4.gv1 when GovHydro4.model is francisPelton or kaplan."]`

### dy302c:GovHydro4.gv3-valueRange

**Path:** `cim:GovHydro4.gv3`  
**Name:** C:302:DY:GovHydro4.gv3:valueRange  
Nonlinear gain point 3, PU gv (Gv3)  (= 0 for simple, > GovHydro4.gv2 for Francis/Pelton and Kaplan). Typical value for Francis/Pelton = 0,7, Kaplan = 0,7.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        $this cim:GovHydro4.gv2 ?gv2 .
        FILTER ((?model=cim:GovHydro4ModelKind.simple && ?value!=0) || ((?model=cim:GovHydro4ModelKind.francisPelton || ?model=cim:GovHydro4ModelKind.kaplan) && ?value<=?gv2)) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple or it is not greater than GovHydro4.gv2 when GovHydro4.model is francisPelton or kaplan."]`

### dy302c:GovHydro4.gv4-valueRange

**Path:** `cim:GovHydro4.gv4`  
**Name:** C:302:DY:GovHydro4.gv4:valueRange  
Nonlinear gain point 4, PU gv (Gv4)  (= 0 for simple, > GovHydro4.gv3 for Francis/Pelton and Kaplan). Typical value for  Francis/Pelton = 0,8, Kaplan = 0,8.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        $this cim:GovHydro4.gv3 ?gv3 .
        FILTER ((?model=cim:GovHydro4ModelKind.simple && ?value!=0) || ((?model=cim:GovHydro4ModelKind.francisPelton || ?model=cim:GovHydro4ModelKind.kaplan) && ?value<=?gv3)) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple or it is not greater than GovHydro4.gv3 when GovHydro4.model is francisPelton or kaplan."]`

### dy302c:GovHydro4.gv5-valueRange

**Path:** `cim:GovHydro4.gv5`  
**Name:** C:302:DY:GovHydro4.gv5:valueRange  
Nonlinear gain point 5, PU gv (Gv5)  (= 0 for simple, < 1 and > GovHydro4.gv4 for Francis/Pelton and Kaplan). Typical value for Francis/Pelton = 0,9, Kaplan = 0,9.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        $this cim:GovHydro4.gv4 ?gv4 .
        FILTER ((?model=cim:GovHydro4ModelKind.simple && ?value!=0) || ((?model=cim:GovHydro4ModelKind.francisPelton || ?model=cim:GovHydro4ModelKind.kaplan) && ?value<=?gv4 && ?value>=1)) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple or it is either not greater than GovHydro4.gv4 or it is not less than 1 when GovHydro4.model is francisPelton or kaplan."]`

### dy302c:GovHydro4.pgv0-valueRange

**Path:** `cim:GovHydro4.pgv0`  
**Name:** C:302:DY:GovHydro4.pgv0:valueRange  
Nonlinear gain point 0, PU power (Pgv0) (= 0 for simple).  Typical value = 0.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        FILTER (?model=cim:GovHydro4ModelKind.simple && ?value!=0) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple."]`

### dy302c:GovHydro4.pgv1-valueRange

**Path:** `cim:GovHydro4.pgv1`  
**Name:** C:302:DY:GovHydro4.pgv1:valueRange  
Nonlinear gain point 1, PU power (Pgv1) (= 0 for simple). Typical value for Francis/Pelton = 0,42, Kaplan = 0,35.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        FILTER (?model=cim:GovHydro4ModelKind.simple && ?value!=0) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple."]`

### dy302c:GovHydro4.pgv2-valueRange

**Path:** `cim:GovHydro4.pgv2`  
**Name:** C:302:DY:GovHydro4.pgv2:valueRange  
Nonlinear gain point 2, PU power (Pgv2) (= 0 for simple). Typical value for Francis/Pelton = 0,56, Kaplan = 0,468.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        FILTER (?model=cim:GovHydro4ModelKind.simple && ?value!=0) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple."]`

### dy302c:GovHydro4.pgv3-valueRange

**Path:** `cim:GovHydro4.pgv3`  
**Name:** C:302:DY:GovHydro4.pgv3:valueRange  
Nonlinear gain point 3, PU power (Pgv3) (= 0 for simple). Typical value for Francis/Pelton = 0,8, Kaplan = 0,796.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        FILTER (?model=cim:GovHydro4ModelKind.simple && ?value!=0) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple."]`

### dy302c:GovHydro4.pgv4-valueRange

**Path:** `cim:GovHydro4.pgv4`  
**Name:** C:302:DY:GovHydro4.pgv4:valueRange  
Nonlinear gain point 4, PU power (Pgv4) (= 0 for simple). Typical value for Francis/Pelton = 0,9, Kaplan = 0,917.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        FILTER (?model=cim:GovHydro4ModelKind.simple && ?value!=0) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple."]`

### dy302c:GovHydro4.pgv5-valueRange

**Path:** `cim:GovHydro4.pgv5`  
**Name:** C:302:DY:GovHydro4.pgv5:valueRange  
Nonlinear gain point 5, PU power (Pgv5) (= 0 for simple). Typical value for Francis/Pelton = 0,97, Kaplan = 0,99.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:GovHydro4.model ?model .
        FILTER (?model=cim:GovHydro4ModelKind.simple && ?value!=0) .        
			}
```
  - Messages: `["The value is not 0 when GovHydro4.model is simple."]`

## dy302c:GovHydroDD

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroDD

## dy302c:GovHydroFrancis

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroFrancis

## dy302c:GovHydroIEEE0

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroIEEE0

## dy302c:GovHydroIEEE2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroIEEE2

## dy302c:GovHydroPID

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroPID

## dy302c:GovHydroPID2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroPID2

## dy302c:GovHydroPelton

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroPelton

## dy302c:GovHydroR

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroR

## dy302c:GovHydroWEH

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroWEH

## dy302c:GovHydroWPID

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovHydroWPID

## dy302c:GovSteam0

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteam0

## dy302c:GovSteam1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteam1

## dy302c:GovSteam2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteam2

## dy302c:GovSteamBB

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteamBB

## dy302c:GovSteamCC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteamCC

## dy302c:GovSteamEU

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteamEU

## dy302c:GovSteamFV2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteamFV2

## dy302c:GovSteamFV3

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteamFV3

**Nested Properties:**

### dy302c:GovSteamFV3.t5-valueRange

**Path:** `cim:GovSteamFV3.t5`  
**Name:** C:302:DY:GovSteamFV3.t5:valueRange  
Time constant of second boiler pass (i.e. reheater) (T5) (> 0 if fast valving is used, otherwise >= 0).  Typical value = 0,5.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        FILTER (?value<0) .        
			}
```
  - Messages: `["The value is not greater than or equal to 0."]`

## dy302c:GovSteamFV4

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteamFV4

## dy302c:GovSteamIEEE1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteamIEEE1

## dy302c:GovSteamSGO

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GovSteamSGO

## dy302c:LoadComposite

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadComposite

## dy302c:LoadGenericNonLinear

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadGenericNonLinear

## dy302c:LoadMotor

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadMotor

## dy302c:LoadStatic

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadStatic

**Nested Properties:**

### dy302c:LoadStatic.staticLoadModelType-constantZ

**Path:** `cim:LoadStatic.staticLoadModelType`  
**Name:** C:302:DY:StaticLoadModelKind.constantZ:requiredAttributes  
The load is represented as a constant impedance.  ConstantZ equations are used  for active and reactive power and no attributes are required.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
          OPTIONAL {$this cim:LoadStatic.kp1 ?kp1} .
          OPTIONAL {$this cim:LoadStatic.kp2 ?kp2} .
          OPTIONAL {$this cim:LoadStatic.kp3 ?kp3} .
          OPTIONAL {$this cim:LoadStatic.kp4 ?kp4} .
          OPTIONAL {$this cim:LoadStatic.kpf ?kpf} .
          OPTIONAL {$this cim:LoadStatic.kq1 ?kq1} .
          OPTIONAL {$this cim:LoadStatic.kq2 ?kq2} .
          OPTIONAL {$this cim:LoadStatic.kq3 ?kq3} .
          OPTIONAL {$this cim:LoadStatic.kq4 ?kq4} .
          OPTIONAL {$this cim:LoadStatic.kqf ?kqf} .
          OPTIONAL {$this cim:LoadStatic.ep1 ?ep1} .
          OPTIONAL {$this cim:LoadStatic.ep2 ?ep2} .
          OPTIONAL {$this cim:LoadStatic.ep3 ?ep3} .
          OPTIONAL {$this cim:LoadStatic.eq1 ?eq1} .
          OPTIONAL {$this cim:LoadStatic.eq2 ?eq2} .
          OPTIONAL {$this cim:LoadStatic.eq3 ?eq3} .
        FILTER ((bound(?kp1) || bound(?kp2) || bound(?kp3) || bound(?kp4) || bound(?kpf) || bound(?kq1) || bound(?kq2) || bound(?kq3) || bound(?kq4) || bound(?kqf) || bound(?ep1) || bound(?ep2) || bound(?ep3) || bound(?eq1) || bound(?eq2) || bound(?eq3)) && ?value=cim:StaticLoadModelKind.constantZ) .        
			}
```
  - Messages: `["The load is represented as a constant impedance but other properties (attributes) are defined."]`

### dy302c:LoadStatic.staticLoadModelType-exponental

**Path:** `cim:LoadStatic.staticLoadModelType`  
**Name:** C:302:DY:StaticLoadModelKind.exponential:requiredAttributes  
This model is an exponential representation of the load. Exponential equations for active and reactive power are used and the following attributes are required: kp1, kp2, kp3, kpf, ep1, ep2, ep3, kq1, kq2, kq3, kqf, eq1, eq2, eq3.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
          OPTIONAL {$this cim:LoadStatic.kp1 ?kp1} .
          OPTIONAL {$this cim:LoadStatic.kp2 ?kp2} .
          OPTIONAL {$this cim:LoadStatic.kp3 ?kp3} .
          OPTIONAL {$this cim:LoadStatic.kp4 ?kp4} .
          OPTIONAL {$this cim:LoadStatic.kpf ?kpf} .
          OPTIONAL {$this cim:LoadStatic.kq1 ?kq1} .
          OPTIONAL {$this cim:LoadStatic.kq2 ?kq2} .
          OPTIONAL {$this cim:LoadStatic.kq3 ?kq3} .
          OPTIONAL {$this cim:LoadStatic.kq4 ?kq4} .
          OPTIONAL {$this cim:LoadStatic.kqf ?kqf} .
          OPTIONAL {$this cim:LoadStatic.ep1 ?ep1} .
          OPTIONAL {$this cim:LoadStatic.ep2 ?ep2} .
          OPTIONAL {$this cim:LoadStatic.ep3 ?ep3} .
          OPTIONAL {$this cim:LoadStatic.eq1 ?eq1} .
          OPTIONAL {$this cim:LoadStatic.eq2 ?eq2} .
          OPTIONAL {$this cim:LoadStatic.eq3 ?eq3} .
        FILTER (((!bound(?kp1) || !bound(?kp2) || !bound(?kp3) || !bound(?kpf) || !bound(?kq1) || !bound(?kq2) || !bound(?kq3) || !bound(?kqf) || !bound(?ep1) || !bound(?ep2) || !bound(?ep3) || !bound(?eq1) || !bound(?eq2) || !bound(?eq3)) && ?value=cim:StaticLoadModelKind.exponential) || ((bound(?kp4) || bound(?kq4)) && ?value=cim:StaticLoadModelKind.exponential)) .        
			}
```
  - Messages: `["Required properties (attributes) for exponential model type are not defined or there are unnecessary properties defined."]`

### dy302c:LoadStatic.staticLoadModelType-zIP1

**Path:** `cim:LoadStatic.staticLoadModelType`  
**Name:** C:302:DY:StaticLoadModelKind.zIP1:requiredAttributes  
This model integrates the frequency-dependent load (primarily motors).  ZIP1 equations for active and reactive power are used and the following attributes are required: kp1, kp2, kp3, kpf, kq1, kq2, kq3, kqf.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
          OPTIONAL {$this cim:LoadStatic.kp1 ?kp1} .
          OPTIONAL {$this cim:LoadStatic.kp2 ?kp2} .
          OPTIONAL {$this cim:LoadStatic.kp3 ?kp3} .
          OPTIONAL {$this cim:LoadStatic.kp4 ?kp4} .
          OPTIONAL {$this cim:LoadStatic.kpf ?kpf} .
          OPTIONAL {$this cim:LoadStatic.kq1 ?kq1} .
          OPTIONAL {$this cim:LoadStatic.kq2 ?kq2} .
          OPTIONAL {$this cim:LoadStatic.kq3 ?kq3} .
          OPTIONAL {$this cim:LoadStatic.kq4 ?kq4} .
          OPTIONAL {$this cim:LoadStatic.kqf ?kqf} .
          OPTIONAL {$this cim:LoadStatic.ep1 ?ep1} .
          OPTIONAL {$this cim:LoadStatic.ep2 ?ep2} .
          OPTIONAL {$this cim:LoadStatic.ep3 ?ep3} .
          OPTIONAL {$this cim:LoadStatic.eq1 ?eq1} .
          OPTIONAL {$this cim:LoadStatic.eq2 ?eq2} .
          OPTIONAL {$this cim:LoadStatic.eq3 ?eq3} .
        FILTER (((!bound(?kp1) || !bound(?kp2) || !bound(?kp3) || !bound(?kpf) || !bound(?kq1) || !bound(?kq2) || !bound(?kq3) || !bound(?kqf) ) && ?value=cim:StaticLoadModelKind.zIP1) || (?value=cim:StaticLoadModelKind.zIP1 && (bound(?ep1) || bound(?ep2) || bound(?ep3) || bound(?eq1) || bound(?eq2) || bound(?eq3) || bound(?kp4) || bound(?kq4)))) .        
			}
```
  - Messages: `["Required properties (attributes) for zIP1 model type are not defined or there are unnecessary properties defined."]`

### dy302c:LoadStatic.staticLoadModelType-zIP2

**Path:** `cim:LoadStatic.staticLoadModelType`  
**Name:** C:302:DY:StaticLoadModelKind.zIP2:requiredAttributes  
This model separates the frequency-dependent load (primarily motors) from other load.  ZIP2 equations for active and reactive power are used and the following attributes are required: kp1, kp2, kp3, kq4, kpf, kq1, kq2, kq3, kq4, kqf.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
          OPTIONAL {$this cim:LoadStatic.kp1 ?kp1} .
          OPTIONAL {$this cim:LoadStatic.kp2 ?kp2} .
          OPTIONAL {$this cim:LoadStatic.kp3 ?kp3} .
          OPTIONAL {$this cim:LoadStatic.kp4 ?kp4} .
          OPTIONAL {$this cim:LoadStatic.kpf ?kpf} .
          OPTIONAL {$this cim:LoadStatic.kq1 ?kq1} .
          OPTIONAL {$this cim:LoadStatic.kq2 ?kq2} .
          OPTIONAL {$this cim:LoadStatic.kq3 ?kq3} .
          OPTIONAL {$this cim:LoadStatic.kq4 ?kq4} .
          OPTIONAL {$this cim:LoadStatic.kqf ?kqf} .
          OPTIONAL {$this cim:LoadStatic.ep1 ?ep1} .
          OPTIONAL {$this cim:LoadStatic.ep2 ?ep2} .
          OPTIONAL {$this cim:LoadStatic.ep3 ?ep3} .
          OPTIONAL {$this cim:LoadStatic.eq1 ?eq1} .
          OPTIONAL {$this cim:LoadStatic.eq2 ?eq2} .
          OPTIONAL {$this cim:LoadStatic.eq3 ?eq3} .
        FILTER (((!bound(?kp1) || !bound(?kp2) || !bound(?kp3) || !bound(?kp4) || !bound(?kpf) || !bound(?kq1) || !bound(?kq2) || !bound(?kq3) || !bound(?kq4) || !bound(?kqf) ) && ?value=cim:StaticLoadModelKind.zIP2) || (?value=cim:StaticLoadModelKind.zIP2 && (bound(?ep1) || bound(?ep2) || bound(?ep3) || bound(?eq1) || bound(?eq2) || bound(?eq3)))) .        
			}
```
  - Messages: `["Required properties (attributes) for zIP2 model type are not defined or there are unnecessary properties defined."]`

## dy302c:MechanicalLoadDynamics

**Name:** C:302:DY:MechanicalLoadDynamics:associationsCondition  
MechanicalLoadDynamics shall have either an association to SynchronousMachineDynamics or to AsynchronousMachineDynamics.

**Severity:** sh:Violation

**Messages:**
- "Required association to either SynchronousMachineDynamics or to AsynchronousMachineDynamics is missing."

**Targets:**
- targetClass: cim:MechanicalLoadUserDefined
- targetClass: cim:MechLoad1

## dy302c:OverexcLim2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:OverexcLim2

## dy302c:OverexcLimX1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:OverexcLimX1

## dy302c:OverexcLimX2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:OverexcLimX2

## dy302c:PFVArType1IEEEPFController

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PFVArType1IEEEPFController

## dy302c:PFVArType1IEEEVArController

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PFVArType1IEEEVArController

## dy302c:Pss1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Pss1

## dy302c:Pss1A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Pss1A

## dy302c:Pss2B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Pss2B

## dy302c:Pss2ST

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Pss2ST

**Nested Properties:**

### dy302c:Pss2ST-inputSignals

**Path:** `cim:Pss2ST.inputSignal1Type`  
**Name:** C:302:DY:Pss2ST:inputSignals  
shall be different than Pss2ST.inputSignal2Type.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:Pss2ST.inputSignal2Type ?input2 .
        FILTER (?value=?input2) .        
			}
```
  - Messages: `["Input signal #1 and input signal #2 are not different."]`

## dy302c:Pss5

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Pss5

## dy302c:PssELIN2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssELIN2

## dy302c:PssIEEE1A

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssIEEE1A

## dy302c:PssIEEE2B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssIEEE2B

## dy302c:PssIEEE3B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssIEEE3B

## dy302c:PssIEEE4B

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssIEEE4B

## dy302c:PssPTIST1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssPTIST1

## dy302c:PssPTIST3

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssPTIST3

## dy302c:PssRQB

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssRQB

## dy302c:PssSB4

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssSB4

## dy302c:PssSH

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssSH

## dy302c:PssSK

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssSK

## dy302c:PssWECC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PssWECC

**Nested Properties:**

### dy302c:PssWECC-inputSignals

**Path:** `cim:PssWECC.inputSignal1Type`  
**Name:** C:302:DY:PssWECC:inputSignals  
shall be different than PssWECC.inputSignal2Type.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:PssWECC.inputSignal2Type ?input2 .
        FILTER (?value=?input2) .        
			}
```
  - Messages: `["Input signal #1 and input signal #2 are not different."]`

## dy302c:RotatingMachineDynamics

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachineUserDefined
- targetClass: cim:SynchronousMachineTimeConstantReactance
- targetClass: cim:SynchronousMachineEquivalentCircuit
- targetClass: cim:AsynchronousMachineUserDefined
- targetClass: cim:AsynchronousMachineTimeConstantReactance
- targetClass: cim:AsynchronousMachineEquivalentCircuit

**Nested Properties:**

### dy302c:RotatingMachineDynamics.saturationFactor120-valueRange

**Path:** `cim:RotatingMachineDynamics.saturationFactor120`  
**Name:** C:302:DY:RotatingMachineDynamics.saturationFactor120:valueRange  
Saturation factor at 120% of rated terminal voltage (S12) (>= RotatingMachineDynamics.saturationFactor). 

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:RotatingMachineDynamics.saturationFactor ?saturationFactor .
        FILTER (?value<?saturationFactor) .        
			}
```
  - Messages: `["The value is less than RotatingMachineDynamics.saturationFactor."]`

## dy302c:SynchronousMachineEquivalentCircuit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachineEquivalentCircuit

## dy302c:SynchronousMachineSimplified

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachineSimplified

**Nested Properties:**

### dy302c:SynchronousMachineSimplified-requiredAttributes

**Path:** `rdf:type`  
**Name:** C:302:DY:SynchronousMachineSimplified:requiredAttributes  
The parameters used for the simplified model include:- RotatingMachineDynamics.damping (D);- RotatingMachineDynamics.inertia (H);- RotatingMachineDynamics.statorLeakageReactance (used to exchange jXp for SynchronousMachineSimplified);- RotatingMachineDynamics.statorResistance (Rs).

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this
			WHERE {
          OPTIONAL {$this cim:RotatingMachineDynamics.saturationFactor ?s1} .
          OPTIONAL {$this cim:RotatingMachineDynamics.saturationFactor120 ?s2} .
        FILTER (bound(?s1) || bound(?s2)) .        
			}
```
  - Messages: `["Saturation related attributes are not needed for SynchronousMachineSimplified."]`

## dy302c:SynchronousMachineTimeConstantReactance

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachineTimeConstantReactance

## dy302c:SynchronousMachineUserDefined

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachineUserDefined

## dy302c:TurbLCFB1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TurbLCFB1

## dy302c:TurbineGovernorDynamics

**Name:** C:302:DY:TurbineGovernorDynamics:associationsCondition  
TurbineGovernorDynamics shall have either an association to SynchronousMachineDynamics or to AsynchronousMachineDynamics.

**Severity:** sh:Violation

**Messages:**
- "Required association to either SynchronousMachineDynamics or to AsynchronousMachineDynamics is missing."

**Targets:**
- targetClass: cim:GovGAST4
- targetClass: cim:GovGAST3
- targetClass: cim:GovGAST
- targetClass: cim:GovSteam1
- targetClass: cim:GovGASTWD
- targetClass: cim:GovHydro1
- targetClass: cim:TurbineGovernorUserDefined
- targetClass: cim:GovHydroIEEE0
- targetClass: cim:GovHydroFrancis
- targetClass: cim:GovSteam0
- targetClass: cim:GovSteamSGO
- targetClass: cim:GovSteamFV3
- targetClass: cim:GovHydroPelton
- targetClass: cim:GovSteamEU
- targetClass: cim:GovHydro3
- targetClass: cim:GovSteamIEEE1
- targetClass: cim:GovSteamBB
- targetClass: cim:GovGAST2
- targetClass: cim:GovHydroIEEE2
- targetClass: cim:GovHydro2
- targetClass: cim:GovHydroPID
- targetClass: cim:GovHydro4
- targetClass: cim:GovSteam2
- targetClass: cim:GovSteamFV2
- targetClass: cim:GovHydroWPID
- targetClass: cim:GovCT1
- targetClass: cim:GovHydroWEH
- targetClass: cim:GovHydroPID2
- targetClass: cim:GovHydroDD
- targetClass: cim:GovSteamFV4
- targetClass: cim:GovGAST1
- targetClass: cim:GovCT2
- targetClass: cim:GovHydroR

## dy302c:UnderexcLim2Simplified

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:UnderexcLim2Simplified

## dy302c:UnderexcLimIEEE1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:UnderexcLimIEEE1

## dy302c:UnderexcLimIEEE2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:UnderexcLimIEEE2

## dy302c:UnderexcLimX1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:UnderexcLimX1

## dy302c:UnderexcLimX2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:UnderexcLimX2

## dy302c:VAdjIEEE

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VAdjIEEE

## dy302c:VCompIEEEType1

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VCompIEEEType1

## dy302c:VCompIEEEType2

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VCompIEEEType2

## dy302c:WindContPType3IEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContPType3IEC

## dy302c:WindContPType4aIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContPType4aIEC

## dy302c:WindContPType4bIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContPType4bIEC

## dy302c:WindContPitchAngleIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContPitchAngleIEC

## dy302c:WindContQIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContQIEC

## dy302c:WindContQLimIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContQLimIEC

## dy302c:WindContQPQULimIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContQPQULimIEC

## dy302c:WindContRotorRIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindContRotorRIEC

## dy302c:WindGenType3aIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindGenType3aIEC

## dy302c:WindGenType3bIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindGenType3bIEC

## dy302c:WindGenType4IEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindGenType4IEC

## dy302c:WindMechIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindMechIEC

## dy302c:WindPitchContPowerIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindPitchContPowerIEC

## dy302c:WindPlantFreqPcontrolIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindPlantFreqPcontrolIEC

## dy302c:WindPlantReactiveControlIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindPlantReactiveControlIEC

## dy302c:WindProtectionIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindProtectionIEC

## dy302c:WindRefFrameRotIEC

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindRefFrameRotIEC

