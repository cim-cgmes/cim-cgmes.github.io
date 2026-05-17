# 61970-301_Equipment-AP-Con-Complex-SHACL

## eq:ACDCConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VsConverter
- targetClass: cim:CsConverter

## eq:ACDCTerminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Clamp
- targetClass: cim:BusbarSection
- targetClass: cim:PetersenCoil
- targetClass: cim:ConformLoad
- targetClass: cim:Breaker
- targetClass: cim:Cut
- targetClass: cim:DCLineSegment
- targetClass: cim:DCSwitch
- targetClass: cim:CsConverter
- targetClass: cim:VsConverter
- targetClass: cim:ACLineSegment
- targetClass: cim:EnergyConsumer
- targetClass: cim:NonlinearShuntCompensator
- targetClass: cim:EquivalentShunt
- targetClass: cim:SeriesCompensator
- targetClass: cim:Switch
- targetClass: cim:StaticVarCompensator
- targetClass: cim:LoadBreakSwitch
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:Junction
- targetClass: cim:GroundingImpedance
- targetClass: cim:NonConformLoad
- targetClass: cim:StationSupply
- targetClass: cim:LinearShuntCompensator
- targetClass: cim:EquivalentInjection
- targetClass: cim:Ground
- targetClass: cim:DCSeriesDevice
- targetClass: cim:PowerElectronicsConnection
- targetClass: cim:EquivalentBranch
- targetClass: cim:Disconnector
- targetClass: cim:DCBusbar
- targetClass: cim:DCDisconnector
- targetClass: cim:DCGround
- targetClass: cim:EnergySource
- targetClass: cim:AsynchronousMachine
- targetClass: cim:Jumper
- targetClass: cim:ExternalNetworkInjection
- targetClass: cim:SynchronousMachine
- targetClass: cim:Fuse
- targetClass: cim:GroundDisconnector
- targetClass: cim:DCChopper
- targetClass: cim:DCShunt
- targetClass: cim:PowerTransformer
- targetClass: cim:DCBreaker

**Nested Properties:**

### eq:ACDCTerminal.sequenceNumber-numbering

**Path:** `rdf:type`  
The sequence numbering starts with 1 and additional terminals should follow in increasing order. The first terminal is the starting point for a two terminal branch.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this (COUNT(?sn) AS ?countsn) (COUNT(DISTINCT ?sn) AS ?countdsn) (MIN(?sn) AS ?minsn) (SUM(?sn) AS ?sumsn) (COUNT(?terms) AS ?countterms)
			WHERE {
        $this (^cim:Terminal.ConductingEquipment)|(^cim:DCTerminal.DCConductingEquipment) ?terms. 
        ?terms rdf:type ?type .
        ?terms cim:ACDCTerminal.sequenceNumber ?sn .
			}
      GROUP BY $this ?type
      HAVING(?countsn!=?countdsn || ?minsn!=1 || (?countterms=1 && ?sumsn!=1) || (?countterms=2 && (?sumsn/2)!=1.5) || (?countterms=3 && (?sumsn/3)!=2))
      
```
  - Messages: `["There is no terminal with sequenceNumber=1 or the numbering is not unique."]`

## eq:ACLineSegment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ACLineSegment

## eq:ActivePowerLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ActivePowerLimit

## eq:ApparentPowerLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ApparentPowerLimit

## eq:AsynchronousMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:AsynchronousMachine

## eq:BaseVoltage

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:BaseVoltage

## eq:BatteryUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:BatteryUnit

## eq:BoundaryPoint

**Severity:** sh:Violation

**Targets:**
- targetClass: cim100:BoundaryPoint

## eq:Breaker

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Breaker

## eq:BusbarSection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:BusbarSection

## eq:Clamp

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Clamp

## eq:Clamp-numberOfTerminals

A Clamp is ConductingEquipment and has one Terminal with an associated ConnectivityNode.

**Severity:** sh:Violation

**Messages:**
- "Either the Clamp does not have exactly one Terminal or the Terminal is not associated with a ConnectivityNode."

**Targets:**
- targetClass: cim:Clamp

## eq:ConductingEquipment-oneTerminal

All other ConductingEquipment leaf classes (notably also including Clamp and BusbarSection) and DCConductingEquipment have a single terminal.

**Severity:** sh:Violation

**Messages:**
- "The ConductingEquipment does not have the required number of Terminal-s."

**Targets:**
- targetClass: cim:DCGround
- targetClass: cim:EnergySource
- targetClass: cim:NonConformLoad
- targetClass: cim:PowerElectronicsConnection
- targetClass: cim:ExternalNetworkInjection
- targetClass: cim:EnergyConsumer
- targetClass: cim:ConformLoad
- targetClass: cim:StationSupply
- targetClass: cim:LinearShuntCompensator
- targetClass: cim:NonlinearShuntCompensator
- targetClass: cim:SynchronousMachine
- targetClass: cim:EquivalentShunt
- targetClass: cim:DCBusbar
- targetClass: cim:DCShunt
- targetClass: cim:Ground
- targetClass: cim:AsynchronousMachine
- targetClass: cim:EquivalentInjection
- targetClass: cim:Junction
- targetClass: cim:StaticVarCompensator

## eq:ConductingEquipment-twoTerminals

The following ConductingEquipment classes have two terminals: ACLineSegment, DCLineSegment, DCSeriesDevice, DCSwitch (and its specializations), DCChopper, Switch and all its specializations (including Jumper, Fuse, Breaker, Disconnector, LoadBreakSwitch, and Cut), SeriesCompensator, and EquivalentBranch. The PowerTransformer class typically has two terminals, but may also have one or more terminals. For example a zig-zag connected grounding transformer may have one terminal. Three terminal transformers are commonly used in transmission systems and in special cases transformers may have four, five, or more terminals. 

**Severity:** sh:Violation

**Messages:**
- "The ConductingEquipment does not have the required number of Terminal-s."

**Targets:**
- targetClass: cim:DCSeriesDevice
- targetClass: cim:DCBreaker
- targetClass: cim:DCChopper
- targetClass: cim:Jumper
- targetClass: cim:Cut
- targetClass: cim:DCSwitch
- targetClass: cim:DCDisconnector
- targetClass: cim:Switch
- targetClass: cim:Disconnector
- targetClass: cim:Fuse
- targetClass: cim:GroundDisconnector
- targetClass: cim:Breaker
- targetClass: cim:LoadBreakSwitch
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:SeriesCompensator
- targetClass: cim:EquivalentBranch
- targetClass: cim:ACLineSegment
- targetClass: cim:DCLineSegment

## eq:ConductingEquipment-twoTerminalsShape

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GroundDisconnector
- targetClass: cim:Jumper
- targetClass: cim:Breaker
- targetClass: cim:DCSeriesDevice
- targetClass: cim:DCSwitch
- targetClass: cim:DCDisconnector
- targetClass: cim:DCBreaker
- targetClass: cim:Fuse
- targetClass: cim:EquivalentBranch
- targetClass: cim:LoadBreakSwitch
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:SeriesCompensator
- targetClass: cim:ACLineSegment
- targetClass: cim:DCChopper
- targetClass: cim:Disconnector
- targetClass: cim:Cut
- targetClass: cim:DCLineSegment
- targetClass: cim:Switch

**Nested Properties:**

### eq:Terminal.phases-consistencyEquipment

**Path:** `rdf:type`  
The phase code on terminals connecting same ConnectivityNode or same TopologicalNode as well as for equipment between two terminals shall be consistent.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value2 ?value1
			WHERE {      
        $this ^cim:Terminal.ConductingEquipment ?term1  .
        ?term1 cim:ACDCTerminal.sequenceNumber 1 .
        $this ^cim:Terminal.ConductingEquipment ?term2  .
        ?term2 cim:ACDCTerminal.sequenceNumber 2 
        OPTIONAL {?term1 cim:Terminal.phases ?value1 } .
        OPTIONAL {?term2 cim:Terminal.phases ?value2 } . 
        FILTER ((bound(?value1) && bound(?value2) && ?term1!=?term2 && (?value1=cim:PhaseCode.ABCN || ?value1=cim:PhaseCode.N) && (?value2!=cim:PhaseCode.ABCN && ?value2!=cim:PhaseCode.N)) ||
        (bound(?value1) && bound(?value2) && ?term1!=?term2 && (?value1=cim:PhaseCode.ABC) && (?value2!=cim:PhaseCode.ABC)) ||
        (bound(?value1) && !bound(?value2) && ?term1!=?term2 && (?value1=cim:PhaseCode.ABCN || ?value1=cim:PhaseCode.N))
        ) .
			}
```
  - Messages: `["The phase codes for terminals of 2-terminal equipment are not consistent. Terminal 1 code:{?value1} Terminal 2 code: {?value2}."]`

