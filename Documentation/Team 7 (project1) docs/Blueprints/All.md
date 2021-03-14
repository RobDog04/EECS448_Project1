# Battleship_MainGameMap
## Connect Player 2 to in-map camera (Client-Only) 
- Name:  EdGraphNode_Comment_0 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: SetViewTargetWithBlend       Name: K2Node_CallFunction_28       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_Literal_4             Class: /Script/BlueprintGraph.K2Node_Literal
    - Name: K2Node_CustomEvent_3         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_MacroInstance_5       Class: /Script/BlueprintGraph.K2Node_MacroInstance

## Confirm Valid/Legal Placement of Ships before allowing the game to progress 
- Name:  EdGraphNode_Comment_2 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: CheckShipPlacement           Name: K2Node_CallFunction_15       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetActorHiddenInGame         Name: K2Node_CallFunction_18       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: AnnounceReadyToPlay          Name: K2Node_CallFunction_57       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: DisplayInvalidShipPlacement  Name: K2Node_CallFunction_58       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_2         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_IfThenElse_0          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_Literal_1             Class: /Script/BlueprintGraph.K2Node_Literal
    - Name: K2Node_VariableGet_15        Class: /Script/BlueprintGraph.K2Node_VariableGet

## Adjust visible ships to match selected ship count 
- Name:  EdGraphNode_Comment_4 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: AdjustVisibleShipsToShipCount Name: K2Node_CallFunction_14       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetupClientCamera            Name: K2Node_CallFunction_29       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetActorHiddenInGame         Name: K2Node_CallFunction_17       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: DisplayConfirmShipPlacement  Name: K2Node_CallFunction_60       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_6         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_MacroInstance_4       Class: /Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_Literal_0             Class: /Script/BlueprintGraph.K2Node_Literal

## Determine if a Game Mode has been selected 
- Name:  EdGraphNode_Comment_9 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
    - EVENT ReceiveBeginPlay
  - Function Calls
    - Call: PopulateLevelVariables       Name: K2Node_CallFunction_40       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetupBindings                Name: K2Node_CallFunction_55       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: Delay                        Name: K2Node_CallFunction_65       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_IfThenElse_11         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_Knot_2                Class: /Script/BlueprintGraph.K2Node_Knot
    - Name: K2Node_Knot_3                Class: /Script/BlueprintGraph.K2Node_Knot

## Handle Game Attack Event 
- Name:  EdGraphNode_Comment_16 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: AttackBoardPosition          Name: K2Node_CallFunction_9        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: UpdatePlayer1TurnInGameState Name: K2Node_CallFunction_19       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: UpdatePlayer2TurnInGameState Name: K2Node_CallFunction_20       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: Delay                        Name: K2Node_CallFunction_31       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: Delay                        Name: K2Node_CallFunction_3        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: DisablePlayingBoard          Name: K2Node_CallFunction_33       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: DisablePlayingBoard          Name: K2Node_CallFunction_32       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: AttackBlock                  Name: K2Node_CallFunction_2        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: Delay                        Name: K2Node_CallFunction_35       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_16        Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_MacroInstance_14      Class: /Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_VariableGet_10        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_11        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_5          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_6          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_Knot_4                Class: /Script/BlueprintGraph.K2Node_Knot
    - Name: K2Node_Knot_5                Class: /Script/BlueprintGraph.K2Node_Knot
    - Name: K2Node_VariableGet_0         Class: /Script/BlueprintGraph.K2Node_VariableGet

