# 61970-456_StateVariables-AP-Con-Complex-SolvedMAS-SHACL

## sv456sol:SvPowerFlow

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ConformLoad
- targetClass: cim:EquivalentInjection
- targetClass: cim:NonlinearShuntCompensator
- targetClass: cim:ExternalNetworkInjection
- targetClass: cim:PowerElectronicsConnection
- targetClass: cim:NonConformLoad
- targetClass: cim:EnergyConsumer
- targetClass: cim:LinearShuntCompensator
- targetClass: cim:StaticVarCompensator
- targetClass: cim:EnergySource
- targetClass: cim:SynchronousMachine
- targetClass: cim:AsynchronousMachine
- targetClass: cim:StationSupply

**Nested Properties:**

### sv456sol:SvPowerFlow-instance

**Path:** `rdf:type`  
As a minimum there shall be an instance of SvPowerFlow associated with the Terminal for all the following classes and their specialisation (subclass) that is part of an energized TopologicalIsland: RotatingMachine, EnergyConsumer, EquivalentInjection, ShuntCompensator, StaticVarCompensator, ExternalNetworkInjection, PowerElectronicsConnection and EnergySource. Additional instances of SvPowerFlow may optionally be available for other in service (SvStatus.inService=true) and energised equipment (equipment connected to a TopologicalNode part of the TopologicalIsland).

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>

			SELECT  $this ?value 
			WHERE {
        $this  ^cim:SvStatus.ConductingEquipment/cim:SvStatus.inService  true .
        $this ^cim:Terminal.ConductingEquipment/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.TopologicalNode/^cim:TopologicalIsland.TopologicalNodes ?topologicalisland .
        $this rdf:type ?value .
        #OPTIONAL {$this ^cim:Terminal.ConductingEquipment/cim:Terminal.ConnectivityNode/cim:ConnectivityNode.TopologicalNode/^cim:TopologicalIsland.TopologicalNodes ?topologicalisland }.
        #OPTIONAL {$this  ^cim:SvStatus.ConductingEquipment/cim:SvStatus.inService  ?svstatus} .
        OPTIONAL {$this ^cim:Terminal.ConductingEquipment/^cim:SvPowerFlow.Terminal ?svpowerflow }.
        #FILTER (bound(?topologicalisland) && bound(?svstatus) && ?svstatus=true && !bound(?svpowerflow)).
        FILTER (!bound(?svpowerflow)).
			}
```
  - Messages: `["SvPowerFlow is not instantiated for the required instances of energized (SvStatus.inService=true and the connected ToplogicalNode is part of the TopologicalIsland) equipment."]`

## sv456sol:SvPowerFlow-SynchronousMachine

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SynchronousMachine

**Nested Properties:**

### sv456sol:SvPowerFlow.p-synchronousMachine

**Path:** `rdf:type`  
The SvPowerFlow.p that is given by the steady state power flow solution for a SynchronousMachine shall normally be within the capability of the machine defined in the ReactiveCapabilityCurve or GeneratingUnit.maxOperatingP and GeneratingUnit.minOperatingP when ReactiveCapabilityCurve is not present. Active power can be outside the capability as part of start-up or shutdown of the generator. CIM cannot represent different operation mode so this constraint will only give a warning. Note that different data exchange processes can assign more restrictive severity depending on the business needs and power flow algorithm applied by the business process.

**Severity:** sh:Warning

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Warning)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>

			SELECT  $this ?value 
			WHERE {
        $this ^cim:Terminal.ConductingEquipment/^cim:SvPowerFlow.Terminal/cim:SvPowerFlow.p ?value .
        $this cim:RotatingMachine.GeneratingUnit ?gu .
        ?gu cim:GeneratingUnit.minOperatingP ?minp .
        ?gu cim:GeneratingUnit.maxOperatingP ?maxp .
        OPTIONAL {$this cim:SynchronousMachine.InitialReactiveCapabilityCurve ?rcc } .
               
        {
        SELECT $this (MAX(?xvalue) AS ?maxxvalue)  (MIN(?xvalue) AS ?minxvalue)
          WHERE {
            #OPTIONAL {?rcc1 ^cim:SynchronousMachine.InitialReactiveCapabilityCurve $this } .
            OPTIONAL {?rcc1 ^cim:SynchronousMachine.InitialReactiveCapabilityCurve $this .
                      ?rcc1 ^cim:CurveData.Curve ?curvedata .
                      ?curvedata rdf:type ?cdtype .
                      ?curvedata cim:CurveData.xvalue ?xvalue .
                      } .
            #?rcc1 ^cim:SynchronousMachine.InitialReactiveCapabilityCurve $this .
            #?rcc1 ^cim:CurveData.Curve ?curvedata .
            #?curvedata rdf:type ?cdtype .
            #?curvedata cim:CurveData.xvalue ?xvalue .
            #FILTER (bound(?rcc1) && ?cdtype=cim:CurveData ) .
          }
          GROUP BY $this ?cdtype
        }

        #FILTER ( (!bound(?rcc) && !(?value>=?minp && ?value<=?maxp)) || (bound(?rcc) && !(?value>=?minxvalue && ?value<=?maxxvalue))).
        FILTER ( (!bound(?rcc) && ((?value!=0 && (-?value<?minp || -?value>?maxp)) || (?value=0 && (?value<?minp || ?value>?maxp)))   ) || (bound(?rcc) && ((?value!=0 && (-?value<?minxvalue || -?value>?maxxvalue)) || (?value=0 && (?value<?minxvalue || ?value>?maxxvalue))))).
			}
```
  - Messages: `["The value is outside of the range defined by the ReactiveCapabilityCurve or [GeneratingUnit.minOperatingP, GeneratingUnit.maxOperatingP] when the curve is not present."]`