## eq:ConductingEquipment.BaseVoltage

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CsConverter
- targetClass: cim:Clamp
- targetClass: cim:EnergyConsumer
- targetClass: cim:EquivalentBranch
- targetClass: cim:Fuse
- targetClass: cim:GroundingImpedance
- targetClass: cim:EnergySource
- targetClass: cim:ConformLoad
- targetClass: cim:Ground
- targetClass: cim:Cut
- targetClass: cim:NonConformLoad
- targetClass: cim:StationSupply
- targetClass: cim:EquivalentInjection
- targetClass: cim:PowerTransformer
- targetClass: cim:GroundDisconnector
- targetClass: cim:ExternalNetworkInjection
- targetClass: cim:StaticVarCompensator
- targetClass: cim:PowerElectronicsConnection
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:Junction
- targetClass: cim:AsynchronousMachine
- targetClass: cim:SeriesCompensator
- targetClass: cim:Disconnector
- targetClass: cim:Jumper
- targetClass: cim:ACLineSegment
- targetClass: cim:SynchronousMachine
- targetClass: cim:VsConverter
- targetClass: cim:LinearShuntCompensator
- targetClass: cim:NonlinearShuntCompensator
- targetClass: cim:EquivalentShunt
- targetClass: cim:Breaker
- targetClass: cim:LoadBreakSwitch
- targetClass: cim:BusbarSection
- targetClass: cim:PetersenCoil
- targetClass: cim:Switch

**Nested Properties:**

### eq:ConductingEquipment.BaseVoltage-usage

**Path:** `cim:Equipment.EquipmentContainer`  
Use only when there is no voltage level container used and only one base voltage applies.  For example, not used for transformers.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT $this ?value
			WHERE {
        $this $PATH ?value .
        #?value rdf:type ?type .
        ?value rdf:type cim:VoltageLevel .
        $this rdf:type ?condeqtype .
        BIND(EXISTS{$this cim:ConductingEquipment.BaseVoltage ?basevoltage} AS ?hasbv).
        #$this cim:ConductingEquipment.BaseVoltage ?basevoltage .
        #FILTER (!isLiteral(?basevoltage) && ?type=cim:VoltageLevel && ?condeqtype!=cim:ACLineSegment && ?condeqtype!=cim:EquivalentBranch && ?condeqtype!=cim:SeriesCompensator) .
        FILTER (?hasbv=true && ?condeqtype!=cim:ACLineSegment && ?condeqtype!=cim:EquivalentBranch && ?condeqtype!=cim:SeriesCompensator && ?condeqtype!=cim:Equipment) .        
			}
