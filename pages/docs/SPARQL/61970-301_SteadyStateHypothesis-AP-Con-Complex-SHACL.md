# 61970-301_SteadyStateHypothesis-AP-Con-Complex-SHACL

## ssh:ActivePowerLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ActivePowerLimit

## ssh:ApparentPowerLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ApparentPowerLimit

## ssh:BatteryUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:BatteryUnit

## ssh:ControlArea

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ControlArea

## ssh:CsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CsConverter

**Nested Properties:**

### ssh:CsConverter.maxAlpha-valueRangeTypical

**Path:** `cim:CsConverter.maxAlpha`  
The attributes minAlpha and maxAlpha define the range of firing angles for rectifier operation between which no discrete tap changer action takes place. The range is typically 10-18 degrees.

**Severity:** sh:Warning

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Warning)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this cim:CsConverter.operatingMode cim:CsOperatingModeKind.rectifier .
        $this $PATH ?value .
        FILTER (?value>18) .        
			}
```
  - Messages: `["The value is greater than 18."]`

### ssh:CsConverter.maxGamma-valueRangeTypical

**Path:** `cim:CsConverter.maxGamma`  
The attributes minGamma and maxGamma define the range of extinction angles for inverter operation between which no discrete tap changer action takes place. The range is typically 17-20 degrees.

**Severity:** sh:Warning

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Warning)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this cim:CsConverter.operatingMode cim:CsOperatingModeKind.inverter .
        $this $PATH ?value .
        FILTER (?value>20) .        
			}
```
  - Messages: `["The value is greater than 20."]`

### ssh:CsConverter.minAlpha-valueRangeTypical

**Path:** `cim:CsConverter.minAlpha`  
The attributes minAlpha and maxAlpha define the range of firing angles for rectifier operation between which no discrete tap changer action takes place. The range is typically 10-18 degrees.

**Severity:** sh:Warning

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Warning)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this cim:CsConverter.operatingMode cim:CsOperatingModeKind.rectifier .
        $this $PATH ?value .
        OPTIONAL {$this cim:CsConverter.maxAlpha ?maxalpha} .
        FILTER (?value<10 || ?value>?maxalpha) .        
			}
```
  - Messages: `["The value is less than 10 or greater than CsConverter.maxAlpha"]`

### ssh:CsConverter.minGamma-valueRangeTypical

**Path:** `cim:CsConverter.minGamma`  
The attributes minGamma and maxGamma define the range of extinction angles for inverter operation between which no discrete tap changer action takes place. The range is typically 17-20 degrees.

**Severity:** sh:Warning

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Warning)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this cim:CsConverter.operatingMode cim:CsOperatingModeKind.inverter .
        $this $PATH ?value .
        OPTIONAL {$this cim:CsConverter.maxGamma ?maxgamma} .
        FILTER (?value<17 || ?value>?maxgamma) .        
			}
```
  - Messages: `["The value is less than 17 or greater than CsConverter.maxGamma"]`

### ssh:CsConverter.pPccControl-targetValuePpcc

**Path:** `cim:CsConverter.pPccControl`  
Target is provided by ACDCConverter.targetPpcc.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        OPTIONAL {$this cim:ACDCConverter.targetPpcc ?targetppcc}.
        FILTER (!bound(?targetppcc) && ?value=cim:CsPpccControlKind.activePower) .        
			}
```
  - Messages: `["ACDCConverter.targetPpcc is not provided for a converter with CsPpccControlKind.activePower."]`

### ssh:CsConverter.pPccControl-targetValueUdc

**Path:** `cim:CsConverter.pPccControl`  
Control is DC voltage  with target value provided by ACDCConverter.targetUdc.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        OPTIONAL {$this cim:ACDCConverter.targetUdc ?targetudc}.
        FILTER (!bound(?targetudc) && ?value=cim:CsPpccControlKind.dcVoltage) .        
			}
```
  - Messages: `["ACDCConverter.targetUdc is not provided for a converter with CsPpccControlKind.dcVoltage."]`

### ssh:CsConverter.pPccControl-targetValueIdc

**Path:** `cim:CsConverter.pPccControl`  
Control is DC current  with target value provided by CsConverter.targetIdc.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        OPTIONAL {$this cim:CsConverter.targetIdc ?targetidc}.
        FILTER (!bound(?targetidc) && ?value=cim:CsPpccControlKind.dcCurrent) .        
			}
```
  - Messages: `["CsConverter.targetIdc is not provided for a converter with CsPpccControlKind.dcCurrent."]`

## ssh:CurrentLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:CurrentLimit

## ssh:EnergySource

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EnergySource

**Nested Properties:**

### ssh:EnergySource.activePower-consumer

**Path:** `cim:EnergySource.activePower`  
Load sign convention is used, i.e. positive sign means flow out from a node.

**Severity:** sh:Warning

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Warning)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        FILTER (?value>0) .        
			}
```
  - Messages: `["EnergySource that is a consumer."]`