## Handle Ship Hit Event 
- Name:  EdGraphNode_Comment_17 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: EqualEqual_IntInt            Name: K2Node_CallFunction_4        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: Activate                     Name: K2Node_CallFunction_45       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: SendShipHit                  Name: K2Node_CallFunction_52       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: EqualEqual_IntInt            Name: K2Node_CallFunction_43       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: IsValid                      Name: K2Node_CallFunction_6        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: GetOverlappingActors         Name: K2Node_CallFunction_8        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: Add_IntInt                   Name: K2Node_CommutativeAssociativeBinaryOperator_0 Class: /Script/BlueprintGraph.K2Node_CommutativeAssociativeBinaryOperator
    - Call: HandleCombatHit              Name: K2Node_CallFunction_10       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: Delay                        Name: K2Node_CallFunction_30       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_15        Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_MacroInstance_0       Class: /Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_VariableGet_8         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_9         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_3          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_4          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_12        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_MacroInstance_15      Class: /Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_VariableGet_2         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_7          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_14        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_MacroInstance_2       Class: /Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_VariableGet_1         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_13        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_3         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_8          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_GetArrayItem_0        Class: /Script/BlueprintGraph.K2Node_GetArrayItem
    - Name: K2Node_IfThenElse_9          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_DynamicCast_0         Class: /Script/BlueprintGraph.K2Node_DynamicCast
    - Name: K2Node_VariableGet_4         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_0         Class: /Script/BlueprintGraph.K2Node_VariableSet

## Handle Change Turns Event 
- Name:  EdGraphNode_Comment_1 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: DisablePlayingBoard          Name: K2Node_CallFunction_0        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: EnablePlayingBoard           Name: K2Node_CallFunction_1        Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_0         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_MacroInstance_1       Class: /Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_IfThenElse_1          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_2          Class: /Script/BlueprintGraph.K2Node_IfThenElse

## Handle Opponent Ship Sunk and Reset ShipSunk in GameState 
- Name:  EdGraphNode_Comment_3 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: SetActorHiddenInGame         Name: K2Node_CallFunction_13       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetActorHiddenInGame         Name: K2Node_CallFunction_16       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetActorHiddenInGame         Name: K2Node_CallFunction_21       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetActorHiddenInGame         Name: K2Node_CallFunction_22       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetActorHiddenInGame         Name: K2Node_CallFunction_23       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetActorHiddenInGame         Name: K2Node_CallFunction_12       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: ResetShipSunk                Name: K2Node_CallFunction_26       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_1         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_SwitchInteger_0       Class: /Script/BlueprintGraph.K2Node_SwitchInteger
    - Name: K2Node_Literal_2             Class: /Script/BlueprintGraph.K2Node_Literal
    - Name: K2Node_Literal_3             Class: /Script/BlueprintGraph.K2Node_Literal
    - Name: K2Node_Literal_5             Class: /Script/BlueprintGraph.K2Node_Literal
    - Name: K2Node_Literal_6             Class: /Script/BlueprintGraph.K2Node_Literal
    - Name: K2Node_Literal_7             Class: /Script/BlueprintGraph.K2Node_Literal
    - Name: K2Node_Literal_8             Class: /Script/BlueprintGraph.K2Node_Literal
    - Name: K2Node_VariableGet_5         Class: /Script/BlueprintGraph.K2Node_VariableGet

# Battleship_Ship
## TODO: Fix second finger touch rotation 
- Name:  EdGraphNode_Comment_0 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: K2_SetActorRotation          Name: K2Node_CallFunction_29       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: K2_GetActorRotation          Name: K2Node_CallFunction_30       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: Add_FloatFloat               Name: K2Node_CommutativeAssociativeBinaryOperator_2 Class: /Script/BlueprintGraph.K2Node_CommutativeAssociativeBinaryOperator
    - Call: PrintString                  Name: K2Node_CallFunction_61       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_IfThenElse_5          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_7         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_InputAction_0         Class: /Script/BlueprintGraph.K2Node_InputAction
    - Name: K2Node_InputKey_0            Class: /Script/BlueprintGraph.K2Node_InputKey

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
    - Call: GetPlayerController          Name: K2Node_CallFunction_10       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: EqualEqual_ByteByte          Name: K2Node_CallFunction_28       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: EqualEqual_ByteByte          Name: K2Node_CallFunction_27       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_1         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_CustomEvent_0         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_IfThenElse_3          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_4          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_14         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_14        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_13         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_15         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_16         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_17         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_18         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_18        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_24         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_25         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_26         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_27         Class: /Script/BlueprintGraph.K2Node_IfThenElse

