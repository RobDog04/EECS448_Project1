# Battleship_Ship
## TODO: Fix second finger touch rotation 
- Name:  EdGraphNode_Comment_0 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call:K2_SetActorRotation          Name: K2Node_CallFunction_29       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:K2_GetActorRotation          Name: K2Node_CallFunction_30       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:Add_FloatFloat               Name: K2Node_CommutativeAssociativeBinaryOperator_2 Class:/Script/BlueprintGraph.K2Node_CommutativeAssociativeBinaryOperator
    - Call:PrintString                  Name: K2Node_CallFunction_61       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_IfThenElse_5          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_7         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_InputAction_0         Class:/Script/BlueprintGraph.K2Node_InputAction
    - Name: K2Node_InputKey_0            Class:/Script/BlueprintGraph.K2Node_InputKey

## Cursor/Touch/Controller Click Event Handler 
- Name:  EdGraphNode_Comment_1 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
    - EVENT ComponentOnClickedSignature__DelegateSignature
    - EVENT ComponentOnInputTouchBeginSignature__DelegateSignature
    - EVENT ComponentOnReleasedSignature__DelegateSignature
    - EVENT ComponentOnInputTouchEndSignature__DelegateSignature
  - Function Calls
    - Call:GetPlayerController          Name: K2Node_CallFunction_10       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:EqualEqual_ByteByte          Name: K2Node_CallFunction_28       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:EqualEqual_ByteByte          Name: K2Node_CallFunction_27       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_1         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_CustomEvent_0         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_IfThenElse_3          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_4          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_14         Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_14        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_13         Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_15         Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_16         Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_17         Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_18         Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_18        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_24         Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_25         Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_26         Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_27         Class:/Script/BlueprintGraph.K2Node_IfThenElse

## Cursor over ship capsule (Grabhand Icon) 
- Name:  EdGraphNode_Comment_4 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call:GetPlayerController          Name: K2Node_CallFunction_11       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_IfThenElse_1          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableSet_1         Class:/Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_2         Class:/Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_2         Class:/Script/BlueprintGraph.K2Node_VariableGet

## Reset Actor Hit Location 
- Name:  EdGraphNode_Comment_5 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call:GetPlayerController          Name: K2Node_CallFunction_1        Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:GetHitResultUnderCursorByChannel Name: K2Node_CallFunction_2        Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:BreakHitResult               Name: K2Node_CallFunction_3        Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:K2_GetActorLocation          Name: K2Node_CallFunction_4        Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:MakeVector                   Name: K2Node_CallFunction_7        Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:K2_SetActorLocation          Name: K2Node_CallFunction_8        Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_VariableGet_0         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_0          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_MacroInstance_0       Class:/Script/BlueprintGraph.K2Node_MacroInstance

## Cursor Selection Handler 
- Name:  EdGraphNode_Comment_6 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call:GetTransform                 Name: K2Node_CallFunction_36       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:K2_SetActorTransform         Name: K2Node_CallFunction_37       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:GetOverlappingActors         Name: K2Node_CallFunction_12       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:UnHighlight                  Name: K2Node_CallFunction_13       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:GetOverlappingActors         Name: K2Node_CallFunction_55       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:UnHighlight                  Name: K2Node_CallFunction_58       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_VariableSet_5         Class:/Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_4         Class:/Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_6         Class:/Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_IfThenElse_6          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_8         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_1         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_MacroInstance_1       Class:/Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_DynamicCast_0         Class:/Script/BlueprintGraph.K2Node_DynamicCast
    - Name: K2Node_VariableSet_15        Class:/Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_MacroInstance_5       Class:/Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_Knot_4                Class:/Script/BlueprintGraph.K2Node_Knot
    - Name: K2Node_DynamicCast_2         Class:/Script/BlueprintGraph.K2Node_DynamicCast
    - Name: K2Node_VariableSet_17        Class:/Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_16        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_21         Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableSet_16        Class:/Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_17        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_22         Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_MacroInstance_4       Class:/Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_DynamicCast_1         Class:/Script/BlueprintGraph.K2Node_DynamicCast
    - Name: K2Node_VariableGet_15        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_MacroInstance_6       Class:/Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_DynamicCast_3         Class:/Script/BlueprintGraph.K2Node_DynamicCast

## Handle Combat Hits 
- Name:  EdGraphNode_Comment_7 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call:EqualEqual_IntInt            Name: K2Node_CallFunction_14       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:KillShip                     Name: K2Node_CallFunction_15       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_2         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_IfThenElse_2          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_3         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_4         Class:/Script/BlueprintGraph.K2Node_VariableGet

## Detect When Ship Should Be Killed 
- Name:  EdGraphNode_Comment_8 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call:GetPlayerController          Name: K2Node_CallFunction_17       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:HandleShipDestroyed          Name: K2Node_CallFunction_18       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_3         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_DynamicCast_4         Class:/Script/BlueprintGraph.K2Node_DynamicCast
    - Name: K2Node_VariableGet_5         Class:/Script/BlueprintGraph.K2Node_VariableGet

## Kill Animation 
- Name:  EdGraphNode_Comment_9 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call:K2_SetRelativeRotation       Name: K2Node_CallFunction_22       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:Multiply_FloatFloat          Name: K2Node_CommutativeAssociativeBinaryOperator_1 Class:/Script/BlueprintGraph.K2Node_CommutativeAssociativeBinaryOperator
    - Call:K2_SetRelativeLocation       Name: K2Node_CallFunction_25       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:Multiply_FloatFloat          Name: K2Node_CommutativeAssociativeBinaryOperator_3 Class:/Script/BlueprintGraph.K2Node_CommutativeAssociativeBinaryOperator
    - Call:Multiply_IntFloat            Name: K2Node_CallFunction_32       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_Timeline_0            Class:/Script/BlueprintGraph.K2Node_Timeline
    - Name: K2Node_VariableGet_6         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_11        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_12        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_19        Class:/Script/BlueprintGraph.K2Node_VariableGet

## Detect Overlapping Blocks for Ship Placement 
- Name:  EdGraphNode_Comment_2 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
    - EVENT ComponentBeginOverlapSignature__DelegateSignature
    - EVENT ComponentEndOverlapSignature__DelegateSignature
  - Function Calls
    - Call:EqualEqual_IntInt            Name: K2Node_CallFunction_43       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:EqualEqual_IntInt            Name: K2Node_CallFunction_42       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:Add_IntInt                   Name: K2Node_CommutativeAssociativeBinaryOperator_4 Class:/Script/BlueprintGraph.K2Node_CommutativeAssociativeBinaryOperator
    - Call:Subtract_IntInt              Name: K2Node_CallFunction_46       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:GetObjectClass               Name: K2Node_CallFunction_53       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:EqualEqual_ClassClass        Name: K2Node_CallFunction_54       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:GetObjectClass               Name: K2Node_CallFunction_51       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:EqualEqual_ClassClass        Name: K2Node_CallFunction_52       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_IfThenElse_7          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_8          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_13        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_10        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_12         Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_11         Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableSet_11        Class:/Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_10        Class:/Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_13        Class:/Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_12        Class:/Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_9         Class:/Script/BlueprintGraph.K2Node_VariableGet

