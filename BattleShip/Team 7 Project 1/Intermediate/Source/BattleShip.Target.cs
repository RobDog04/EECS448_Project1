using UnrealBuildTool;

public class BattleShipTarget : TargetRules
{
	public BattleShipTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Game;
		ExtraModuleNames.Add("BattleShip");
	}
}
