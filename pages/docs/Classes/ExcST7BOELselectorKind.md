# ExcST7BOELselectorKind (Enumeration)

Types of connections for the OEL input used for static excitation systems type 7B.

## Values

| Label | Comment |
|-------|---------|
| noOELinput | No OEL input is used. Corresponds to OELin not = 1 and not = 2 and not = 3 on the ExcST7B diagram. Original ExcST7B model would have called this OELin = 0. |
| addVref | The signal is added to Vref. Corresponds to OELin = 1 on the ExcST7B diagram. |
| inputLVgate | The signal is connected into the input LVGate. Corresponds to OELin = 2 on the ExcST7B diagram. |
| outputLVgate | The signal is connected into the output LVGate. Corresponds to OELin = 3 on the ExcST7B diagram. |

