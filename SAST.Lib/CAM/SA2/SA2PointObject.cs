using Kermalis.EndianBinaryIO;
using SAST.Lib.DataTypes;

namespace SAST.Lib.CAM.SA2
{
	public class SA2PointObject : IBinarySerializable
	{
		#region Internal
		#region Variables
		/// <summary>
		/// 3D Position of the <see cref="SA2PointObject"/> in the scene.
		/// </summary>
		public FloatVector PlayerPoint { get; set; } = new FloatVector();

		/// <summary>
		/// Radius size of the <see cref="SA2PointObject"/>.
		/// </summary>
		public float PlayerPointRadius { get; set; } = 1.0f;

		/// <summary>
		/// 3D Position of the <see cref="SA2PointObject"/>'s camera in the scene.
		/// </summary>
		public FloatVector CameraPoint { get; set; } = new FloatVector();

		/// <summary>
		/// Radius size of the camera in the <see cref="SA2PointObject"/>.
		/// 
		/// Has no effect in-game and effectively goes unused.
		/// </summary>
		public float CameraPointRadius { get; set; } = 0.0f;

		/// <summary>
		/// Indices to any linked <see cref="SA2PointObject"/>s in the scene.
		/// </summary>
		public short[] Links { get; set; } = { -1, -1, -1, -1, -1, -1 };

		/// <summary>
		/// When not -1, indicates the travel direction of the linked cameras.
		/// 
		/// When used, the camera will flow along an average of the line of points for a more fluid movement.
		/// Is prone to crashing when using indices that are not connected to the point in the <see cref="Links"/>.
		/// </summary>
		public short FlowIndex { get; set; } = -1;

		/// <summary>
		/// When true, the point will interact with the player.
		/// 
		/// If false, the point can still be referenced by other points.
		/// </summary>
		[BinaryBooleanSize(BooleanSize.U8)]
		public bool IsPlayerPointEnabled { get; set; } = true;

		/// <summary>
		/// When a <see cref="FlowIndex"/> is set, this enables the camera to retain tracking the player along its path.
		/// 
		/// If disabled, the camera follows the fixed path along the points without attempting to keep the player in view.
		/// </summary>
		[BinaryBooleanSize(BooleanSize.U8)]
		public bool TrackPlayer { get; set; } = false;
		#endregion

		#region Constructors
		public SA2PointObject() { }

		#endregion

		#region Functions
		/// <summary>
		/// <see cref="IBinarySerializable"/> method for reading <see cref="SA2PointObject"/>.
		/// </summary>
		/// <param name="endianBinaryReader"></param>
		public void Read(EndianBinaryReader endianBinaryReader)
		{
			PlayerPoint = endianBinaryReader.ReadObject<FloatVector>();
			PlayerPointRadius = endianBinaryReader.ReadSingle();
			CameraPoint = endianBinaryReader.ReadObject<FloatVector>();
			CameraPointRadius = endianBinaryReader.ReadSingle();
			for (int i = 0; i < 6; i++)
				Links[i] = endianBinaryReader.ReadInt16();
			FlowIndex = endianBinaryReader.ReadInt16();
			IsPlayerPointEnabled = endianBinaryReader.ReadBoolean8();
			TrackPlayer = endianBinaryReader.ReadBoolean8();
		}

		/// <summary>
		/// <see cref="IBinarySerializable"/> method for writing <see cref="SA2PointObject"/>.
		/// </summary>
		/// <param name="endianBinaryWriter"></param>
		public void Write(EndianBinaryWriter endianBinaryWriter)
		{
			endianBinaryWriter.WriteObject(PlayerPoint);
			endianBinaryWriter.WriteSingle(PlayerPointRadius);
			endianBinaryWriter.WriteObject(CameraPoint);
			endianBinaryWriter.WriteSingle(CameraPointRadius);
			for (int i = 0; i < 6; i++)
				endianBinaryWriter.WriteInt16(Links[i]);
			endianBinaryWriter.WriteInt16(FlowIndex);
			endianBinaryWriter.WriteBoolean8(IsPlayerPointEnabled);
			endianBinaryWriter.WriteBoolean8(TrackPlayer);
		}

		/// <summary>
		/// Checks if the PlayerPoint and CameraPoint variables are not empty/new.
		/// </summary>
		/// <returns>True if the PlayerPoint and CameraPoint variables are new, else false.</returns>
		public bool IsEmpty()
		{
			if (PlayerPoint.IsEmpty() && PlayerPointRadius == 0.0f)
				return true;
			else
				return false;
		}

		#endregion
		#endregion

		#region Static
		public static readonly int Size = 48;

		#endregion
	}
}