### sv456sol:SvPowerFlow.q-synchronousMachine

**Path:** `rdf:type`  
The SvPowerFlow.q that is given by the steady state power flow solution for a SynchronousMachine shall normally be within the capability of the machine defined in the ReactiveCapabilityCurve or SynchronousMachine.maxQ, SynchronousMachine.minQ when ReactiveCapabilityCurve is not present. Reactive power can be outside the capability if powerflow excludes reactive restriction. CIM cannot represent this so this contains will also give a warning. Note that different data exchange processes can assign more restrictive severity depending on the business needs and power flow algorithm applied by the business process.

**Severity:** sh:Warning

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Warning)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>

			SELECT  $this ?value 
			WHERE {
        $this ^cim:Terminal.ConductingEquipment/^cim:SvPowerFlow.Terminal/cim:SvPowerFlow.q ?value .
        OPTIONAL {$this cim:SynchronousMachine.minQ ?minq }.
        OPTIONAL {$this cim:SynchronousMachine.maxQ ?maxq }.
        OPTIONAL {$this cim:SynchronousMachine.InitialReactiveCapabilityCurve ?rcc } .
                   
        {
        SELECT $this (MAX(?y2value) AS ?my2value)  (MIN(?y1value) AS ?my1value)
          WHERE {
            #OPTIONAL {?rcc1 ^cim:SynchronousMachine.InitialReactiveCapabilityCurve $this } .
            OPTIONAL {?rcc1 ^cim:SynchronousMachine.InitialReactiveCapabilityCurve $this.
                      ?rcc1 ^cim:CurveData.Curve ?curvedata .
                      ?curvedata rdf:type ?cdtype .
                      ?curvedata cim:CurveData.y1value ?y1value .
                      ?curvedata cim:CurveData.y2value ?y2value .
                      }.
            #FILTER (bound(?rcc1) && ?cdtype=cim:CurveData ) .
          }
          GROUP BY $this ?cdtype
        }

        FILTER ( (!bound(?rcc) && bound(?minq) && bound(?maxq) && ((?value!=0 && (-?value<?minq || -?value>?maxq)) || (?value=0 && (?value<?minq || ?value>?maxq)))) || (bound(?rcc) && ((?value!=0 && (-?value<?my1value || -?value>?my2value)) || (?value=0 && (?value<?my1value || ?value>?my2value))))).
			}
