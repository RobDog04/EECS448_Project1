# BattleshipPlayerController
## Update Server (GameState) with Player 2 Connected (Run on Server Only) 
- Name:  EdGraphNode_Comment_11 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_0         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableSet_0         Class:/Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_16        Class:/Script/BlueprintGraph.K2Node_VariableGet

## Update Server (GameState) with Player 1 Connected (Run on Server Only) 
- Name:  EdGraphNode_Comment_12 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_1         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableSet_1         Class:/Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_3         Class:/Script/BlueprintGraph.K2Node_VariableGet

## Determine if the Player Has Selected a Game Mode (GameInstance) 
- Name:  EdGraphNode_Comment_13 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
    - EVENT ReceiveBeginPlay
  - Function Calls
    - Call:GetCurrentLevelName          Name: K2Node_CallFunction_12       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:EqualEqual_StrStr            Name: K2Node_CallFunction_13       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_Composite_0           Class:/Script/BlueprintGraph.K2Node_Composite
    - Name: K2Node_MacroInstance_0       Class:/Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_IfThenElse_0          Class:/Script/BlueprintGraph.K2Node_IfThenElse

## If Host Mode Selected Notify GameState of Player 1 Connected 
- Name:  EdGraphNode_Comment_14 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call:UpdatePlayer1ConnectedInGameState Name: K2Node_CallFunction_4        Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:DisplayWaitingForPlayerToConnect Name: K2Node_CallFunction_6        Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:SetGameStateShipCount        Name: K2Node_CallFunction_7        Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:SetupPlayer1Bindings         Name: K2Node_CallFunction_18       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CallDelegate_1        Class:/Script/BlueprintGraph.K2Node_CallDelegate

## If Join Mode Selected Notify GameState of Player 2 Connected 
- Name:  EdGraphNode_Comment_15 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call:UpdatePlayer2ConnectedInGameState Name: K2Node_CallFunction_30       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:SetupPlayer2Bindings         Name: K2Node_CallFunction_19       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:DisplayConnectingToGameHost  Name: K2Node_CallFunction_20       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CallDelegate_0        Class:/Script/BlueprintGraph.K2Node_CallDelegate

## Update Server (GameState) with Player 1 Ready (Run on Server Only) 
- Name:  EdGraphNode_Comment_1 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_2         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableGet_6         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_4         Class:/Script/BlueprintGraph.K2Node_VariableSet

## Update Server (GameState) with Player 2 Ready (Run on Server Only) 
- Name:  EdGraphNode_Comment_2 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_3         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableGet_5         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_5         Class:/Script/BlueprintGraph.K2Node_VariableSet

## Update Server (GameState) with Block Currently under attack 
- Name:  EdGraphNode_Comment_5 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_4         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableGet_7         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_6         Class:/Script/BlueprintGraph.K2Node_VariableSet

## Update Server (GameState) with Player 1 Turn Status (Run on Server Only) 
- Name:  EdGraphNode_Comment_7 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_6         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableGet_10        Class:/Script/BlueprintGraph.K2Node_VariableGet

## Update Server (GameState) with Player 2 Turn Status (Run on Server Only) 
- Name:  EdGraphNode_Comment_8 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_5         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableGet_8         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_8         Class:/Script/BlueprintGraph.K2Node_VariableSet

## Update Server (GameState) with Ship Hit (Run on Server Only) 
- Name:  EdGraphNode_Comment_0 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_8         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableGet_9         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_9         Class:/Script/BlueprintGraph.K2Node_VariableSet

## Handle Win/Lose Conditions 
- Name:  EdGraphNode_Comment_3 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call:DisplayWin                   Name: K2Node_CallFunction_1        Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:DisplayLose                  Name: K2Node_CallFunction_3        Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_10        Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_IfThenElse_4          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_MacroInstance_2       Class:/Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_IfThenElse_1          Class:/Script/BlueprintGraph.K2Node_IfThenElse

## Set (GameState) Ship Count using Game Instance 
- Name:  EdGraphNode_Comment_4 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_12        Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableGet_13        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_14        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_15        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_10        Class:/Script/BlueprintGraph.K2Node_VariableSet

## If Game Mode Not Selected Yet 
- Name:  EdGraphNode_Comment_6 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call:DisplayHostOrJoin            Name: K2Node_CallFunction_22       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others