```
  - Messages: `["The association ConductingEquipment.BaseVoltage is defined for a ConductingEquipment contained in a VoltageLevel."]`

## eq:ControlAreaGeneratingUnit.GeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NuclearGeneratingUnit
- targetClass: cim:SolarGeneratingUnit
- targetClass: cim:ThermalGeneratingUnit
- targetClass: cim:GeneratingUnit
- targetClass: cim:WindGeneratingUnit
- targetClass: cim:HydroGeneratingUnit

**Nested Properties:**

### eq:ControlAreaGeneratingUnit.GeneratingUnit-instance

**Path:** `rdf:type`  
Note that a control area should include a GeneratingUnit only once.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this (COUNT(?ca) AS ?count)
			WHERE {
        $this ^cim:ControlAreaGeneratingUnit.GeneratingUnit/cim:ControlAreaGeneratingUnit.ControlArea ?ca.   
			}
      GROUP BY $this ?ca
      HAVING(?count>1)
      
```
  - Messages: `["The GeneratingUnit is assigned to more than once in a ControlArea."]`

## eq:CsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CsConverter

**Nested Properties:**

### eq:DCConverterUnit-cscPowerTransformer

**Path:** `rdf:type`  
For a CSC HVDC, the transformer shall be modelled explicitly.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value  
			WHERE {      
        $this cim:Equipment.EquipmentContainer ?value .
        
        FILTER NOT EXISTS {
        ?value ^cim:Equipment.EquipmentContainer/rdf:type cim:PowerTransformer 
        }.
			}
```
  - Messages: `["A DCConverterUnit that contains CsConverter does not contain a PowerTransformer."]`

## eq:CurrentLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CurrentLimit

## eq:Cut

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Cut

## eq:DCBreaker

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCBreaker

## eq:DCBusbar

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCBusbar

## eq:DCChopper

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCChopper

## eq:DCDisconnector

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCDisconnector

## eq:DCGround

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCGround

## eq:DCLineSegment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCLineSegment

## eq:DCSeriesDevice

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCSeriesDevice

## eq:DCShunt

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCShunt

## eq:DCSwitch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DCSwitch

## eq:DisconnectingCircuitBreaker

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:DisconnectingCircuitBreaker

## eq:Disconnector

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Disconnector

## eq:EarthFaultCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GroundingImpedance
- targetClass: cim:PetersenCoil

## eq:Equipment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentBranch
- targetClass: cim:EquivalentShunt
- targetClass: cim:EquivalentInjection

**Nested Properties:**

### eq:Equipment.aggregate-notUsed

**Path:** `cim:Equipment.aggregate`  
The attribute is not used for EquivalentBranch, EquivalentShunt and EquivalentInjection.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        OPTIONAL {$this $PATH ?value }.
        FILTER (bound(?value)) .
			}
```
  - Messages: `["Not allowed property (attribute)."]`

## eq:EquivalentBranch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentBranch

**Nested Properties:**

### eq:EquivalentBranch.r21-usage

**Path:** `cim:EquivalentBranch.r21`  
This attribute is optional and represent unbalanced network such as off-nominal phase shifter. If only EquivalentBranch.r is given, then EquivalentBranch.r21 is assumed equal to EquivalentBranch.r.

**Severity:** sh:Info

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Info)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        OPTIONAL {$this $PATH ?value }.
        $this cim:EquivalentBranch.r ?r .
        FILTER (bound(?value) && ?value!=?r) .
			}
```
  - Messages: `["Asymmetrical EquivalentBranch is modelled as EquivalentBranch.r is different from EquivalentBranch.r21."]`

### eq:EquivalentBranch.x21-usage

**Path:** `cim:EquivalentBranch.x21`  
This attribute is optional and represent unbalanced network such as off-nominal phase shifter. If only EquivalentBranch.x is given, then EquivalentBranch.x21 is assumed equal to EquivalentBranch.x.

**Severity:** sh:Info

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Info)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        OPTIONAL {$this $PATH ?value }.
        $this cim:EquivalentBranch.x ?x .
        FILTER (bound(?value) && ?value!=?x) .
			}
```
  - Messages: `["Asymmetrical EquivalentBranch is modelled as EquivalentBranch.x is different from EquivalentBranch.x21."]`

## eq:EquivalentInjection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentInjection

**Nested Properties:**

### eq:EquivalentInjection.regulationCapability-associatedCurve

**Path:** `cim:EquivalentInjection.regulationCapability`  
ReactiveCapabilityCurve can only be associated with EquivalentInjection  if the flag is true.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value
        OPTIONAL {$this cim:EquivalentInjection.ReactiveCapabilityCurve ?curve }.
        FILTER (bound(?curve) && ?value=false) .
			}
```
  - Messages: `["The value does not allow a ReactiveCapabilityCurve to be associated. "]`

## eq:Fuse

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Fuse

## eq:GeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GeneratingUnit

## eq:GeneratingUnit.nominalP

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:HydroGeneratingUnit
- targetClass: cim:NuclearGeneratingUnit
- targetClass: cim:SolarGeneratingUnit
- targetClass: cim:ThermalGeneratingUnit
- targetClass: cim:GeneratingUnit
- targetClass: cim:WindGeneratingUnit

**Nested Properties:**

### eq:GeneratingUnit.nominalP-valueRangePair

**Path:** `cim:GeneratingUnit.nominalP`  
The attribute shall be a positive value equal to or less than RotatingMachine.ratedS.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        BIND(EXISTS{$this $PATH ?v} AS ?hasvalue).
        #OPTIONAL {$this $PATH ?value }. 
        $this ^cim:RotatingMachine.GeneratingUnit/cim:RotatingMachine.ratedS ?rateds .
        BIND(EXISTS{$this ^cim:RotatingMachine.GeneratingUnit/cim:RotatingMachine.ratedS ?r} AS ?hasrateds).
        #OPTIONAL {$this ^cim:RotatingMachine.GeneratingUnit ?machine }. 
        #OPTIONAL {?machine cim:RotatingMachine.ratedS ?rateds }. 
        FILTER (?hasvalue=true && ?hasrateds=true && (?value<=0 || ?value>?rateds) ) .        
			}
```
  - Messages: `["The value is either negative, zero or greater than RotatingMachine.ratedS."]`

## eq:GroundDisconnector

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GroundDisconnector

## eq:HydroGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:HydroGeneratingUnit

## eq:Jumper

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Jumper

## eq:LimitKind

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:OperationalLimitType