```
  - Messages: `["The value is outside of the range defined by the ReactiveCapabilityCurve or [SynchronousMachine.minQ, SynchronousMachine.maxQ] when the curve is not present."]`

## sv456sol:SvShuntCompensatorSections

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SvShuntCompensatorSections

**Nested Properties:**

### sv456sol:SvShuntCompensatorSections.sections-value

**Path:** `cim:SvShuntCompensatorSections.sections`  
In cases where RegulatingControl.discrete is true and RegulatingControl.enabled is true, SvShuntCompensatorSections.sections shall be integer.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:SvShuntCompensatorSections.ShuntCompensator/cim:RegulatingCondEq.RegulatingControl ?contr .
        #$this cim:SvShuntCompensatorSections.ShuntCompensator ?shuntcomp .
        #OPTIONAL {?shuntcomp cim:RegulatingCondEq.RegulatingControl ?contr}.
        #?contr cim:RegulatingControl.discrete ?discrete . 
        #?contr cim:RegulatingControl.enabled ?enabled .
        ?contr cim:RegulatingControl.enabled true .
        ?contr cim:RegulatingControl.discrete true . 
        FILTER (STRENDS(str(?value), ".") && !REGEX(STRAFTER(str(?value), "."), "^[0]$", "i") ) . 
        #FILTER (STRENDS(str(?value), ".") && !REGEX(STRAFTER(str(?value), "."), "^[0]$", "i")  && bound(?contr) && ?discrete=true && ?enabled=true) .          
			}
```
  - Messages: `["The value is not integer for an active discrete regulating control."]`

## sv456sol:SvSwitch

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:Cut
- targetClass: cim:Switch
- targetClass: cim:GroundDisconnector
- targetClass: cim:Disconnector
- targetClass: cim:Fuse
- targetClass: cim:Jumper
- targetClass: cim:Breaker
- targetClass: cim:LoadBreakSwitch
- targetClass: cim:DisconnectingCircuitBreaker

**Nested Properties:**

### sv456sol:SvSwitch-instance

**Path:** `rdf:type`  
SvSwitch shall be exchanged for all switching devices. It is expected that in most cases the SvSwitch.open in SV instance data will be identical with Switch.open in SSH instance data. However, in cases where a regulating control is modifying the connection state of the controlled device a difference between SvSwitch.open and Switch.open can occur.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>

			SELECT  $this
			WHERE {
        OPTIONAL {$this ^cim:SvSwitch.Switch ?svswitch } .
        FILTER (!bound(?svswitch)) .        
			}
```
  - Messages: `["SvSwitch not instantiated."]`

## sv456sol:SvTapStep

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SvTapStep

**Nested Properties:**

### sv456sol:SvTapStep.position-value

**Path:** `cim:SvTapStep.position`  
In cases where RegulatingControl.discrete is true and RegulatingControl.enabled is true, SvTapStep.position shall be integer.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        $this cim:SvTapStep.TapChanger/cim:TapChanger.TapChangerControl ?contr .
        #$this cim:SvTapStep.TapChanger ?tapchanger .
        #OPTIONAL {?tapchanger cim:TapChanger.TapChangerControl ?contr}.
        ?contr cim:RegulatingControl.enabled true .
        ?contr cim:RegulatingControl.discrete true . 
        FILTER (STRENDS(str(?value), ".") && !REGEX(STRAFTER(str(?value), "."), "^[0]$", "i")) . 
        #?contr cim:RegulatingControl.discrete ?discrete . 
        #?contr cim:RegulatingControl.enabled ?enabled .
        #FILTER (STRENDS(str(?value), ".") && !REGEX(STRAFTER(str(?value), "."), "^[0]$", "i")  && bound(?contr) && ?discrete=true && ?enabled=true) .        
			}
```
  - Messages: `["The value is not integer for an active discrete regulating control."]`

## sv456sol:SvVoltage

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SvVoltage

**Nested Properties:**

### sv456sol:SvVoltage.v-limits

