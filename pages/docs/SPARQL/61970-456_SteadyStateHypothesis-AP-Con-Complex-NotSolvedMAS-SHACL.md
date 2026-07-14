# 61970-456_SteadyStateHypothesis-AP-Con-Complex-NotSolvedMAS-SHACL

## ssh456n:Equipment

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentShunt
- targetClass: cim:EquivalentBranch
- targetClass: cim:PostLineSensor
- targetClass: cim:PotentialTransformer
- targetClass: cim:Fuse
- targetClass: cim:SolarGeneratingUnit
- targetClass: cim:ACLineSegment
- targetClass: cim:VsConverter
- targetClass: cim:Equipment
- targetClass: cim:ConformLoad
- targetClass: cim:CurrentTransformer
- targetClass: cim:LinearShuntCompensator
- targetClass: cim:NuclearGeneratingUnit
- targetClass: cim:HydroPump
- targetClass: cim:DCBusbar
- targetClass: cim:Clamp
- targetClass: cim:ExternalNetworkInjection
- targetClass: cim:WindGeneratingUnit
- targetClass: cim:DCShunt
- targetClass: cim:DCSeriesDevice
- targetClass: cim:CsConverter
- targetClass: cim:Cut
- targetClass: cim:PowerElectronicsConnection
- targetClass: cim:StationSupply
- targetClass: cim:EnergyConsumer
- targetClass: cim:Breaker
- targetClass: cim:LoadBreakSwitch
- targetClass: cim:EquivalentInjection
- targetClass: cim:AsynchronousMachine
- targetClass: cim:SeriesCompensator
- targetClass: cim:DCBreaker
- targetClass: cim:DCLineSegment
- targetClass: cim:DisconnectingCircuitBreaker
- targetClass: cim:Jumper
- targetClass: cim:BatteryUnit
- targetClass: cim:SynchronousMachine
- targetClass: cim:DCSwitch
- targetClass: cim:HydroGeneratingUnit
- targetClass: cim:PhotoVoltaicUnit
- targetClass: cim:NonlinearShuntCompensator
- targetClass: cim:PetersenCoil
- targetClass: cim:ThermalGeneratingUnit
- targetClass: cim:DCChopper
- targetClass: cim:PowerElectronicsWindUnit
- targetClass: cim:Switch
- targetClass: cim:DCGround
- targetClass: cim:NonConformLoad
- targetClass: cim:PowerTransformer
- targetClass: cim:SurgeArrester
- targetClass: cim:GroundDisconnector
- targetClass: cim:StaticVarCompensator
- targetClass: cim:FaultIndicator
- targetClass: cim:GeneratingUnit
- targetClass: cim:Ground
- targetClass: cim:DCDisconnector
- targetClass: cim:Disconnector
- targetClass: cim:EnergySource
- targetClass: cim:GroundingImpedance
- targetClass: cim:Junction
- targetClass: cim:BusbarSection
- targetClass: cim:WaveTrap

## ssh456n:EquivalentInjection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentInjection

**Nested Properties:**

### ssh456n:EquivalentInjection.p-limits

**Path:** `cim:EquivalentInjection.p`  
**Name:** C:456:SSH:EquivalentInjection.p:limits  
The negated value (necessary due to sign convention) of EquivalentInjection.p shall be less than or equal to EquivalentInjection.maxP and shall be greater than or equal to EquivalentInjection.minP.

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
        #OPTIONAL {$this cim:EquivalentInjection.maxP ?maxp} . 
        #OPTIONAL {$this cim:EquivalentInjection.minP ?minp} .
        $this cim:EquivalentInjection.maxP ?maxp . 
        $this cim:EquivalentInjection.minP ?minp .
        #FILTER (bound(?maxp) && bound(?minp) && !(-?value<=?maxp && -?value>=?minp && ?value!=0) && !(?value<=?maxp && ?value>=?minp && ?value=0)) .  
        FILTER (!(-?value<=?maxp && -?value>=?minp && ?value!=0) && !(?value<=?maxp && ?value>=?minp && ?value=0)) .        
			}