**Nested Properties:**

### eq:LimitKind.tc-duration

**Path:** `rdf:type`  
The duration is always zero if the OperationalLimitType.acceptableDuration is exchanged. Only one limit value exists for the TC type.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this (COUNT(?ol) AS ?tcs) ?adur ?value
			WHERE {      
        $this eu:OperationalLimitType.kind eu:LimitKind.tc .
        $this ^cim:OperationalLimit.OperationalLimitType ?ol .
        ?ol cim:OperationalLimit.OperationalLimitSet ?value .
        OPTIONAL {$this cim:OperationalLimitType.acceptableDuration ?adur }.
			}
      GROUP BY $this ?value ?adur ?value
      HAVING (?tcs>1 || (bound(?adur) && ?adur!=0))
      
```
  - Messages: `["Either OperationalLimitType.acceptableDuration is present and different than 0 or there is more than one limit with TC type. The OperationnalLimitType.acceptableDuration is: {?adur}."]`

### eq:LimitKind.patl-numberOfLimitType

**Path:** `rdf:type`  
The OperationnalLimitType.isInfiniteDuration is set to true. There shall be only one OperationalLimitType of kind PATL per OperationalLimitSet if the PATL is ApparentPowerLimit, ActivePowerLimit, or CurrentLimit for a given Terminal or Equipment.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this (COUNT(?ol) AS ?patls) ?infdur ?value
			WHERE {      
        $this cim:OperationalLimitType.isInfiniteDuration ?infdur .
        $this eu:OperationalLimitType.kind eu:LimitKind.patl .
        $this ^cim:OperationalLimit.OperationalLimitType ?ol .
        ?ol  rdf:type ?typeol .
        ?ol cim:OperationalLimit.OperationalLimitSet ?value .
        FILTER (?typeol IN (cim:ApparentPowerLimit , cim:ActivePowerLimit , cim:CurrentLimit)) .
			}
      GROUP BY $this ?value ?infdur 
      HAVING (?patls>1 || ?infdur=false)
      
```
  - Messages: `["Either there is more than one PATL defined for a given OperationalLimitSet or OperationnalLimitType.isInfiniteDuration is not set to true for PATL type. The OperationnalLimitType.isInfiniteDuration is: {?infdur}."]`

## eq:LinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LinearShuntCompensator

**Nested Properties:**

### eq:ShuntCompensator.nomU-nominalVoltageDifference

**Path:** `rdf:type`  
This should normally be within 10% of the voltage at which the capacitor is connected to the network.

**Severity:** sh:Warning

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Warning)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value   
			WHERE {      
        $this cim:ShuntCompensator.nomU ?value .
        $this cim:Equipment.EquipmentContainer/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?nomv .
        
        FILTER (?value<0.9*?nomv && ?value>1.1*?nomv) .
			}
```
  - Messages: `["The value differs with more than 10% of the nominal voltage abtained via the containment to VoltageLevel."]`

## eq:LoadBreakSwitch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadBreakSwitch

## eq:LoadResponseCharacteristic

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LoadResponseCharacteristic

**Nested Properties:**

### eq:LoadResponseCharacteristic.exponentModel-exponentCoefficient

**Path:** `cim:LoadResponseCharacteristic.exponentModel`  
Indicates the exponential voltage dependency model is to be used. If false, the coefficient model is to be used. The exponential voltage dependency model consist of the attributes:- pVoltageExponent; - qVoltageExponent; - pFrequencyExponent; - qFrequencyExponent. The coefficient model consist of the attributes:- pConstantImpedance; - pConstantCurrent; - pConstantPower; - qConstantImpedance; - qConstantCurrent; - qConstantPower. The sum of pConstantImpedance, pConstantCurrent and pConstantPower shall equal 1. The sum of qConstantImpedance, qConstantCurrent and qConstantPower shall equal 1.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        
        OPTIONAL {$this cim:LoadResponseCharacteristic.pFrequencyExponent ?pfe }.
        OPTIONAL {$this cim:LoadResponseCharacteristic.pVoltageExponent ?pve }.
        OPTIONAL {$this cim:LoadResponseCharacteristic.qFrequencyExponent ?qfe }.
        OPTIONAL {$this cim:LoadResponseCharacteristic.qVoltageExponent ?qve }.
        OPTIONAL {$this cim:LoadResponseCharacteristic.pConstantCurrent ?pcc }.
        OPTIONAL {$this cim:LoadResponseCharacteristic.pConstantImpedance ?pci }.
        OPTIONAL {$this cim:LoadResponseCharacteristic.pConstantPower ?pcp }.
        OPTIONAL {$this cim:LoadResponseCharacteristic.qConstantCurrent ?qcc }.
        OPTIONAL {$this cim:LoadResponseCharacteristic.qConstantImpedance ?qci }.
        OPTIONAL {$this cim:LoadResponseCharacteristic.qConstantPower ?qcp }.
 
        FILTER ((?value=true && (!bound(?pfe) || !bound(?pve) || !bound(?qfe) || !bound(?qve) || bound(?pcc) || bound(?pci) || bound(?pcp) || bound(?qcc) || bound(?qci) || bound(?qcp))) ||
                (?value=false && (bound(?pfe) || bound(?pve) || bound(?qfe) || bound(?qve) || !bound(?pcc) || !bound(?pci) || !bound(?pcp) || !bound(?qcc) || !bound(?qci) || !bound(?qcp))) || 
                (?value=false && bound(?pcc) && bound(?pci) && bound(?pcp) && bound(?qcc) && bound(?qci) && bound(?qcp) && (?pcc+?pci+?pcp!=1 || ?qcc+?qci+?qcp!=1)  )
        ) .
			}
```
  - Messages: `["One of the following occurs: 1) Missing required properties (attributes) for either exponential voltage dependency model or exponential model. 2) There is a mixture between the attributes. 3) The sum of either all active power related coefficients or reactive power related coefficients does not equal 1."]`

## eq:NonlinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NonlinearShuntCompensator

