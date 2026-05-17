# WindLookupTableFunctionKind (Enumeration)

Function of the lookup table.

## Values

| Label | Comment |
|-------|---------|
| prr | Power versus speed change (negative slip) lookup table (prr(deltaomega)). It is used for the rotor resistance control model, IEC 61400-27-1:2015, 5.6.5.3. |
| omegap | Power vs. speed lookup table (omega(p)). It is used for the P control model type 3, IEC 61400-27-1:2015, 5.6.5.4. |
| ipmax | Lookup table for voltage dependency of active current limits (ipmax(uWT)). It is used for the current limitation model, IEC 61400-27-1:2015, 5.6.5.8. |
| iqmax | Lookup table for voltage dependency of reactive current limits (iqmax(uWT)). It is used for the current limitation model, IEC 61400-27-1:2015, 5.6.5.8. |
| pwp | Power vs. frequency lookup table (pWPbias(f)). It is used for the wind power plant frequency and active power control model, IEC 61400-27-1:2015, Annex D. |
| tcwdu | Crowbar duration versus voltage variation look-up table (TCW(du)). It is a case-dependent parameter. It is used for the type 3B generator set model, IEC 61400-27-1:2015, 5.6.3.3. |
| tduwt | Lookup table to determine the duration of the power reduction after a voltage dip, depending on the size of the voltage dip (Td(uWT)). It is a type-dependent parameter. It is used for the pitch control power model, IEC 61400-27-1:2015, 5.6.5.1. |
| qmaxp | Lookup table for active power dependency of reactive power maximum limit (qmaxp(p)). It is used for the QP and QU limitation model, IEC 61400-27-1:2015, 5.6.5.10. |
| qminp | Lookup table for active power dependency of reactive power minimum limit (qminp(p)). It is used for the QP and QU limitation model, IEC 61400-27-1:2015, 5.6.5.10. |
| qmaxu | Lookup table for voltage dependency of reactive power maximum limit (qmaxu(p)). It is used for the QP and QU limitation model, IEC 61400-27-1:2015, 5.6.5.10. |
| qminu | Lookup table for voltage dependency of reactive power minimum limit (qminu(p)). It is used for the QP and QU limitation model, IEC 61400-27-1:2015, 5.6.5.10. |
| tuover | Disconnection time versus over-voltage lookup table (Tuover(uWT)). It is used for the grid protection model, IEC 61400-27-1:2015, 5.6.6. |
| tuunder | Disconnection time versus under-voltage lookup table (Tuunder(uWT)). It is used for the grid protection model, IEC 61400-27-1:2015, 5.6.6. |
| tfover | Disconnection time versus over-frequency lookup table (Tfover(fWT)). It is used for the grid protection model, IEC 61400-27-1:2015, 5.6.6. |
| tfunder | Disconnection time versus under-frequency lookup table (Tfunder(fWT)). It is used for the grid protection model, IEC 61400-27-1:2015, 5.6.6. |
| qwp | Look up table for the UQ static mode (qWP(uerr)). It is used for the voltage and reactive power control model, IEC 61400-27-1:2015, Annex D. |

