namespace SAST.Lib.CAM.SA1
{
	/// <summary>
	/// Camera Level (Detection) method from Sonic Adventure 1
	/// 
	/// These are auto assigned by their camera types.
	/// </summary>
	public enum SA1CamLevel : byte
	{
		Normal = 0,
		Area = 1,
		Compulsion = 2,
		Collision = 3,
	}

	/// <summary>
	/// Camera Types/Modes from Sonic Adventure 1
	/// </summary>
	public enum SA1CamMode : byte
	{
		Follow = 0,
		Follow_Area = Follow + SA1CamLevel.Area,
		Follow_Compulsion = Follow + SA1CamLevel.Compulsion,
		Follow_Collision = Follow + SA1CamLevel.Collision,

		Knuckles = 4,
		Knuckles_Area = Knuckles + SA1CamLevel.Area,
		Knuckles_Compulsion = Knuckles + SA1CamLevel.Compulsion,
		Knuckles_Collision = Knuckles + SA1CamLevel.Collision,

		Knuckles2 = 8,
		Knuckles2_Area = Knuckles2 + SA1CamLevel.Area,
		Knuckles2_Compulsion = Knuckles2 + SA1CamLevel.Compulsion,
		Knuckles2_Collision = Knuckles2 + SA1CamLevel.Collision,

		Magonote = 12,
		Magonote_Area = Magonote + SA1CamLevel.Area,
		Magonote_Compulsion = Magonote + SA1CamLevel.Compulsion,
		Magonote_Collision = Magonote + SA1CamLevel.Collision,

		Sonic = 16,
		Sonic_Area = Sonic + SA1CamLevel.Area,
		Sonic_Compulsion = Sonic + SA1CamLevel.Compulsion,
		Sonic_Collision = Sonic + SA1CamLevel.Collision,

		Ashland = 20,
		Ashland_Area = Ashland + SA1CamLevel.Area,
		Ashland_Compulsion = Ashland + SA1CamLevel.Compulsion,

		AshlandI = 23,
		AshlandI_Area = AshlandI + SA1CamLevel.Area,
		AshlandI_Compulsion = AshlandI + SA1CamLevel.Compulsion,

		Fishing = 26,
		Fishing_Area = Fishing + SA1CamLevel.Area,

		Fixed = 28,
		Fixed_Area = Fixed + SA1CamLevel.Area,
		Fixed_Compulsion = Fixed + SA1CamLevel.Compulsion,

		Klamath = 31,
		Klamath_Area = Klamath + SA1CamLevel.Area,
		Klamath_Compulsion = Klamath + SA1CamLevel.Compulsion,

		Line = 34,
		Line_Area = Line + SA1CamLevel.Area,

		NewFollow = 36,
		NewFollow_Area = NewFollow + SA1CamLevel.Area,
		NewFollow_Compulsion = NewFollow + SA1CamLevel.Compulsion,

		Point = 39,
		Point_Area = Point + SA1CamLevel.Area,
		Point_Compulsion = Point + SA1CamLevel.Compulsion,

		SonicP = 42,
		SonicP_Area = SonicP + SA1CamLevel.Area,
		SonicP_Compulsion = SonicP + SA1CamLevel.Compulsion,

		Advertise = 45,

		Back = 46,

		Back2 = 47,

		Building = 48,

		Cart = 49,

		Chaos = 50,
		ChaosP = 51,
		ChaosStageInit = 52,
		ChaosStandard = 53,
		ChaosW = 54,

		E101R = 55,

		E103 = 56,

		EGM3 = 57,

		FollowG = 58,
		FollowG_Area = FollowG + SA1CamLevel.Area,

		LeftRight = 60,

		Collision = 61,

		RuinWaka1 = 62,

		Snowboard = 63,

		Survey = 64,

		Taiho = 65,

		Tornado = 66,

		TwoHares = 67,

		Leave = 68,

		Avoid = 69,
		Avoid_Area = Avoid + SA1CamLevel.Area,
		Avoid_Compulsion = Avoid + SA1CamLevel.Compulsion,
		Avoid_Collision = Avoid + SA1CamLevel.Collision,

		Editor = 72,

		GuriGuri = 73,

		PathCam = 74,

		KosCam = 75,
	}

	/// <summary>
	/// Camera Adjustment Modes from Sonic Adventure 1.
	/// 
	/// These are how cameras transition between each other.
	/// </summary>
	public enum SA1CamAdjustMode : byte
	{
		None = 0,

		Normal = 1,
		NormalS = 2,

		Slow = 3,
		SlowS = 4,

		Time = 5,

		Three1 = 6,
		Three1C = 7,

		Three2 = 8,
		Three2C = 9,

		Three3 = 10,
		Three3C = 11,

		Three4 = 12,
		Three4C = 13,

		Three5 = 14,
		Three5C = 15,

		Relative1 = 16,
		Relative1C = 17,

		Relative2 = 18,
		Relative2C = 19,

		Relative3 = 20,
		Relative3C = 21,

		Relative4 = 22,
		Relative4C = 23,

		Relative5 = 24,
		Relative5C = 25,

		Relative6C = 26,

		FreeCamera = 27,
	}

	/// <summary>
	/// The Collision Shape used by <see cref="SA1CamObject"/>s
	/// </summary>
	public enum SA1CamCollisionShape : byte
	{
		Sphere = 0,
		Plane = 1,
		Block = 2,
	}
}