## ssh:EquivalentInjection

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EquivalentInjection

## ssh:GeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:GeneratingUnit

## ssh:HydroGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:HydroGeneratingUnit

## ssh:LinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:LinearShuntCompensator

## ssh:NonlinearShuntCompensator

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NonlinearShuntCompensator

## ssh:NuclearGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NuclearGeneratingUnit

## ssh:RegulatingControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:RegulatingControl

**Nested Properties:**

### ssh:RegulatingControl.targetDeadband-applicability

**Path:** `cim:RegulatingControl.discrete`  
This is a deadband used with discrete control to avoid excessive update of controls like tap changers and shunt compensator banks while regulating.…If RegulatingControl.discrete is set to false, the RegulatingControl.targetDeadband is to be ignored.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        OPTIONAL {$this cim:RegulatingControl.targetDeadband ?targetdeadband}.
        FILTER ((bound(?targetdeadband) && ?value=false) || (!bound(?targetdeadband) && ?value=true)) .        
			}
```
  - Messages: `["Either RegulatingControl.targetDeadband is provided for a continuous control or it is not provided for a discrete control."]`

## ssh:SolarGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:SolarGeneratingUnit

## ssh:TapChangerControl

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:TapChangerControl

**Nested Properties:**

### ssh:RegulatingControl.targetDeadband-applicability

**Path:** `cim:RegulatingControl.discrete`  
This is a deadband used with discrete control to avoid excessive update of controls like tap changers and shunt compensator banks while regulating.…If RegulatingControl.discrete is set to false, the RegulatingControl.targetDeadband is to be ignored.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        OPTIONAL {$this cim:RegulatingControl.targetDeadband ?targetdeadband}.
        FILTER ((bound(?targetdeadband) && ?value=false) || (!bound(?targetdeadband) && ?value=true)) .        
			}
```
  - Messages: `["Either RegulatingControl.targetDeadband is provided for a continuous control or it is not provided for a discrete control."]`

## ssh:ThermalGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ThermalGeneratingUnit

## ssh:VoltageLimit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VoltageLimit

## ssh:VsConverter

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:VsConverter

**Nested Properties:**

### ssh:VsConverter.pPccControl-targetValuepPccAndUdcDroopWithCompensation

**Path:** `cim:VsConverter.pPccControl`  
Targets are provided by ACDCConverter.targetPpcc, ACDCConverter.targetUdc, VsConverter.droop and VsConverter.droopCompensation.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        OPTIONAL {$this cim:ACDCConverter.targetPpcc ?targetppcc}.
        OPTIONAL {$this cim:ACDCConverter.targetUdc ?targetudc}.
        OPTIONAL {$this cim:VsConverter.droop ?droop}.
        OPTIONAL {$this cim:VsConverter.droopCompensation ?droopcompensation}.
        FILTER ((!bound(?targetppcc) || !bound(?targetudc) || !bound(?droop) || !bound(?droopcompensation)) && ?value=cim:VsPpccControlKind.pPccAndUdcDroopWithCompensation) .        
			}
```
  - Messages: `["One or all among ACDCConverter.targetPpcc, ACDCConverter.targetUdc, VsConverter.droop and VsConverter.droopCompensation are not provided for a converter with VsPpccControlKind.pPccAndUdcDroopWithCompensation."]`

### ssh:VsConverter.pPccControl-targetValuephasePcc

**Path:** `cim:VsConverter.pPccControl`  
Control is phase at point of common coupling. Target is provided by VsConverter.targetPhasePcc.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        OPTIONAL {$this cim:VsConverter.targetPhasePcc ?targetphasepcc}.
        FILTER (!bound(?targetphasepcc) && ?value=cim:VsPpccControlKind.phasePcc) .        
			}
```
  - Messages: `["VsConverter.targetPhasePcc is not provided for a converter with VsPpccControlKind.phasePcc."]`

### ssh:VsConverter.pPccControl-targetValuePpcc

**Path:** `cim:VsConverter.pPccControl`  
Control is real power at point of common coupling. The target value is provided by ACDCConverter.targetPpcc.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        OPTIONAL {$this cim:ACDCConverter.targetPpcc ?targetppcc}.
        FILTER (!bound(?targetppcc) && ?value=cim:VsPpccControlKind.pPcc) .        
			}
```
  - Messages: `["ACDCConverter.targetPpcc is not provided for a converter with VsPpccControlKind.pPcc."]`

### ssh:VsConverter.pPccControl-targetValuepPccAndUdcDroop

**Path:** `cim:VsConverter.pPccControl`  
Target values are provided by ACDCConverter.targetPpcc, ACDCConverter.targetUdc and VsConverter.droop.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        OPTIONAL {$this cim:ACDCConverter.targetPpcc ?targetppcc}.
        OPTIONAL {$this cim:ACDCConverter.targetUdc ?targetudc}.
        OPTIONAL {$this cim:VsConverter.droop ?droop}.
        FILTER ((!bound(?targetppcc) || !bound(?targetudc) || !bound(?droop)) && ?value=cim:VsPpccControlKind.pPccAndUdcDroop) .        
			}
```
  - Messages: `["One or all among ACDCConverter.targetPpcc, ACDCConverter.targetUdc and VsConverter.droop are not provided for a converter with VsPpccControlKind.pPccAndUdcDroop."]`