```
  - Messages: `["Active power is outside defined active power limits."]`

### ssh456n:EquivalentInjection.q-limits

**Path:** `cim:EquivalentInjection.q`  
**Name:** C:456:SSH:EquivalentInjection.q:limits  
The negated value (necessary due to sign convention) of EquivalentInjection.q shall be less than or equal to EquivalentInjection.maxQ and shall be greater than or equal to EquivalentInjection.minQ.

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
        #OPTIONAL {$this cim:EquivalentInjection.maxQ ?maxq} . 
        #OPTIONAL {$this cim:EquivalentInjection.minQ ?minq} .
        $this cim:EquivalentInjection.maxQ ?maxq . 
        $this cim:EquivalentInjection.minQ ?minq .
        #FILTER (bound(?maxq) && bound(?minq) && !(-?value<=?maxq && -?value>=?minq && ?value!=0) && !(?value<=?maxq && ?value>=?minq && ?value=0)) .  
        FILTER (!(-?value<=?maxq && -?value>=?minq && ?value!=0) && !(?value<=?maxq && ?value>=?minq && ?value=0)) .        
			}
```
  - Messages: `["Reactive power is outside defined reactive power limits."]`

### ssh456n:EquivalentInjection-regulation

**Path:** `cim:EquivalentInjection.regulationCapability`  
**Name:** C:456:SSH:EquivalentInjection:regulation  
If EquivalentInjection.regulationCapability in EQ is true, then EquivalentInjection.regulationStatus and EquivalentInjection.regulationTarget are required in SSH. If EquivalentInjection.regulationCapability in EQ is false, then EquivalentInjection.regulationStatus and EquivalentInjection.regulationTarget are not exchanged in SSH.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value.
        OPTIONAL {$this cim:EquivalentInjection.regulationStatus ?rstatus}.
        OPTIONAL {$this cim:EquivalentInjection.regulationTarget ?rtarget}. 
        FILTER ((?value=true && (!bound(?rstatus) || !bound(?rtarget))) || (?value=false && (bound(?rstatus) || bound(?rtarget)))) .        
			}
```
  - Messages: `["Inconsistancy between EquivalentInjection.regulationCapability,  EquivalentInjection.regulationStatus and EquivalentInjection.regulationTarget. "]`

## ssh456n:ExternalNetworkInjection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ExternalNetworkInjection

**Nested Properties:**

### ssh456n:ExternalNetworkInjection.p-limits

**Path:** `cim:ExternalNetworkInjection.p`  
**Name:** C:456:SSH:ExternalNetworkInjection.p:limits  
The negated value (necessary due to sign convention) of ExternalNetworkInjection.p shall be less than or equal to ExternalNetworkInjection.maxP and shall be greater than or equal to ExternalNetworkInjection.minP.

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
        $this cim:ExternalNetworkInjection.maxP ?maxp . 
        $this cim:ExternalNetworkInjection.minP ?minp .
        FILTER (!(-?value<=?maxp && -?value>=?minp && ?value!=0) && !(?value<=?maxp && ?value>=?minp && ?value=0)) .        
			}
```
  - Messages: `["Active power is outside defined active power limits."]`

### ssh456n:ExternalNetworkInjection.q-limits

**Path:** `cim:ExternalNetworkInjection.q`  
**Name:** C:456:SSH:ExternalNetworkInjection.q:limits  
The negated value (necessary due to sign convention) of ExternalNetworkInjection.q shall be less than or equal to ExternalNetworkInjection.maxQ and shall be greater than or equal to ExternalNetworkInjection.minQ.

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
        $this cim:ExternalNetworkInjection.maxQ ?maxq . 
        $this cim:ExternalNetworkInjection.minQ ?minq .
        FILTER (!(-?value<=?maxq && -?value>=?minq && ?value!=0) && !(?value<=?maxq && ?value>=?minq && ?value=0)) .        
			}