**Path:** `rdf:type`  
The SvVoltage.v shall be less than or equal to VoltageLimit.value associated with OperationalLimitType.limitType=highVoltage and greater than or equal to VoltageLimit.value associated with OperationalLimitType.limitType=lowVoltage.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>

			SELECT  $this ?value 
			WHERE {
        $this cim:SvVoltage.v ?value .
        $this cim:SvVoltage.ToplogicalNode/^cim:ConnectivityNode.TopologicalNode/^cim:Terminal.ConnectivityNode ?term .
        
        ?limith cim:OperationalLimit.OperationalLimitSet/cim:OperationalLimitSet.Terminal ?term .
        ?limitl cim:OperationalLimit.OperationalLimitSet/cim:OperationalLimitSet.Terminal ?term .
        ?limith cim:OperationalLimit.OperationalLimitType/cim:OperationalLimitType.direction cim:OperationalLimitDirectionKind.high .
        ?limitl cim:OperationalLimit.OperationalLimitType/cim:OperationalLimitType.direction cim:OperationalLimitDirectionKind.low .
        ?limith cim:VoltageLimit.value ?vhigh .
        ?limitl cim:VoltageLimit.value ?vlow .
        
        #OPTIONAL {?limith cim:OperationalLimit.OperationalLimitSet/cim:OperationalLimitSet.Terminal ?term} .
        #OPTIONAL {?limitl cim:OperationalLimit.OperationalLimitSet/cim:OperationalLimitSet.Terminal ?term} .
        ##OPTIONAL {?limith rdf:type ?limithtype} .
        ##OPTIONAL {?limitl rdf:type ?limitltype} .
        #OPTIONAL {?limith cim:OperationalLimit.OperationalLimitType/cim:OperationalLimitType.direction cim:OperationalLimitDirectionKind.high} .
        #OPTIONAL {?limitl cim:OperationalLimit.OperationalLimitType/cim:OperationalLimitType.direction cim:OperationalLimitDirectionKind.low} .
        #OPTIONAL {?limith cim:VoltageLimit.value ?vhigh} .
        #OPTIONAL {?limitl cim:VoltageLimit.value ?vlow} .
       
        FILTER ( ?value>?vhigh || ?value<?vlow).
        #FILTER ( bound(?vhigh) && bound(?vlow) && ?value<=?vhigh && ?value>=?vlow).
			}
```
  - Messages: `["The value is outside the defined limits."]`

### sv456sol:SvVoltage.v-absoluteLimit

**Path:** `rdf:type`  
SvVoltage.v shall be greater than 0.4 pu in cases where associated voltage limits are not defining different limit range.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>
PREFIX cim: <http://iec.ch/TC57/CIM100#>

			SELECT  $this ?value 
			WHERE {
        $this cim:SvVoltage.v ?value .
        $this cim:SvVoltage.ToplogicalNode/^cim:ConnectivityNode.TopologicalNode/^cim:Terminal.ConnectivityNode ?term .
        $this cim:SvVoltage.ToplogicalNode/cim:ToplogicalNode.BaseVoltage/cim:BaseVoltage.nominalVoltage ?nvoltage .
        #OPTIONAL {?limith cim:OperationalLimit.OperationalLimitSet/cim:OperationalLimitSet.Terminal ?term} .
        #OPTIONAL {?limitl cim:OperationalLimit.OperationalLimitSet/cim:OperationalLimitSet.Terminal ?term} .
        ##OPTIONAL {?limith rdf:type ?limithtype} .
        ##OPTIONAL {?limitl rdf:type ?limitltype} .
        #OPTIONAL {?limith cim:OperationalLimit.OperationalLimitType/cim:OperationalLimitType.direction cim:OperationalLimitDirectionKind.high} .
        #OPTIONAL {?limitl cim:OperationalLimit.OperationalLimitType/cim:OperationalLimitType.direction cim:OperationalLimitDirectionKind.low} .
        #OPTIONAL {?limith cim:VoltageLimit.value ?vhigh} .
        #OPTIONAL {?limitl cim:VoltageLimit.value ?vlow} .
        OPTIONAL {
                  ?limith cim:OperationalLimit.OperationalLimitSet/cim:OperationalLimitSet.Terminal ?term .
                  ?limitl cim:OperationalLimit.OperationalLimitSet/cim:OperationalLimitSet.Terminal ?term .
                  ?limith cim:OperationalLimit.OperationalLimitType/cim:OperationalLimitType.direction cim:OperationalLimitDirectionKind.high .
                  ?limitl cim:OperationalLimit.OperationalLimitType/cim:OperationalLimitType.direction cim:OperationalLimitDirectionKind.low .
                  ?limith cim:VoltageLimit.value ?vhigh .
                  ?limitl cim:VoltageLimit.value ?vlow .
                  }.
       

        FILTER ( !bound(?vhigh) && !bound(?vlow) && (?value/?nvoltage)<=0.4).
			}
```
  - Messages: `["The value is <=0.4 pu."]`