### ssh:VsConverter.pPccControl-targetValuepPccAndUdcDroopPilot

**Path:** `cim:VsConverter.pPccControl`  
Targets are provided by ACDCConverter.targetPpcc, ACDCConverter.targetUdc and  VsConverter.droop.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        OPTIONAL {$this cim:ACDCConverter.targetPpcc ?targetppcc}.
        OPTIONAL {$this cim:ACDCConverter.targetUdc ?targetudc}.
        OPTIONAL {$this cim:VsConverter.droop ?droop}.
        FILTER ((!bound(?targetppcc) || !bound(?targetudc) || !bound(?droop)) && ?value=cim:VsPpccControlKind.pPccAndUdcDroopPilot) .        
			}
```
  - Messages: `["One or all among ACDCConverter.targetPpcc, ACDCConverter.targetUdc and  VsConverter.droop are not provided for a converter with VsPpccControlKind.pPccAndUdcDroopPilot."]`

### ssh:VsConverter.pPccControl-targetValueUdc

**Path:** `cim:VsConverter.pPccControl`  
Control is DC voltage  with target value provided by ACDCConverter.targetUdc.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        OPTIONAL {$this cim:ACDCConverter.targetUdc ?targetudc}.
        FILTER (!bound(?targetudc) && ?value=cim:VsPpccControlKind.udc) .        
			}
```
  - Messages: `["ACDCConverter.targetUdc is not provided for a converter with VsPpccControlKind.udc."]`

### ssh:VsConverter.qPccControl-targetValuereactivePcc

**Path:** `cim:VsConverter.qPccControl`  
Control is reactive power at point of common coupling. Target is provided by VsConverter.targetQpcc.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        OPTIONAL {$this cim:VsConverter.targetQpcc ?targetqpcc}.
        FILTER (!bound(?targetqpcc) && ?value=cim:VsQpccControlKind.reactivePcc) .        
			}
```
  - Messages: `["VsConverter.targetQpcc is not provided for a converter with VsQpccControlKind.reactivePcc."]`

### ssh:VsConverter.qPccControl-targetValuepulseWidthModulation

**Path:** `cim:VsConverter.qPccControl`  
No explicit control. Pulse-modulation factor is directly set in magnitude (VsConverter.targetPWMfactor) and phase (VsConverter.targetPhasePcc).

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        OPTIONAL {$this cim:VsConverter.targetPWMfactor ?targetpwmfactor}.
        OPTIONAL {$this cim:VsConverter.targetPhasePcc ?targetphasepcc}.
        FILTER ((!bound(?targetpwmfactor) || !bound(?targetphasepcc)) && ?value=cim:VsQpccControlKind.pulseWidthModulation) .        
			}
```
  - Messages: `["VsConverter.targetPWMfactor and/or VsConverter.targetPhasePcc are not provided for a converter with VsQpccControlKind.pulseWidthModulation."]`

### ssh:VsConverter.qPccControl-targetValuevoltagePcc

**Path:** `cim:VsConverter.qPccControl`  
Control is voltage at point of common coupling. Target is provided by VsConverter.targetUpcc.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        OPTIONAL {$this cim:VsConverter.targetUpcc ?targetupcc}.
        FILTER (!bound(?targetupcc) && ?value=cim:VsQpccControlKind.voltagePcc) .        
			}
```
  - Messages: `["VsConverter.targetUpcc is not provided for a converter with VsQpccControlKind.voltagePcc."]`

### ssh:VsConverter.qPccControl-targetValuepowerFactorPcc

**Path:** `cim:VsConverter.qPccControl`  
Control is power factor at point of common coupling. Target is provided by VsConverter.targetPowerFactorPcc.

**Severity:** sh:Violation

**Constraints:**

- **sh:SPARQLConstraintComponent** (Severity: sh:Violation)

```sparql
PREFIX cim: <http://iec.ch/TC57/CIM100#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX eu: <http://iec.ch/TC57/CIM100-European#>

			SELECT  $this ?value
			WHERE {
        $this $PATH ?value .
        OPTIONAL {$this cim:VsConverter.targetPowerFactorPcc ?targetpowerfactorpcc}.
        FILTER (!bound(?targetpowerfactorpcc) && ?value=cim:VsQpccControlKind.powerFactorPcc) .        
			}
```
  - Messages: `["VsConverter.targetPowerFactorPcc is not provided for a converter with VsQpccControlKind.powerFactorPcc."]`

## ssh:WindGeneratingUnit

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:WindGeneratingUnit

