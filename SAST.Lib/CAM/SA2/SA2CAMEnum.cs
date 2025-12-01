namespace SAST.Lib.CAM.SA2
{
	/// <summary>
	/// Camera Modes/Types from Sonic Adventure 2.
	/// </summary>
	public enum SA2CamMode : int
	{
		None = 0,
		User = 1,
		Follow = 2,
		Knuckles = 3,
		Editor = 4,
		Editor2 = 5,
		SnapShot = 6,
		Klamath = 7,
		Point = 8,
		Ashland = 9,
		Fix = 10,
		Leave = 11,
		Space = 12,
		Carmel = 13,
		Motion = 14,
		BossInit = 15,
		BossPoint = 16,
		Collision = 17,
		PStone = 18,
		Init = 19,
		EasySet = 20,
		BossKlamath = 21,
		GakuGaku = 22,
		Knuckles_L = 23,
		Fix2 = 24,
		PStone2 = 25,
		SS = 26,
		Colli_LR = 27,
	}

	/// <summary>
	/// Camera Adjustment Types from Sonic Adventure 2.
	/// 
	/// These are how cameras transition between each other.
	/// </summary>
	public enum SA2CamAdjustMode : int
	{
		None = 0,
		User = 1,

		Half = 2,

		Three1 = 3,
		Three2 = 4,
		Three3 = 5,
		Three4 = 6,
		Three5 = 7,

		Relative1 = 8,
		Relative2 = 9,
		Relative3 = 10,
		Relative4 = 11,
		Relative5 = 12,
		Relative6 = 13,
	}

	/// <summary>
	/// The Collision Shapes used <see cref="SA2CAMObject"/>s
	/// </summary>
	public enum SA2CamCollisionShape : int
	{
		Sphere = 1,
		Plane = 2,
		Block = 3,
	}
}