```
  - Messages: `["Reactive power is outside defined reactive power limits."]`

## ssh456n:GeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetNode: cim:AllGeneratingUnit

**Nested Properties:**

### ssh456n:GeneratingUnit-singleActivePowerSlack

**Path:** `rdf:type`  
**Name:** C:456:SSH:NA:singleActivePowerSlack  
Active power slack by a single generator per ControlArea: one generator has GeneratingUnit.normalPF set to a highest value (non-zero) and all other generating units have a zero GeneratingUnit.normalPF.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value ?countm ?countd (COUNT(?npf1) as ?counte) ?countall
        WHERE {
          ?gu cim:GeneratingUnit.normalPF ?npf1 .
          BIND ("" AS ?value).
          FILTER (?npf1=?countm)
          {
            SELECT $this (COUNT(DISTINCT ?npf) as ?countd) (MAX(?npf) as ?countm) (COUNT(?npf) as ?countall)
            WHERE {
              ?gu cim:GeneratingUnit.normalPF ?npf .
            }
            GROUP BY $this datatype(?npf)
          }
        }
        GROUP BY $this ?value ?countm ?countd datatype(?npf1) ?countall
        HAVING((?countd<2 && ?countall!=1) || ?countm=0 || ?counte!=1)
      
```
  - Messages: `["Either there is no highest value among GeneratingUnit.normalPF or there are multiple maximum values which are the same."]`

## ssh456n:RegulatingControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RegulatingControl
- targetClass: cim:TapChangerControl

**Nested Properties:**

### ssh456n:RegulatingControl.targetValue-value

**Path:** `cim:RegulatingControl.targetValue`  
**Name:** C:456:SSH:RegulatingControl.targetValue:value  
RegulatingControl.targetValue shall be positive value in cases where the RegulatingControl.mode is set to voltage in EQ profile. 

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        $this cim:RegulatingControl.mode cim:RegulatingControlModeKind.voltage .
        $this $PATH ?value .
        FILTER (?value<=0 ) . 
        #FILTER (?value<=0 && ?mode=cim:RegulatingControlModeKind.voltage) .        
			}
```
  - Messages: `["The value is negative or zero for RegulatingControl in voltage mode."]`

## ssh456n:RotatingMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachine
- targetClass: cim:AsynchronousMachine

**Nested Properties:**

### ssh456n:RotatingMachine.p-limits

**Path:** `cim:RotatingMachine.p`  
**Name:** C:456:SSH:RotatingMachine.p:limits  
The negated value (necessary due to sign convention) of RotatingMachine.p shall be less than or equal to GeneratingUnit.maxOperatingP and shall be greater than or equal to GeneratingUnit.minOperatingP of the associated GeneratingUnit.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        $this cim:Equipment.inService true .
        $this cim:RotatingMachine.GeneratingUnit ?genunit.
        #BIND(EXISTS{$this cim:RotatingMachine.GeneratingUnit ?hasgenunit} AS ?hasgu).
        $this $PATH ?value .
        ?genunit cim:GeneratingUnit.maxOperatingP ?maxp . 
        ?genunit cim:GeneratingUnit.minOperatingP ?minp .
        FILTER (!(-?value<=?maxp && -?value>=?minp && ?value!=0) && !(?value<=?maxp && ?value>=?minp && ?value=0)) .        
        #FILTER (?hasgu=true && !(-?value<=?maxp && -?value>=?minp && ?value!=0) && !(?value<=?maxp && ?value>=?minp && ?value=0)) .        
			}
```
  - Messages: `["Active power is outside defined active power limits."]`

### ssh456n:RotatingMachine.q-limits

**Path:** `cim:RotatingMachine.q`  
**Name:** C:456:SSH:RotatingMachine.q:limits  
In case there is no ReactiveCapabilityCurve associated with the SynchronousMachine, the negated value (necessary due to sign convention) of RotatingMachine.q shall be less than or equal to SynchronousMachine.maxQ and shall be greater than or equal to SynchronousMachine.minQ.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value
			WHERE {
        $this cim:Equipment.inService true .
        $this $PATH ?value .
        BIND(EXISTS{$this cim:SynchronousMachine.InitialReactiveCapabilityCurve ?curve} AS ?hascurve).
        #OPTIONAL {$this cim:SynchronousMachine.maxQ ?maxq}.
        #OPTIONAL {$this cim:SynchronousMachine.minQ ?minq}.
        $this cim:SynchronousMachine.maxQ ?maxq.
        $this cim:SynchronousMachine.minQ ?minq.
        #FILTER (?hascurve=false && bound(?maxq) && bound(?minq) && !(-?value<=?maxq && -?value>=?minq && ?value!=0) && !(?value<=?maxq && ?value>=?minq && ?value=0)) .  
        FILTER (?hascurve=false && !(-?value<=?maxq && -?value>=?minq && ?value!=0) && !(?value<=?maxq && ?value>=?minq && ?value=0)) .           
			}
