# 61970-457_Dynamics-AP-Con-Complex-SHACL

## dy457c:ExcitationSystemDynamics.SynchronousMachineDynamics-valueType

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExcELIN1
- targetClass: cim:ExcPIC
- targetClass: cim:ExcIEEEST2A
- targetClass: cim:ExcNI
- targetClass: cim:ExcRQB
- targetClass: cim:ExcELIN2
- targetClass: cim:ExcIEEEAC1A
- targetClass: cim:ExcIEEEST5B
- targetClass: cim:ExcDC3A1
- targetClass: cim:ExcHU
- targetClass: cim:ExcAC2A
- targetClass: cim:ExcIEEEAC8B
- targetClass: cim:ExcAVR1
- targetClass: cim:ExcAVR5
- targetClass: cim:ExcAC8B
- targetClass: cim:ExcDC1A
- targetClass: cim:ExcCZ
- targetClass: cim:ExcIEEEDC2A
- targetClass: cim:ExcAVR4
- targetClass: cim:ExcIEEEAC6A
- targetClass: cim:ExcBBC
- targetClass: cim:ExcST2A
- targetClass: cim:ExcIEEEST4B
- targetClass: cim:ExcAVR2
- targetClass: cim:ExcIEEEDC1A
- targetClass: cim:ExcIEEEST3A
- targetClass: cim:ExcAC6A
- targetClass: cim:ExcST3A
- targetClass: cim:ExcAC1A
- targetClass: cim:ExcIEEEST7B
- targetClass: cim:ExcIEEEAC3A
- targetClass: cim:ExcAC4A
- targetClass: cim:ExcANS
- targetClass: cim:ExcST7B
- targetClass: cim:ExcST6B
- targetClass: cim:ExcIEEEST1A
- targetClass: cim:ExcST4B
- targetClass: cim:ExcitationSystemUserDefined
- targetClass: cim:ExcSCRX
- targetClass: cim:ExcIEEEST6B
- targetClass: cim:ExcSK
- targetClass: cim:ExcSEXS
- targetClass: cim:ExcIEEEDC3A
- targetClass: cim:ExcAC5A
- targetClass: cim:ExcIEEEAC2A
- targetClass: cim:ExcOEX3T
- targetClass: cim:ExcIEEEAC5A
- targetClass: cim:ExcST1A
- targetClass: cim:ExcAVR3
- targetClass: cim:ExcDC3A
- targetClass: cim:ExcIEEEAC7B
- targetClass: cim:ExcIEEEDC4B
- targetClass: cim:ExcAC3A
- targetClass: cim:ExcDC2A
- targetClass: cim:ExcIEEEAC4A
- targetClass: cim:ExcREXS
- targetClass: cim:ExcAVR7

**Nested Properties:**

### dy457c:ExcitationSystemDynamics.SynchronousMachineDynamicsSynchronousMachineSimplified-valueType

**Path:** `cim:ExcitationSystemDynamics.SynchronousMachineDynamics`  
ExcitationSystemDynamics.SynchronousMachineDynamics cannot point to an object of type SynchronousMachineSimplified.

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
        ?value rdf:type ?type .
        FILTER (?type=cim:SynchronousMachineSimplified) .       
			}
```
  - Messages: `["The association ExcitationSystemDynamics.SynchronousMachineDynamics points to an object of type SynchronousMachineSimplified."]`

## dy457c:SynchronousMachineTimeConstantReactance

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachineTimeConstantReactance

**Nested Properties:**

### dy457c:SynchronousMachineTimeConstantReactance-modelType-SubtransientSalientPole

**Path:** `cim:SynchronousMachineTimeConstantReactance.modelType`  
Annex A specifies the usage of different attributes related to the model type. If SynchronousMachineTimeConstantReactance.modelType is subtransient and .rotorType is salientPole the following optional attributes are not exchanged or set to 0: - SynchronousMachineDetailed.saturationFactorQAxis - SynchronousMachineDetailed.saturationFactor120QAxis.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this
			WHERE {
        $this $PATH ?modelType .
        $this cim:SynchronousMachineTimeConstantReactance.rotorType ?rotorType .
        OPTIONAL {$this cim:SynchronousMachineDetailed.saturationFactorQAxis ?sfqaxis} .
        OPTIONAL {$this cim:SynchronousMachineDetailed.saturationFactor120QAxis ?sf120qaxis} .
        FILTER (?modelType=cim:SynchronousMachineModelKind.subtransient && ?rotorType=cim:RotorKind.salientPole && (?sfqaxis!=0 || ?sf120qaxis!=0)) .       
			}
```
  - Messages: `["Missing attributes or default values not provided according to 61970-457 Annex A."]`