## Cursor over ship capsule (Grabhand Icon) 
- Name:  EdGraphNode_Comment_4 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: GetPlayerController          Name: K2Node_CallFunction_11       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_IfThenElse_1          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableSet_1         Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_2         Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_2         Class: /Script/BlueprintGraph.K2Node_VariableGet

## Reset Actor Hit Location 
- Name:  EdGraphNode_Comment_5 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: GetPlayerController          Name: K2Node_CallFunction_1        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: GetHitResultUnderCursorByChannel Name: K2Node_CallFunction_2        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: BreakHitResult               Name: K2Node_CallFunction_3        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: K2_GetActorLocation          Name: K2Node_CallFunction_4        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: MakeVector                   Name: K2Node_CallFunction_7        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: K2_SetActorLocation          Name: K2Node_CallFunction_8        Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_VariableGet_0         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_0          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_MacroInstance_0       Class: /Script/BlueprintGraph.K2Node_MacroInstance

## Cursor Selection Handler 
- Name:  EdGraphNode_Comment_6 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: GetTransform                 Name: K2Node_CallFunction_36       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: K2_SetActorTransform         Name: K2Node_CallFunction_37       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: GetOverlappingActors         Name: K2Node_CallFunction_12       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: UnHighlight                  Name: K2Node_CallFunction_13       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: GetOverlappingActors         Name: K2Node_CallFunction_55       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: UnHighlight                  Name: K2Node_CallFunction_58       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_VariableSet_5         Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_4         Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_6         Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_IfThenElse_6          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_8         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_1         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_MacroInstance_1       Class: /Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_DynamicCast_0         Class: /Script/BlueprintGraph.K2Node_DynamicCast
    - Name: K2Node_VariableSet_15        Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_MacroInstance_5       Class: /Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_Knot_4                Class: /Script/BlueprintGraph.K2Node_Knot
    - Name: K2Node_DynamicCast_2         Class: /Script/BlueprintGraph.K2Node_DynamicCast
    - Name: K2Node_VariableSet_17        Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_16        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_21         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableSet_16        Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_17        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_22         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_MacroInstance_4       Class: /Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_DynamicCast_1         Class: /Script/BlueprintGraph.K2Node_DynamicCast
    - Name: K2Node_VariableGet_15        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_MacroInstance_6       Class: /Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_DynamicCast_3         Class: /Script/BlueprintGraph.K2Node_DynamicCast

## Handle Combat Hits 
- Name:  EdGraphNode_Comment_7 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: EqualEqual_IntInt            Name: K2Node_CallFunction_14       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: KillShip                     Name: K2Node_CallFunction_15       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_2         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_IfThenElse_2          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_3         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_4         Class: /Script/BlueprintGraph.K2Node_VariableGet

## Detect When Ship Should Be Killed 
- Name:  EdGraphNode_Comment_8 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: GetPlayerController          Name: K2Node_CallFunction_17       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: HandleShipDestroyed          Name: K2Node_CallFunction_18       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_3         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_DynamicCast_4         Class: /Script/BlueprintGraph.K2Node_DynamicCast
    - Name: K2Node_VariableGet_5         Class: /Script/BlueprintGraph.K2Node_VariableGet