```
  - Messages: `["Reactive power is outside defined reactive power limits."]`

## ssh456n:ShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LinearShuntCompensator
- targetClass: cim:NonlinearShuntCompensator

**Nested Properties:**

### ssh456n:ShuntCompensator.sections-value

**Path:** `cim:ShuntCompensator.sections`  
**Name:** C:456:SSH:ShuntCompensator.sections:value  
In cases where RegulatingControl.discrete is true and RegulatingControl.enabled is true, ShuntCompensator.sections shall be integer. 

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
        #OPTIONAL {$this cim:RegulatingCondEq.RegulatingControl ?contr}.
        #?contr cim:RegulatingControl.discrete ?discrete . 
        #?contr cim:RegulatingControl.enabled ?enabled .
        $this cim:RegulatingCondEq.RegulatingControl ?contr.
        ?contr cim:RegulatingControl.discrete true . 
        ?contr cim:RegulatingControl.enabled true .
        #FILTER (STRENDS(str(?value), ".") && !REGEX(STRAFTER(str(?value), "."), "^[0]$", "i") && bound(?contr) && ?discrete=true && ?enabled=true) .
        FILTER (STRENDS(str(?value), ".") && !REGEX(STRAFTER(str(?value), "."), "^[0]$", "i") ) .        
			}
```
  - Messages: `["The value is not integer for an active discrete regulating control."]`

## ssh456n:SynchronousMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachine

**Nested Properties:**

### ssh456n:SynchronousMachine.operatingMode-matchType

**Path:** `cim:SynchronousMachine.operatingMode`  
**Name:** C:456:SSH:SynchronousMachine.operatingMode:matchType  
The SynchronousMachine.operatingMode shall be consistent with the SynchronousMachine.type. SynchronousMachine.operatingMode = motor shall be provided for SynchronousMachine.type in (motor, generatorOrMotor, motorOrCondenser, generatorOrCondenserOrMotor), SynchronousMachine.operatingMode = condenser shall be provided for SynchronousMachine.type in (condenser, generatorOrCondenser, motorOrCondenser, generatorOrCondenserOrMotor), and SynchronousMachine.operatingMode = generator shall be provided for SynchronousMachine.type in (generator, generatorOrMotor, generatorOrCondenser, generatorOrCondenserOrMotor).

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
        $this cim:SynchronousMachine.type ?type .
         
        FILTER ((?value=cim:SynchronousMachineOperatingMode.motor && ?type NOT IN (cim:SynchronousMachineKind.motor , cim:SynchronousMachineKind.generatorOrMotor , cim:SynchronousMachineKind.motorOrCondenser , cim:SynchronousMachineKind.generatorOrCondenserOrMotor)) ||
        (?value=cim:SynchronousMachineOperatingMode.condenser && ?type NOT IN (cim:SynchronousMachineKind.condenser , cim:SynchronousMachineKind.generatorOrCondenser , cim:SynchronousMachineKind.motorOrCondenser , cim:SynchronousMachineKind.generatorOrCondenserOrMotor)) ||
        (?value=cim:SynchronousMachineOperatingMode.generator && ?type NOT IN (cim:SynchronousMachineKind.generator , cim:SynchronousMachineKind.generatorOrMotor , cim:SynchronousMachineKind.generatorOrCondenser , cim:SynchronousMachineKind.generatorOrCondenserOrMotor))) .        
			}