### dy457c:SynchronousMachineTimeConstantReactance-modelType-SubtransientRoundRotorSimplified

**Path:** `cim:SynchronousMachineTimeConstantReactance.modelType`  
Annex A specifies the usage of different attributes related to the model type. If SynchronousMachineTimeConstantReactance.modelType is subtransientSimplified and .rotorType is roundRotor the following optional attributes are not exchanged or set to 0: - SynchronousMachineDetailed.saturationFactorQAxis; - SynchronousMachineDetailed.saturationFactor120QAxis. RotatingMachineDynamics.statorResistance is set to 0.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this
			WHERE {
        $this $PATH ?modelType .
        $this cim:SynchronousMachineTimeConstantReactance.rotorType ?rotorType .
        $this cim:RotatingMachineDynamics.statorResistance ?statorResistance .
        OPTIONAL {$this cim:SynchronousMachineDetailed.saturationFactorQAxis ?sfqaxis} .
        OPTIONAL {$this cim:SynchronousMachineDetailed.saturationFactor120QAxis ?sf120qaxis} .
        FILTER (?modelType=cim:SynchronousMachineModelKind.subtransientSimplified && ?rotorType=cim:RotorKind.roundRotor && (?statorResistance!=0 || ?sfqaxis!=0 || ?sf120qaxis!=0)) .       
			}
```
  - Messages: `["Missing attributes or default values not provided according to 61970-457 Annex A."]`

### dy457c:SynchronousMachineTimeConstantReactance-modelType-SubtransientRoundRotor

**Path:** `cim:SynchronousMachineTimeConstantReactance.modelType`  
Annex A specifies the usage of different attributes related to the model type. If SynchronousMachineTimeConstantReactance.modelType is subtransient and .rotorType is roundRotor the following optional attributes are required:- SynchronousMachineTimeConstantReactance.xQuadTrans;- SynchronousMachineTimeConstantReactance.tpqo;- SynchronousMachineDetailed.saturationFactorQAxis;- SynchronousMachineDetailed.saturationFactor120QAxis;- RotatingMachineDynamics.saturationFactor;- RotatingMachineDynamics.saturationFactor120.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT $this
			WHERE {
        $this $PATH ?modelType .
        $this cim:SynchronousMachineTimeConstantReactance.rotorType ?rotorType .
        OPTIONAL {$this cim:RotatingMachineDynamics.saturationFactor ?s1} .
        OPTIONAL {$this cim:RotatingMachineDynamics.saturationFactor120 ?s2} .
        OPTIONAL {$this cim:SynchronousMachineDetailed.saturationFactorQAxis ?sfqaxis} .
        OPTIONAL {$this cim:SynchronousMachineDetailed.saturationFactor120QAxis ?sf120qaxis} .
        OPTIONAL {$this cim:SynchronousMachineTimeConstantReactance.xQuadTrans ?xqtans} .
        OPTIONAL {$this cim:SynchronousMachineTimeConstantReactance.tpqo ?tpqo} .
        FILTER (?modelType=cim:SynchronousMachineModelKind.subtransient && ?rotorType=cim:RotorKind.roundRotor && (!bound(?sfqaxis) || !bound(?sf120qaxis) || !bound(?s1) || !bound(?s2) || !bound(?xqtans) || !bound(?tpqo))) .       
			}
```
  - Messages: `["Missing attributes or default values not provided according to 61970-457 Annex A."]`

