# 61970-456_SteadyStateHypothesis-AP-Con-Complex-SHACL

## ssh456c:ConformLoad

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:ConformLoad

## ssh456c:EnergyConsumer

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:EnergyConsumer

## ssh456c:EnergySource-EnergySourcePQ

**Name:** C:456:SSH:EnergySource:EnergySourcePQ  
The attributes voltageAngle and voltageMagnitude shall not be used when the EnergySource is representing a constant active and reactive power injection (PQ injection), i.e. they shall only be used when the EnergySource is modelling a voltage source.

**Severity:** sh:Warning

**Messages:**
- "EnergySource modelled as voltage source (attributes voltageAngle and voltageMagnitude are used). Please assess depending on the use case."

**Targets:**
- targetClass: cim:EnergySource

## ssh456c:NonConformLoad

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:NonConformLoad

## ssh456c:StationSupply

**Severity:** sh:Violation

**Targets:**
- targetClass: cim:StationSupply