```
  - Messages: `["The value of SynchronousMachine.operatingMode is not consistent with the value of SynchronousMachine.type."]`

### ssh456n:RotatingMachine-pAndQcapabilityCurveP

**Path:** `rdf:type`  
**Name:** C:456:SSH:RotatingMachine:pAndQcapabilityCurve  
In cases where a ReactiveCapabilityCurve is associated, the RotatingMachine.p shall be less than or equal to the maximum active power value defined by the curve and it shall be greater than or equal to the minimum active power value defined by the curve. The RotatingMachine.q shall be less than or equal to the maximum reactive power value defined by the curve and it shall be greater than or equal to the minimum reactive power value defined by the curve.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value 
			WHERE {
        $this cim:RotatingMachine.p ?value .
        OPTIONAL {$this cim:SynchronousMachine.InitialReactiveCapabilityCurve ?rcc } .
               
        {
        SELECT $this (MAX(?xvalue) AS ?maxxvalue)  (MIN(?xvalue) AS ?minxvalue)
          WHERE {
            OPTIONAL {?rcc1 ^cim:SynchronousMachine.InitialReactiveCapabilityCurve $this } .
            ?rcc1 ^cim:CurveData.Curve ?curvedata .
            ?curvedata rdf:type ?cdtype .
            ?curvedata cim:CurveData.xvalue ?xvalue .
            FILTER (bound(?rcc1) && ?cdtype=cim:CurveData ) .
          }
          GROUP BY $this ?cdtype
        }

        FILTER ( bound(?rcc) && !(-?value>=?minxvalue && -?value<=?maxxvalue)).
			}
```
  - Messages: `["The active power is not within the limits defined by the ReactiveCapabilityCurve."]`

### ssh456n:RotatingMachine-pAndQcapabilityCurveQ

**Path:** `rdf:type`  
**Name:** C:456:SSH:RotatingMachine:pAndQcapabilityCurve  
In cases where a ReactiveCapabilityCurve is associated, the RotatingMachine.p shall be less than or equal to the maximum active power value defined by the curve and it shall be greater than or equal to the minimum active power value defined by the curve. The RotatingMachine.q shall be less than or equal to the maximum reactive power value defined by the curve and it shall be greater than or equal to the minimum reactive power value defined by the curve.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

			SELECT  $this ?value 
			WHERE {
        $this cim:RotatingMachine.q ?value .
        OPTIONAL {$this cim:SynchronousMachine.InitialReactiveCapabilityCurve ?rcc } .
               
        {
        SELECT $this (MAX(?y2value) AS ?my2value)  (MIN(?y1value) AS ?my1value)
          WHERE {
            OPTIONAL {?rcc1 ^cim:SynchronousMachine.InitialReactiveCapabilityCurve $this } .
            ?rcc1 ^cim:CurveData.Curve ?curvedata .
            ?curvedata rdf:type ?cdtype .
            ?curvedata cim:CurveData.y1value ?y1value .
            ?curvedata cim:CurveData.y2value ?y2value .
            FILTER (bound(?rcc1) && ?cdtype=cim:CurveData ) .
          }
          GROUP BY $this ?cdtype
        }

        FILTER ( bound(?rcc) && !(-?value>=?my1value && -?value<=?my2value)).
			}
```
  - Messages: `["The reactive power is not within the limits defined by the ReactiveCapabilityCurve."]`

## ssh456n:TapChanger

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:PhaseTapChangerTabular
- targetClass: cim:RatioTapChanger
- targetClass: cim:PhaseTapChangerLinear
- targetClass: cim:PhaseTapChangerSymmetrical
- targetClass: cim:PhaseTapChangerAsymmetrical

**Nested Properties:**

### ssh456n:TapChanger.step-value

**Path:** `cim:TapChanger.step`  
**Name:** C:456:SSH:TapChanger.step:value  
In cases where RegulatingControl.discrete is true and RegulatingControl.enabled is true, TapChanger.step shall be integer. 

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
        #OPTIONAL {$this cim:TapChanger.TapChangerControl ?contr}.
        #?contr cim:RegulatingControl.discrete ?discrete . 
        #?contr cim:RegulatingControl.enabled ?enabled .
        $this cim:TapChanger.TapChangerControl ?contr.
        ?contr cim:RegulatingControl.discrete true . 
        ?contr cim:RegulatingControl.enabled true .
        #FILTER (STRENDS(str(?value), ".") && !REGEX(STRAFTER(str(?value), "."), "^[0]$", "i")  && bound(?contr) && ?discrete=true && ?enabled=true) .  
        FILTER (STRENDS(str(?value), ".") && !REGEX(STRAFTER(str(?value), "."), "^[0]$", "i")) .         
			}
```
  - Messages: `["The value is not integer for an active discrete regulating control."]`