## Kill Animation 
- Name:  EdGraphNode_Comment_9 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: K2_SetRelativeRotation       Name: K2Node_CallFunction_22       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: Multiply_FloatFloat          Name: K2Node_CommutativeAssociativeBinaryOperator_1 Class: /Script/BlueprintGraph.K2Node_CommutativeAssociativeBinaryOperator
    - Call: K2_SetRelativeLocation       Name: K2Node_CallFunction_25       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: Multiply_FloatFloat          Name: K2Node_CommutativeAssociativeBinaryOperator_3 Class: /Script/BlueprintGraph.K2Node_CommutativeAssociativeBinaryOperator
    - Call: Multiply_IntFloat            Name: K2Node_CallFunction_32       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_Timeline_0            Class: /Script/BlueprintGraph.K2Node_Timeline
    - Name: K2Node_VariableGet_6         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_11        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_12        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_19        Class: /Script/BlueprintGraph.K2Node_VariableGet

## Detect Overlapping Blocks for Ship Placement 
- Name:  EdGraphNode_Comment_2 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
    - EVENT ComponentBeginOverlapSignature__DelegateSignature
    - EVENT ComponentEndOverlapSignature__DelegateSignature
  - Function Calls
    - Call: EqualEqual_IntInt            Name: K2Node_CallFunction_43       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: EqualEqual_IntInt            Name: K2Node_CallFunction_42       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: Add_IntInt                   Name: K2Node_CommutativeAssociativeBinaryOperator_4 Class: /Script/BlueprintGraph.K2Node_CommutativeAssociativeBinaryOperator
    - Call: Subtract_IntInt              Name: K2Node_CallFunction_46       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: GetObjectClass               Name: K2Node_CallFunction_53       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: EqualEqual_ClassClass        Name: K2Node_CallFunction_54       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: GetObjectClass               Name: K2Node_CallFunction_51       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: EqualEqual_ClassClass        Name: K2Node_CallFunction_52       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_IfThenElse_7          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_8          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_13        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_10        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_12         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_11         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableSet_11        Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_10        Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_13        Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_12        Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_9         Class: /Script/BlueprintGraph.K2Node_VariableGet

# BattleshipBlock
## Handle block being clicked 
- Name:  EdGraphNode_Comment_8 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
    - EVENT ComponentOnClickedSignature__DelegateSignature
    - EVENT ReceiveActorOnInputTouchBegin
  - Function Calls
    - Call: SetMaterial                  Name: K2Node_CallFunction_9        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: GetPlayerController          Name: K2Node_CallFunction_4        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: AttackBlock                  Name: K2Node_CallFunction_5        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: Activate                     Name: K2Node_CallFunction_10       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: Delay                        Name: K2Node_CallFunction_6        Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_VariableGet_727       Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_225        Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableSet_690       Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_3         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_CustomEvent_0         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableSet_1         Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_DynamicCast_0         Class: /Script/BlueprintGraph.K2Node_DynamicCast
    - Name: K2Node_VariableGet_0         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_1         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_4         Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_5         Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_2         Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_3         Class: /Script/BlueprintGraph.K2Node_VariableSet

## VR - Handles changing color of the tile player is looking at. 
- Name:  EdGraphNode_Comment_3 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: SetMaterial                  Name: K2Node_CallFunction_56       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetMaterial                  Name: K2Node_CallFunction_57       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_IfThenElse_30         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_54        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_31         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_55        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_56        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_0         Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_CustomEvent_1         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_IfThenElse_7          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_12         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_81        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_82        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_80        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_69        Class: /Script/BlueprintGraph.K2Node_VariableSet

## Inactive blocks turn white when hovered by mouse and back to blue if the mouse isn\'t hovering. 
- Name:  EdGraphNode_Comment_1 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
    - EVENT ComponentBeginCursorOverSignature__DelegateSignature
    - EVENT ComponentEndCursorOverSignature__DelegateSignature
  - Function Calls
    - Call: SetMaterial                  Name: K2Node_CallFunction_137      Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetMaterial                  Name: K2Node_CallFunction_37       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_IfThenElse_81         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_141       Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_82         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_142       Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_143       Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_47        Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_IfThenElse_20         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_36        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_21         Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_37        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_38        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_12        Class: /Script/BlueprintGraph.K2Node_VariableSet