**Nested Properties:**

### eq:ShuntCompensator.maximumSections-numberOfInstances

**Path:** `cim:ShuntCompensator.maximumSections`  
The number of NonlinearShuntCompenstorPoint instances associated with a NonlinearShuntCompensator shall be equal to ShuntCompensator.maximumSections. 

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value ?typesall
			WHERE {
        {
        SELECT $this (COUNT(?typeall) AS ?typesall)
        WHERE {
            $this ^cim:NonlinearShuntCompensatorPoint.NonlinearShuntCompensator/rdf:type ?typeall .
            #?nscpointsall cim:NonlinearShuntCompensatorPoint.NonlinearShuntCompensator  $this .
            #?nscpointsall rdf:type ?typeall .
          }
        GROUP BY $this ?typesall
        }
        $this $PATH ?value .  
        FILTER (?value!=?typesall) .
			}
```
  - Messages: `["The number of NonlinearShuntCompenstorPoint instances associated with a NonlinearShuntCompensator does not equal to ShuntCompensator.maximumSections."]`

### eq:ShuntCompensator.nomU-nominalVoltageDifference

**Path:** `rdf:type`  
This should normally be within 10% of the voltage at which the capacitor is connected to the network.

**Severity:** sh:Warning

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Warning)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value   
			WHERE {      
        $this cim:ShuntCompensator.nomU ?value .
        $this cim:Equipment.EquipmentContainer/cim:VoltageLevel.BaseVoltage/cim:BaseVoltage.nominalVoltage ?nomv .
        
        FILTER (?value<0.9*?nomv && ?value>1.1*?nomv) .
			}
```
  - Messages: `["The value differs with more than 10% of the nominal voltage abtained via the containment to VoltageLevel."]`

## eq:NuclearGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NuclearGeneratingUnit

## eq:OperationalLimitType

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:OperationalLimitType

**Nested Properties:**

### eq:OperationalLimitType.acceptableDuration-usage

**Path:** `cim:OperationalLimitType.acceptableDuration`  
The attribute has meaning only if the flag isInfiniteDuration is set to false, hence it shall not be exchanged when isInfiniteDuration is set to true.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        BIND(EXISTS{$this $PATH ?v } AS ?hasvalue). 
        $this cim:OperationalLimitType.isInfiniteDuration ?indur .
        FILTER (?hasvalue=true && ?indur=true ) .        
			}
```
  - Messages: `["The attribute is present and .isInfiniteDuration is set to true."]`

### eq:OperationalLimitType.isInfiniteDuration-usage

**Path:** `cim:OperationalLimitType.acceptableDuration`  
If false, the limit has definite duration which is defined by the attribute acceptableDuration.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        #OPTIONAL {$this $PATH ?value }.
        $this $PATH ?value .
        BIND(EXISTS{$this $PATH ?v} AS ?hasvalue).
        $this cim:OperationalLimitType.isInfiniteDuration ?indur .
        FILTER (?hasvalue=false && ?indur=false ) .        
			}
```
  - Messages: `["The attribute is not present when .isInfiniteDuration is set ot false."]`

## eq:PhaseTapChangerAsymmetrical

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerAsymmetrical

**Nested Properties:**

### eq:PhaseTapChangerAsymmetrical.windingConnectionAngle-valueRange

**Path:** `cim:PhaseTapChangerAsymmetrical.windingConnectionAngle`  
The attribute can only be multiples of 30 degrees.  The allowed range is -150 degrees to 150 degrees excluding 0.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value . 
        FILTER (contains(str(?value), ".") || (?value!=-150 && ?value!=-120 && ?value!=-90 && ?value!=-60 && ?value!=-30 && ?value!=150 && ?value!=120 && ?value!=90 && ?value!=60 && ?value!=30)) .        
			}
```
  - Messages: `["The value is not an integer, multiples of 30 degrees in the range of -150 degrees to 150 degrees excluding 0."]`

### eq:PhaseTapChangerNonLinear.xMin-valueRangePair

**Path:** `cim:PhaseTapChangerNonLinear.xMin`  
PowerTransformerEnd.x shall be consistent with PhaseTapChangerLinear.xMin and PhaseTapChangerNonLinear.xMin. In case of inconsistency, PowerTransformerEnd.x shall be used.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value . 
        $this cim:PhaseTapChanger.TransformerEnd/cim:PowerTransformerEnd.x ?x . 
        #$this cim:PhaseTapChanger.TransformerEnd ?theend . 
        #?theend cim:PowerTransformerEnd.x ?x . 
        FILTER (?value!=?x ) .        
			}
```
  - Messages: `["Inconsistency between PowerTransformerEnd.x and PhaseTapChangerNonLinear.xMin."]`

## eq:PhaseTapChangerLinear

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerLinear

**Nested Properties:**

### eq:PhaseTapChangerLinear.xMin-valueRangePair

**Path:** `cim:PhaseTapChangerLinear.xMin`  
PowerTransformerEnd.x shall be consistent with PhaseTapChangerLinear.xMin and PhaseTapChangerNonLinear.xMin. In case of inconsistency, PowerTransformerEnd.x shall be used.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value . 
        $this cim:PhaseTapChanger.TransformerEnd/cim:PowerTransformerEnd.x ?x . 
        #$this cim:PhaseTapChanger.TransformerEnd ?theend . 
        #?theend cim:PowerTransformerEnd.x ?x . 
        FILTER (?value!=?x ) .        
			}
```
  - Messages: `["Inconsistency between PowerTransformerEnd.x and PhaseTapChangerLinear.xMin."]`

## eq:PhaseTapChangerSymmetrical

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerSymmetrical

**Nested Properties:**

### eq:PhaseTapChangerNonLinear.xMin-valueRangePair

**Path:** `cim:PhaseTapChangerNonLinear.xMin`  
PowerTransformerEnd.x shall be consistent with PhaseTapChangerLinear.xMin and PhaseTapChangerNonLinear.xMin. In case of inconsistency, PowerTransformerEnd.x shall be used.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value . 
        $this cim:PhaseTapChanger.TransformerEnd/cim:PowerTransformerEnd.x ?x . 
        #$this cim:PhaseTapChanger.TransformerEnd ?theend . 
        #?theend cim:PowerTransformerEnd.x ?x . 
        FILTER (?value!=?x ) .        
			}
```
  - Messages: `["Inconsistency between PowerTransformerEnd.x and PhaseTapChangerNonLinear.xMin."]`

