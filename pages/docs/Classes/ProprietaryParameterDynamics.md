# ProprietaryParameterDynamics

Supports definition of one or more parameters of several different datatypes for use by proprietary user-defined models. This class does not inherit from IdentifiedObject since it is not intended that a single instance of it be referenced by more than one proprietary user-defined model instance.

## Attributes

| Label | Type | Multiplicity | Comment |
|-------|------|--------------|---------|
| AsynchronousMachineUserDefined | [AsynchronousMachineUserDefined](AsynchronousMachineUserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| CSCUserDefined | [CSCUserDefined](CSCUserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| DiscontinuousExcitationControlUserDefined | [DiscontinuousExcitationControlUserDefined](DiscontinuousExcitationControlUserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| ExcitationSystemUserDefined | [ExcitationSystemUserDefined](ExcitationSystemUserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| LoadUserDefined | [LoadUserDefined](LoadUserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| MechanicalLoadUserDefined | [MechanicalLoadUserDefined](MechanicalLoadUserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| OverexcitationLimiterUserDefined | [OverexcitationLimiterUserDefined](OverexcitationLimiterUserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| PFVArControllerType1UserDefined | [PFVArControllerType1UserDefined](PFVArControllerType1UserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| PFVArControllerType2UserDefined | [PFVArControllerType2UserDefined](PFVArControllerType2UserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| PowerSystemStabilizerUserDefined | [PowerSystemStabilizerUserDefined](PowerSystemStabilizerUserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| SVCUserDefined | [SVCUserDefined](SVCUserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| SynchronousMachineUserDefined | [SynchronousMachineUserDefined](SynchronousMachineUserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| TurbineGovernorUserDefined | [TurbineGovernorUserDefined](TurbineGovernorUserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| TurbineLoadControllerUserDefined | [TurbineLoadControllerUserDefined](TurbineLoadControllerUserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| UnderexcitationLimiterUserDefined | [UnderexcitationLimiterUserDefined](UnderexcitationLimiterUserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| VSCUserDefined | [VSCUserDefined](VSCUserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| VoltageAdjusterUserDefined | [VoltageAdjusterUserDefined](VoltageAdjusterUserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| VoltageCompensatorUserDefined | [VoltageCompensatorUserDefined](VoltageCompensatorUserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| WindPlantUserDefined | [WindPlantUserDefined](WindPlantUserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| WindType1or2UserDefined | [WindType1or2UserDefined](WindType1or2UserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| WindType3or4UserDefined | [WindType3or4UserDefined](WindType3or4UserDefined.md) | 0..1 | Proprietary user-defined model with which this parameter is associated. |
| booleanParameterValue | Boolean | 0..1 | Boolean parameter value. If this attribute is populated, integerParameterValue and floatParameterValue will not be. |
| floatParameterValue | Float | 0..1 | Floating point parameter value. If this attribute is populated, booleanParameterValue and integerParameterValue will not be. |
| integerParameterValue | Integer | 0..1 | Integer parameter value. If this attribute is populated, booleanParameterValue and floatParameterValue will not be. |
| parameterNumber | Integer | 1..1 | Sequence number of the parameter among the set of parameters associated with the related proprietary user-defined model. |