## Handle Incoming Attack 
- Name:  EdGraphNode_Comment_9 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: SetMaterial                  Name: K2Node_CallFunction_25925    Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: Activate                     Name: K2Node_CallFunction_12       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: Activate                     Name: K2Node_CallFunction_11       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: GetPlayerController          Name: K2Node_CallFunction_13       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: SendShipHit                  Name: K2Node_CallFunction_14       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_2         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableGet_729       Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_18        Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_4         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_5         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_2          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_6         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_DynamicCast_1         Class: /Script/BlueprintGraph.K2Node_DynamicCast

## Handle Ship Overlaps 
- Name:  EdGraphNode_Comment_2 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
    - EVENT ComponentBeginOverlapSignature__DelegateSignature
    - EVENT ComponentEndOverlapSignature__DelegateSignature
  - Function Calls
    - Call: GetObjectClass               Name: K2Node_CallFunction_1        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: GetObjectClass               Name: K2Node_CallFunction_0        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: EqualEqual_ClassClass        Name: K2Node_CallFunction_3        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: EqualEqual_ClassClass        Name: K2Node_CallFunction_2        Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_IfThenElse_0          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_1          Class: /Script/BlueprintGraph.K2Node_IfThenElse

# BattleShipGameMode
## Begin of Gameplay 
- Name:  EdGraphNode_Comment_0 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
    - EVENT ReceiveBeginPlay
  - Function Calls
    - Call: ExecuteConsoleCommand        Name: K2Node_CallFunction_0        Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others

# BattleShipGameState
## Initialize Random First Turn for Game Play 
- Name:  EdGraphNode_Comment_1 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_0         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableSet_1         Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_0         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_0          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_1          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableSet_0         Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_3         Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_7         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_8         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_CallDelegate_2        Class: /Script/BlueprintGraph.K2Node_CallDelegate
    - Name: K2Node_VariableGet_14        Class: /Script/BlueprintGraph.K2Node_VariableGet

# BattleshipPlayerController
## Update Server (GameState) with Player 2 Connected (Run on Server Only) 
- Name:  EdGraphNode_Comment_11 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_0         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableSet_0         Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_16        Class: /Script/BlueprintGraph.K2Node_VariableGet

## Update Server (GameState) with Player 1 Connected (Run on Server Only) 
- Name:  EdGraphNode_Comment_12 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_1         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableSet_1         Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_3         Class: /Script/BlueprintGraph.K2Node_VariableGet

## Determine if the Player Has Selected a Game Mode (GameInstance) 
- Name:  EdGraphNode_Comment_13 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
    - EVENT ReceiveBeginPlay
  - Function Calls
    - Call: GetCurrentLevelName          Name: K2Node_CallFunction_12       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: EqualEqual_StrStr            Name: K2Node_CallFunction_13       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_Composite_0           Class: /Script/BlueprintGraph.K2Node_Composite
    - Name: K2Node_MacroInstance_0       Class: /Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_IfThenElse_0          Class: /Script/BlueprintGraph.K2Node_IfThenElse

## If Host Mode Selected Notify GameState of Player 1 Connected 
- Name:  EdGraphNode_Comment_14 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: UpdatePlayer1ConnectedInGameState Name: K2Node_CallFunction_4        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: DisplayWaitingForPlayerToConnect Name: K2Node_CallFunction_6        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetGameStateShipCount        Name: K2Node_CallFunction_7        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetupPlayer1Bindings         Name: K2Node_CallFunction_18       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CallDelegate_1        Class: /Script/BlueprintGraph.K2Node_CallDelegate

## If Join Mode Selected Notify GameState of Player 2 Connected 
- Name:  EdGraphNode_Comment_15 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: UpdatePlayer2ConnectedInGameState Name: K2Node_CallFunction_30       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetupPlayer2Bindings         Name: K2Node_CallFunction_19       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: DisplayConnectingToGameHost  Name: K2Node_CallFunction_20       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CallDelegate_0        Class: /Script/BlueprintGraph.K2Node_CallDelegate