## Setup Server Host Connection and Reopen Level in ?listen for Client connection state 
- Name:  EdGraphNode_Comment_9 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call:OpenLevel                    Name: K2Node_CallFunction_46       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_13        Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_AsyncAction_0         Class:/Script/BlueprintGraph.K2Node_AsyncAction
    - Name: K2Node_VariableSet_11        Class:/Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_4         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_17        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_18        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_Self_1                Class:/Script/BlueprintGraph.K2Node_Self

## Connect to a Hosted LAN Server as a Client. Also display a \"Connecting to Host\" UI until connection established 
- Name:  EdGraphNode_Comment_10 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call:DisplayConnectingToGameHost  Name: K2Node_CallFunction_23       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_14        Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_AsyncAction_2         Class:/Script/BlueprintGraph.K2Node_AsyncAction
    - Name: K2Node_GetArrayItem_0        Class:/Script/BlueprintGraph.K2Node_GetArrayItem
    - Name: K2Node_AsyncAction_3         Class:/Script/BlueprintGraph.K2Node_AsyncAction
    - Name: K2Node_Knot_2                Class:/Script/BlueprintGraph.K2Node_Knot
    - Name: K2Node_Knot_3                Class:/Script/BlueprintGraph.K2Node_Knot
    - Name: K2Node_Self_3                Class:/Script/BlueprintGraph.K2Node_Self
    - Name: K2Node_Self_2                Class:/Script/BlueprintGraph.K2Node_Self

## Announce to (GameState) Ready to play 
- Name:  EdGraphNode_Comment_16 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call:UpdatePlayer1ReadyInGameState Name: K2Node_CallFunction_24       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:UpdatePlayer2ReadyInGameState Name: K2Node_CallFunction_25       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:DisplayWaitingForPlayerToPlaceShips Name: K2Node_CallFunction_26       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:InitiateGamePlay             Name: K2Node_CallFunction_27       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:SetupPlayer1BindingsPart2    Name: K2Node_CallFunction_31       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:SetupPlayer2BindingsPart2    Name: K2Node_CallFunction_8        Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_15        Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_MacroInstance_1       Class:/Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_VariableGet_19        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_20        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_21        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_5          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_6          Class:/Script/BlueprintGraph.K2Node_IfThenElse

## Handle Change Turns 
- Name:  EdGraphNode_Comment_17 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_11        Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_CallDelegate_3        Class:/Script/BlueprintGraph.K2Node_CallDelegate

## Initiate Random Start Player 
- Name:  EdGraphNode_Comment_19 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
    - Call:RandomBool                   Name: K2Node_CallFunction_10       Class:/Script/BlueprintGraph.K2Node_CallFunction
    - Call:Delay                        Name: K2Node_CallFunction_11       Class:/Script/BlueprintGraph.K2Node_CallFunction
  - Others
    - Name: K2Node_CustomEvent_18        Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableSet_3         Class:/Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_2         Class:/Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableGet_0         Class:/Script/BlueprintGraph.K2Node_VariableGet

## Notify GameState of Ship Sunk 
- Name:  EdGraphNode_Comment_18 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_7         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_VariableGet_1         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableSet_12        Class:/Script/BlueprintGraph.K2Node_VariableSet
    - Name: K2Node_VariableSet_13        Class:/Script/BlueprintGraph.K2Node_VariableSet

## Show Attacking Player that Opponent\'s Ship was Sunk 
- Name:  EdGraphNode_Comment_20 
- Class:  /Script/UnrealEd.EdGraphNode_Comment 
- Members: 
  - Events
  - Function Calls
  - Others
    - Name: K2Node_CustomEvent_9         Class:/Script/BlueprintGraph.K2Node_CustomEvent
    - Name: K2Node_MacroInstance_3       Class:/Script/BlueprintGraph.K2Node_MacroInstance
    - Name: K2Node_VariableGet_2         Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_11        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_VariableGet_12        Class:/Script/BlueprintGraph.K2Node_VariableGet
    - Name: K2Node_IfThenElse_2          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_IfThenElse_3          Class:/Script/BlueprintGraph.K2Node_IfThenElse
    - Name: K2Node_CallDelegate_2        Class:/Script/BlueprintGraph.K2Node_CallDelegate