## eq:PhaseTapChangerTabular

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerTabular

## eq:PowerElectronicsConnection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PowerElectronicsConnection

## eq:PowerTransformer

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PowerTransformer

**Nested Properties:**

### eq:PowerTransformerEnd.ratedU-valueRange

**Path:** `rdf:type`  
A high voltage side, as given by TransformerEnd.endNumber, shall have a ratedU that is greater than or equal to ratedU for the lower voltage sides. The attribute shall be a positive value.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value ?ends
			WHERE {
        {
        SELECT $this (COUNT(?typeend) AS ?ends)
        WHERE {
        $this ^cim:PowerTransformerEnd.PowerTransformer/rdf:type ?typeend .
        }
        GROUP BY $this ?typeend
        }
        
        ?end1 cim:PowerTransformerEnd.PowerTransformer $this .
        ?end1 cim:TransformerEnd.endNumber  1.
        ?end1 cim:PowerTransformerEnd.ratedU  ?value .
        ?end2 cim:PowerTransformerEnd.PowerTransformer $this  .
        ?end2 cim:TransformerEnd.endNumber  2 .
        ?end2 cim:PowerTransformerEnd.ratedU  ?rateduend2 .
        #BIND(EXISTS{$this cim:PowerTransformerEnd.PowerTransformer/cim:TransformerEnd.endNumber  3} AS ?isthreew).
        #?end3 cim:PowerTransformerEnd.PowerTransformer $this .
        #?end3 cim:TransformerEnd.endNumber  3 .
        #?end3 cim:PowerTransformerEnd.ratedU  ?rateduend3 .
        OPTIONAL {?end3 cim:PowerTransformerEnd.PowerTransformer $this } .
        OPTIONAL {?end3 cim:TransformerEnd.endNumber  3 }.
        OPTIONAL {?end3 cim:PowerTransformerEnd.ratedU  ?rateduend3 }.

        FILTER (((?value<?rateduend2 || ?value<=0 || ?rateduend2<=0) && ?ends=2 && ?end1!=?end2 && ?end3=?end1) || (?ends=3 && ?end1!=?end2 && ?end1!=?end3 && ?end2!=?end3 && (?value<?rateduend2 || ?rateduend2<?rateduend3 || ?value<=0 || ?rateduend2<=0 || ?rateduend3<=0))) .        
			}

      
```
  - Messages: `["The PowerTransformerEnd.ratedU does not fuifil one of the following: 1) it is not a positive value; 2) the value of the high voltage side shall be greater than or equal to ratedU for the lower voltage sides."]`

### eq:TransformerEnd.endNumber-unique

**Path:** `rdf:type`  
Highest voltage winding should be 1.  Each end within a power transformer should have a unique subsequent end number.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        {
        SELECT $this (COUNT(DISTINCT ?endnumber) as ?countd) (COUNT(?endnumber) as ?count) (MIN(?endnumber) as ?minendnumber) (MAX(?ratedu) as ?maxratedu) 
        WHERE {
          $this ^cim:PowerTransformerEnd.PowerTransformer ?ends .
          ?ends rdf:type ?endtype .
          ?ends cim:TransformerEnd.endNumber ?endnumber .
          ?ends cim:PowerTransformerEnd.ratedU ?ratedu .
        }
        GROUP BY $this ?endtype
        }
        
        ?end1 cim:PowerTransformerEnd.PowerTransformer $this .
        ?end1 cim:TransformerEnd.endNumber ?minendnumber.
        ?end1 cim:PowerTransformerEnd.ratedU ?end1ratedu .
        
        ?end2 cim:PowerTransformerEnd.PowerTransformer $this .
        ?end2 cim:PowerTransformerEnd.ratedU ?maxratedu .
        BIND("" as ?value).
        FILTER(?countd!=?count || (?countd=?count && ?end1ratedu!=?maxratedu && ?end1!=?end2) ).
			} 
      
```
  - Messages: `["The PowerTransformer has TransformerEnd.endNumber which is not unique or the PowerTransformerEnd with endNumber 1 is not the highest voltage winding."]`

### eq:PowerTransformer-associationNotUsed

**Path:** `rdf:type`  
The inherited association ConductingEquipment.BaseVoltage should not be used.  The association from TransformerEnd to BaseVoltage should be used instead.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        $this cim:ConductingEquipment.BaseVoltage ?value .
        BIND(EXISTS{$this cim:ConductingEquipment.BaseVoltage ?v } AS ?hasvalue). 
        FILTER (?hasvalue=true) .        
			}
```
  - Messages: `["The inherited association ConductingEquipment.BaseVoltage is used."]`

### eq:PowerTransformerEnd.ratedS-valueRange2winding

**Path:** `rdf:type`  
For a two-winding transformer the values for the high and low voltage sides shall be identical. 

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value ?ends
			WHERE {
        {
        SELECT $this (COUNT(?typeend) AS ?ends)
        WHERE {
        $this ^cim:PowerTransformerEnd.PowerTransformer/rdf:type ?typeend .
        }
        GROUP BY $this ?typeend
        }
        
        ?end1 cim:PowerTransformerEnd.PowerTransformer $this .
        ?end1 cim:TransformerEnd.endNumber  1.
        ?end1 cim:PowerTransformerEnd.ratedS  ?value .
        #OPTIONAL {?end1 cim:PowerTransformerEnd.ratedS  ?value }.
        BIND(EXISTS{?end1 cim:PowerTransformerEnd.ratedS  ?v} AS ?hasvalue).
        ?end2 cim:PowerTransformerEnd.PowerTransformer $this  .
        ?end2 cim:TransformerEnd.endNumber  2 .
        ?end2 cim:PowerTransformerEnd.ratedS  ?ratedsend2 .
        BIND(EXISTS{?end2 cim:PowerTransformerEnd.ratedS  ?r} AS ?hasratedsend2).
        #OPTIONAL {?end2 cim:PowerTransformerEnd.ratedS  ?ratedsend2 }.

        FILTER (?hasvalue=true && ?hasratedsend2=true && ?end1!=?end2 && ?value!=?ratedsend2) .        
			}
      HAVING(?ends=2)
      
```
  - Messages: `["The value is different for a two-winding transformer."]`