## Update Server (GameState) with Player 1 Ready (Run on Server Only) 
- Name:  EdGraphNode_Comment_1 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_2         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableGet_6         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_4         Class: /Script/BlueprintGraph.K2Node_VariableSet

## Update Server (GameState) with Player 2 Ready (Run on Server Only) 
- Name:  EdGraphNode_Comment_2 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_3         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableGet_5         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_5         Class: /Script/BlueprintGraph.K2Node_VariableSet

## Update Server (GameState) with Block Currently under attack 
- Name:  EdGraphNode_Comment_5 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_4         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableGet_7         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_6         Class: /Script/BlueprintGraph.K2Node_VariableSet

## Update Server (GameState) with Player 1 Turn Status (Run on Server Only) 
- Name:  EdGraphNode_Comment_7 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_6         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableGet_10        Class: /Script/BlueprintGraph.K2Node_VariableGet

## Update Server (GameState) with Player 2 Turn Status (Run on Server Only) 
- Name:  EdGraphNode_Comment_8 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_5         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableGet_8         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_8         Class: /Script/BlueprintGraph.K2Node_VariableSet

## Update Server (GameState) with Ship Hit (Run on Server Only) 
- Name:  EdGraphNode_Comment_0 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_8         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableGet_9         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_9         Class: /Script/BlueprintGraph.K2Node_VariableSet

## Handle Win/Lose Conditions 
- Name:  EdGraphNode_Comment_3 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: DisplayWin                   Name: K2Node_CallFunction_1        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: DisplayLose                  Name: K2Node_CallFunction_3        Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_10        Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_IfThenElse_4          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_MacroInstance_2       Class: /Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_IfThenElse_1          Class: /Script/BlueprintGraph.K2Node_IfThenElse

## Set (GameState) Ship Count using Game Instance 
- Name:  EdGraphNode_Comment_4 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_12        Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableGet_13        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_14        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_15        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_10        Class: /Script/BlueprintGraph.K2Node_VariableSet

## If Game Mode Not Selected Yet 
- Name:  EdGraphNode_Comment_6 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: DisplayHostOrJoin            Name: K2Node_CallFunction_22       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others

## Setup Server Host Connection and Reopen Level in ?listen for Client connection state 
- Name:  EdGraphNode_Comment_9 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: OpenLevel                    Name: K2Node_CallFunction_46       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_13        Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_AsyncAction_0         Class: /Script/BlueprintGraph.K2Node_AsyncAction
    - Name: K2Node_VariableSet_11        Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_4         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_17        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_18        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_Self_1                Class: /Script/BlueprintGraph.K2Node_Self

## Connect to a Hosted LAN Server as a Client. Also display a \"Connecting to Host\" UI until connection established 
- Name:  EdGraphNode_Comment_10 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: DisplayConnectingToGameHost  Name: K2Node_CallFunction_23       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_14        Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_AsyncAction_2         Class: /Script/BlueprintGraph.K2Node_AsyncAction
    - Name: K2Node_GetArrayItem_0        Class: /Script/BlueprintGraph.K2Node_GetArrayItem
    - Name: K2Node_AsyncAction_3         Class: /Script/BlueprintGraph.K2Node_AsyncAction
    - Name: K2Node_Knot_2                Class: /Script/BlueprintGraph.K2Node_Knot
    - Name: K2Node_Knot_3                Class: /Script/BlueprintGraph.K2Node_Knot
    - Name: K2Node_Self_3                Class: /Script/BlueprintGraph.K2Node_Self
    - Name: K2Node_Self_2                Class: /Script/BlueprintGraph.K2Node_Self

