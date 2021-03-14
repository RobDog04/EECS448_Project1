# Battleship_MainGameMap
## Connect Player 2 to in-map camera (Client-Only) 
- Name:  EdGraphNode_Comment_0 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: SetViewTargetWithBlend       Name: K2Node_CallFunction_28       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_Literal_4             Class:/Script/BlueprintGraph.K2Node_Literal
    - Name: K2Node_CustomEvent_3         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_MacroInstance_5       Class:/Script/BlueprintGraph.K2Node_MacroInstance

## Confirm Valid/Legal Placement of Ships before allowing the game to progress 
- Name:  EdGraphNode_Comment_2 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: CheckShipPlacement           Name: K2Node_CallFunction_15       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetActorHiddenInGame         Name: K2Node_CallFunction_18       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: AnnounceReadyToPlay          Name: K2Node_CallFunction_57       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: DisplayInvalidShipPlacement  Name: K2Node_CallFunction_58       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_2         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_IfThenElse_0          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_Literal_1             Class:/Script/BlueprintGraph.K2Node_Literal
    - Name: K2Node_VariableGet_15        Class:/Script/BlueprintGraph.K2Node_VariableGet

## Adjust visible ships to match selected ship count 
- Name:  EdGraphNode_Comment_4 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: AdjustVisibleShipsToShipCount Name: K2Node_CallFunction_14       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetupClientCamera            Name: K2Node_CallFunction_29       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetActorHiddenInGame         Name: K2Node_CallFunction_17       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: DisplayConfirmShipPlacement  Name: K2Node_CallFunction_60       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_6         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_MacroInstance_4       Class:/Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_Literal_0             Class:/Script/BlueprintGraph.K2Node_Literal

## Determine if a Game Mode has been selected 
- Name:  EdGraphNode_Comment_9 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
    - EVENT ReceiveBeginPlay
  - Function Calls
    - Call: PopulateLevelVariables       Name: K2Node_CallFunction_40       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetupBindings                Name: K2Node_CallFunction_55       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: Delay                        Name: K2Node_CallFunction_65       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_IfThenElse_11         Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_Knot_2                Class:/Script/BlueprintGraph.K2Node_Knot
    - Name: K2Node_Knot_3                Class:/Script/BlueprintGraph.K2Node_Knot

## Handle Game Attack Event 
- Name:  EdGraphNode_Comment_16 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: AttackBoardPosition          Name: K2Node_CallFunction_9        Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: UpdatePlayer1TurnInGameState Name: K2Node_CallFunction_19       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: UpdatePlayer2TurnInGameState Name: K2Node_CallFunction_20       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: Delay                        Name: K2Node_CallFunction_31       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: Delay                        Name: K2Node_CallFunction_3        Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: DisablePlayingBoard          Name: K2Node_CallFunction_33       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: DisablePlayingBoard          Name: K2Node_CallFunction_32       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: AttackBlock                  Name: K2Node_CallFunction_2        Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: Delay                        Name: K2Node_CallFunction_35       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_16        Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_MacroInstance_14      Class:/Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_VariableGet_10        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_11        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_5          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_6          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_Knot_4                Class:/Script/BlueprintGraph.K2Node_Knot
    - Name: K2Node_Knot_5                Class:/Script/BlueprintGraph.K2Node_Knot
    - Name: K2Node_VariableGet_0         Class:/Script/BlueprintGraph.K2Node_VariableGet

## Handle Ship Hit Event 
- Name:  EdGraphNode_Comment_17 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: EqualEqual_IntInt            Name: K2Node_CallFunction_4        Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: Activate                     Name: K2Node_CallFunction_45       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: SendShipHit                  Name: K2Node_CallFunction_52       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: EqualEqual_IntInt            Name: K2Node_CallFunction_43       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: IsValid                      Name: K2Node_CallFunction_6        Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: GetOverlappingActors         Name: K2Node_CallFunction_8        Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: Add_IntInt                   Name: K2Node_CommutativeAssociativeBinaryOperator_0 Class:/Script/BlueprintGraph.K2Node_CommutativeAssociativeBinaryOperator
    - Call: HandleCombatHit              Name: K2Node_CallFunction_10       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: Delay                        Name: K2Node_CallFunction_30       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_15        Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_MacroInstance_0       Class:/Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_VariableGet_8         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_9         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_3          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_4          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_12        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_MacroInstance_15      Class:/Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_VariableGet_2         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_7          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_VariableGet_14        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_MacroInstance_2       Class:/Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_VariableGet_1         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_13        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_3         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_8          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_GetArrayItem_0        Class:/Script/BlueprintGraph.K2Node_GetArrayItem
    - Name: K2Node_IfThenElse_9          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_DynamicCast_0         Class:/Script/BlueprintGraph.K2Node_DynamicCast
    - Name: K2Node_VariableGet_4         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_0         Class:/Script/BlueprintGraph.K2Node_VariableSet

## Handle Change Turns Event 
- Name:  EdGraphNode_Comment_1 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: DisablePlayingBoard          Name: K2Node_CallFunction_0        Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: EnablePlayingBoard           Name: K2Node_CallFunction_1        Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_0         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_MacroInstance_1       Class:/Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_IfThenElse_1          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_2          Class:/Script/BlueprintGraph.K2Node_IfThenElse

## Handle Opponent Ship Sunk and Reset ShipSunk in GameState 
- Name:  EdGraphNode_Comment_3 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call: SetActorHiddenInGame         Name: K2Node_CallFunction_13       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetActorHiddenInGame         Name: K2Node_CallFunction_16       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetActorHiddenInGame         Name: K2Node_CallFunction_21       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetActorHiddenInGame         Name: K2Node_CallFunction_22       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetActorHiddenInGame         Name: K2Node_CallFunction_23       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: SetActorHiddenInGame         Name: K2Node_CallFunction_12       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call: ResetShipSunk                Name: K2Node_CallFunction_26       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_1         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_SwitchInteger_0       Class:/Script/BlueprintGraph.K2Node_SwitchInteger
    - Name: K2Node_Literal_2             Class:/Script/BlueprintGraph.K2Node_Literal
    - Name: K2Node_Literal_3             Class:/Script/BlueprintGraph.K2Node_Literal
    - Name: K2Node_Literal_5             Class:/Script/BlueprintGraph.K2Node_Literal
    - Name: K2Node_Literal_6             Class:/Script/BlueprintGraph.K2Node_Literal
    - Name: K2Node_Literal_7             Class:/Script/BlueprintGraph.K2Node_Literal
    - Name: K2Node_Literal_8             Class:/Script/BlueprintGraph.K2Node_Literal
    - Name: K2Node_VariableGet_5         Class:/Script/BlueprintGraph.K2Node_VariableGet