## eq:PowerTransformer-twoWinding

**Severity:** sh:Violation

**Nested Properties:**

### eq:PowerTransformerEnd-secondWindingValues

**Path:** `rdf:type`  
1) for a two Terminal PowerTransformer the high voltage (TransformerEnd.endNumber=1) PowerTransformerEnd has non zero values on r, r0, x, and x0 while the low voltage (TransformerEnd.endNumber=2) PowerTransformerEnd has zero values for r, r0, x, and x0.  Parameters are always provided, even if the PowerTransformerEnds have the same rated voltage.  In this case, the parameters are provided at the PowerTransformerEnd which has TransformerEnd.endNumber equal to 1.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        ?value cim:PowerTransformerEnd.PowerTransformer $this .  
        ?value cim:TransformerEnd.endNumber 2 .
        #?value cim:TransformerEnd.endNumber ?endnumber .
        ?value cim:PowerTransformerEnd.r ?r .
        ?value cim:PowerTransformerEnd.r0 ?r0 .
        ?value cim:PowerTransformerEnd.x ?x .
        ?value cim:PowerTransformerEnd.x0 ?x0 .
        FILTER (!(?r=0 && ?r0=0 && ?x=0 && ?x0=0)).
        #FILTER ((!(?r=0 && ?r0=0 && ?x=0 && ?x0=0) && ?endnumber=2) || (!(?r!=0 && ?r0!=0 && ?x!=0 && ?x0!=0) && ?endnumber=1)).
        #FILTER (?r!=0 || ?r0!=0 || ?x!=0 || ?x0!=0).
			} 
```
  - Messages: `["Non-zero values for the PowerTransformerEnd with TransformerEnd.endNumber=2 for a two Terminal PowerTransformer."]`

## eq:PowerTransformerEnd

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PowerTransformerEnd

**Nested Properties:**

### eq:PowerTransformerEnd.r-valueRange

**Path:** `cim:PowerTransformerEnd.r`  
The attribute shall be equal to or greater than zero for non-equivalent transformers.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value . 
        OPTIONAL {$this cim:Equipment.aggregate ?aggregate }.
        #BIND(EXISTS{$this cim:Equipment.aggregate ?a } AS ?hasaggregate).
        FILTER ((!bound(?aggregate) || ?aggregate=false) && ?value<0 ) .        
			}
```
  - Messages: `["The value is negative for a non-equivalent transformer."]`

### eq:PowerTransformerEnd-terminalConsistency

**Path:** `rdf:type`  
In all cases a PowerTransformer models a group of physical devices acting together to transform power among terminals and in one physical location.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this   
			WHERE {      
        $this cim:TransformerEnd.Terminal/cim:Terminal.ConductingEquipment ?endtermpt .
        $this cim:PowerTransformerEnd.PowerTransformer ?pendpt .
        
        FILTER (?endtermpt!=?pendpt) .
			}
```
  - Messages: `["The Terminal referenced by TransformerEnd.Terminal points to a PowerTransformer which is different than the referenced element via PowerTransformerEnd.PowerTransformer."]`

## eq:RatioTapChanger

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RatioTapChanger

## eq:ReactiveCapabilityCurve-curveYvalues

For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure. 

**Severity:** sh:Violation

**Messages:**
- "CurveData associated with a ReactiveCapabilityCurve does not have both .y1value and .y2value defined."

**Targets:**
- targetClass: cim:CurveData

## eq:RegularTimePoint

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RegularTimePoint

## eq:RegulatingControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RegulatingControl

**Nested Properties:**

### eq:RegulatingControl-terminalConnectivityNode

**Path:** `cim:RegulatingControl.Terminal`  
The specified terminal shall be associated with the connectivity node of the controlled point.  The most specific subtype of RegulatingControl shall be used in case such equipment participate in the control, e.g. TapChangerControl for tap changers.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

	    SELECT $this ?value 
      WHERE {
        $this $PATH ?value .
        BIND(EXISTS{?value cim:Terminal.ConnectivityNode ?cn} AS ?hascn).
        #OPTIONAL {?value cim:Terminal.ConnectivityNode ?cn }.
        FILTER (?hascn=false) .
        } 
```
  - Messages: `["The Terminal referenced by the RegulatingControl is not associated with a ConnectivityNode."]`

## eq:SeriesCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SeriesCompensator

## eq:SolarGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SolarGeneratingUnit

## eq:StaticVarCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:StaticVarCompensator

## eq:Switch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Switch

## eq:SynchronousMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachine

## eq:TapChanger

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RatioTapChanger
- targetClass: cim:PhaseTapChangerTabular
- targetClass: cim:PhaseTapChangerSymmetrical
- targetClass: cim:PhaseTapChangerAsymmetrical
- targetClass: cim:PhaseTapChangerLinear

**Nested Properties:**

### eq:TapChanger.ltcFlag-tapChangerControl

**Path:** `cim:TapChanger.ltcFlag`  
When TapChanger.ltcFlag=false and TapChanger.TapChangerControl is present an artificial tap changer can be used to simulate control behaviour in power flow.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value  
			WHERE {      
        $this $PATH ?value .
        BIND(EXISTS{$this cim:TapChanger.TapChangerControl ?tcc } AS ?hastcc).
        
        FILTER (?hastcc=true && ?value=false) .
			}