## Announce to (GameState) Ready to play 
- Name:  EdGraphNode_Comment_16 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: UpdatePlayer1ReadyInGameState Name: K2Node_CallFunction_24       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: UpdatePlayer2ReadyInGameState Name: K2Node_CallFunction_25       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: DisplayWaitingForPlayerToPlaceShips Name: K2Node_CallFunction_26       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: InitiateGamePlay             Name: K2Node_CallFunction_27       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetupPlayer1BindingsPart2    Name: K2Node_CallFunction_31       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetupPlayer2BindingsPart2    Name: K2Node_CallFunction_8        Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_15        Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_MacroInstance_1       Class: /Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_VariableGet_19        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_20        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_21        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_5          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_6          Class: /Script/BlueprintGraph.K2Node_IfThenElse

## Handle Change Turns 
- Name:  EdGraphNode_Comment_17 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_11        Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_CallDelegate_3        Class: /Script/BlueprintGraph.K2Node_CallDelegate

## Initiate Random Start Player 
- Name:  EdGraphNode_Comment_19 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: RandomBool                   Name: K2Node_CallFunction_10       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: Delay                        Name: K2Node_CallFunction_11       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_18        Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableSet_3         Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_2         Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_0         Class: /Script/BlueprintGraph.K2Node_VariableGet

## Notify GameState of Ship Sunk 
- Name:  EdGraphNode_Comment_18 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_7         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableGet_1         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_12        Class: /Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_13        Class: /Script/BlueprintGraph.K2Node_VariableSet

## Show Attacking Player that Opponent\'s Ship was Sunk 
- Name:  EdGraphNode_Comment_20 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_9         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_MacroInstance_3       Class: /Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_VariableGet_2         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_11        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_12        Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_2          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_3          Class: /Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_CallDelegate_2        Class: /Script/BlueprintGraph.K2Node_CallDelegate

# GameBoardAnimation
## GameBoard Animation 
- Name:  EdGraphNode_Comment_0 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
    - EVENT ReceiveBeginPlay
    - EVENT ReceiveActorBeginOverlap
  - Function Calls
    - Call: K2_SetRelativeRotation       Name: K2Node_CallFunction_8        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: K2_SetRelativeLocation       Name: K2Node_CallFunction_6        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: K2_SetRelativeLocation       Name: K2Node_CallFunction_1        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: K2_SetRelativeRotation       Name: K2Node_CallFunction_0        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: GetCurrentLevelName          Name: K2Node_CallFunction_12       Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: EqualEqual_StrStr            Name: K2Node_CallFunction_13       Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_Timeline_0            Class: /Script/BlueprintGraph.K2Node_Timeline
    - Name: K2Node_VariableGet_4         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_Timeline_1            Class: /Script/BlueprintGraph.K2Node_Timeline
    - Name: K2Node_VariableGet_1         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_Knot_0                Class: /Script/BlueprintGraph.K2Node_Knot
    - Name: K2Node_Knot_1                Class: /Script/BlueprintGraph.K2Node_Knot
    - Name: K2Node_VariableGet_6         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_5         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_CustomEvent_0         Class: /Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableGet_0         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_3         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_2         Class: /Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_0          Class: /Script/BlueprintGraph.K2Node_IfThenElse

# Opening_Animation
## Opening Animation Animate 
- Name:  EdGraphNode_Comment_0 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
    - EVENT ReceiveBeginPlay
  - Function Calls
    - Call: K2_SetActorRotation          Name: K2Node_CallFunction_1        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: K2_GetActorRotation          Name: K2Node_CallFunction_2        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: Add_FloatFloat               Name: K2Node_CommutativeAssociativeBinaryOperator_0 Class: /Script/BlueprintGraph.K2Node_CommutativeAssociativeBinaryOperator
    - Call: Animate                      Name: K2Node_CallFunction_5        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: Delay                        Name: K2Node_CallFunction_6        Class: /Script/BlueprintGraph.K2Node_CallFunction
    - Call: OpenLevel                    Name: K2Node_CallFunction_7        Class: /Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_Timeline_0            Class: /Script/BlueprintGraph.K2Node_Timeline
    - Name: K2Node_Literal_0             Class: /Script/BlueprintGraph.K2Node_Literal