```
  - Messages: `["An artificial tap changer is used to simulate control behaviour in power flow."]`

### eq:DCConverterUnit-tapChangerControl

**Path:** `rdf:type`  
No TapChangerControl is used for the converter transformer, the control function is described in the ACDCConverter-s.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value  
			WHERE {      
        OPTIONAL {$this cim:TapChanger.TapChangerControl ?value }.
        OPTIONAL {$this cim:RatioTapChanger.TransformerEnd/cim:PowerTransformerEnd.PowerTransformer/cim:Equipment.EquipmentContainer/rdf:type ?typeratiotc }.
        OPTIONAL {$this cim:PhaseTapChanger.TransformerEnd/cim:PowerTransformerEnd.PowerTransformer/cim:Equipment.EquipmentContainer/rdf:type ?typephasetc }.
        
        FILTER (bound(?value) && ((bound(?typeratiotc) && ?typeratiotc=cim:DCConverterUnit) || (bound(?typephasetc) && ?typephasetc=cim:DCConverterUnit))) .
			}
```
  - Messages: `["TapChangerControl is association to a transformer contained in DCConverterUnit."]`

## eq:TapChangerControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TapChangerControl

**Nested Properties:**

### eq:RegulatingControl-terminalConnectivityNode

**Path:** `cim:RegulatingControl.Terminal`  
The specified terminal shall be associated with the connectivity node of the controlled point.  The most specific subtype of RegulatingControl shall be used in case such equipment participate in the control, e.g. TapChangerControl for tap changers.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

	    SELECT $this ?value 
      WHERE {
        $this $PATH ?value .
        BIND(EXISTS{?value cim:Terminal.ConnectivityNode ?cn} AS ?hascn).
        #OPTIONAL {?value cim:Terminal.ConnectivityNode ?cn }.
        FILTER (?hascn=false) .
        } 
```
  - Messages: `["The Terminal referenced by the RegulatingControl is not associated with a ConnectivityNode."]`

## eq:Terminal

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GroundDisconnector
- targetClass: cim:Ground
- targetClass: cim:GroundingImpedance
- targetClass: cim:PetersenCoil

## eq:Terminal.phases

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ConnectivityNode

**Nested Properties:**

### eq:Terminal.phases-consistencyConnectivityNode

**Path:** `rdf:type`  
The phase code on terminals connecting same ConnectivityNode or same TopologicalNode as well as for equipment between two terminals shall be consistent.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value2 ?terms ?value1 ?value
			WHERE {
        {
        SELECT $this (COUNT(?typeterm) AS ?terms) ?value
        WHERE {
        $this ^cim:Terminal.ConnectivityNode ?value .
        ?value rdf:type ?typeterm .
        #?term cim:Terminal.ConnectivityNode $this .
        #?term rdf:type ?typeterm .
        }
        GROUP BY $this ?typeterm ?value
        HAVING (?terms>1)
        }
      
        #$this ^cim:Terminal.ConnectivityNode ?value  .
        $this ^cim:Terminal.ConnectivityNode ?term2  .
        ?value cim:Terminal.phases ?value1  .
        OPTIONAL {?term2 cim:Terminal.phases ?value2 } .
      
        #?value cim:Terminal.ConnectivityNode $this  .
        #?term1 cim:Terminal.phases ?value1  .
        #?term2 cim:Terminal.ConnectivityNode $this  .
        #?term2 cim:Terminal.phases ?value2.
        
        #BIND(EXISTS{?term1 cim:Terminal.phases ?v1} AS ?hasvalue1).
  
        
        #BIND(EXISTS{?term2 cim:Terminal.phases ?v2} AS ?hasvalue2).        
        #FILTER ((?terms>1 && ?hasvalue2=true && ?hasvalue1=true && ?term1!=?term2 && (?value1=cim:PhaseCode.ABCN || ?value1=cim:PhaseCode.N) && (?value2!=cim:PhaseCode.ABCN && ?value2!=cim:PhaseCode.N)) ||
        #(?terms>1 && ?hasvalue2=true && ?hasvalue1=true && ?term1!=?term2 && (?value1=cim:PhaseCode.ABC) && (?value2!=cim:PhaseCode.ABC)) ||
        #(?terms>1 && ?hasvalue1=true && ?hasvalue2=false && ?term1!=?term2 && (?value1=cim:PhaseCode.ABCN || ?value1=cim:PhaseCode.N))
        #) .
        FILTER ((?value!=?term2 && bound(?value2) && (?value1=cim:PhaseCode.ABCN || ?value1=cim:PhaseCode.N) && (?value2!=cim:PhaseCode.ABCN && ?value2!=cim:PhaseCode.N)) ||
        (?value!=?term2 && bound(?value2) && (?value1=cim:PhaseCode.ABC) && (?value2!=cim:PhaseCode.ABC)) ||
        (?value!=?term2 && !bound(?value2) && (?value1=cim:PhaseCode.ABCN || ?value1=cim:PhaseCode.N))
        ) .
			}
```
  - Messages: `["The phase codes for the connected terminals are not consistent. Terminal 1 code:{?value1} Terminal 2 code: {?value2}."]`

## eq:ThermalGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ThermalGeneratingUnit

## eq:VoltageLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VoltageLimit

**Nested Properties:**

### eq:LimitKind.patl-allowedType

**Path:** `rdf:type`  
The Permanent Admissible Transmission Loading (PATL) is the loading in amperes, MVA or MW that can be accepted by a network branch for an unlimited duration without any risk for the material.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {      
        $this cim:OperationalLimit.OperationalLimitType/eu:OperationalLimitType.kind ?value.
        #?type eu:OperationalLimitType.kind ?value .

        FILTER (?value=eu:LimitKind.patl) .
			}
```
  - Messages: `["PATL type is provided for VoltageLimit."]`

## eq:VsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VsConverter

## eq:WindGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindGeneratingUnit

