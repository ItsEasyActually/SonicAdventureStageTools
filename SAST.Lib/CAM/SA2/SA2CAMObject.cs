using Kermalis.EndianBinaryIO;
using SAST.Lib.DataTypes;

namespace SAST.Lib.CAM.SA2
{
	/// <summary>
	/// Represents a Camera Object used within SA2's Camera Files.
	/// </summary>
	public class SA2CAMObject : CAMObject, IBinarySerializable
	{
		#region Internal
		#region Variables
		/// <summary>
		/// Mode (or type) for the camera.
		/// 
		/// See <see cref="SA2CamMode"/> for more information.
		/// </summary>
		public SA2CamMode Mode { get; set; } = SA2CamMode.Follow;

		/// <summary>
		/// Method in which one camera object will transition to another as the player modes between camera volumes.
		/// 
		/// See <see cref="SA2CamAdjustMode"/> for more information.
		/// </summary>
		public SA2CamAdjustMode AdjustMode { get; set; } = SA2CamAdjustMode.Relative3;

		/// <summary>
		/// Type of collision volume to be used by the camera.
		/// 
		/// See <see cref="SA2CamCollisionShape"/> for more information.
		/// </summary>
		public SA2CamCollisionShape CollisionShape { get; set; } = SA2CamCollisionShape.Sphere;

		public int IntProperty1 { get; set; } = 0;
		public int IntProperty2 { get; set; } = 0;
		public int IntProperty3 { get; set; } = 0;
		public int IntProperty4 { get; set; } = 0;
		public int IntProperty5 { get; set; } = 0;
		public int IntProperty6 { get; set; } = 0;
		public int IntProperty7 { get; set; } = 0;
		public int IntProperty8 { get; set; } = 0;

		public float FloatProperty1 { get; set; } = 0.0f;
		public float FloatProperty2 { get; set; } = 0.0f;
		public float FloatProperty3 { get; set; } = 0.0f;
		public float FloatProperty4 { get; set; } = 0.0f;
		public float FloatProperty5 { get; set; } = 0.0f;
		public float FloatProperty6 { get; set; } = 0.0f;
		public float FloatProperty7 { get; set; } = 0.0f;
		public float FloatProperty8 { get; set; } = 0.0f;
		#endregion

		#region Constructors
		/// <summary>
		/// Default constructor.
		/// </summary>
		public SA2CAMObject() { }

		/// <summary>
		/// Creates a new <see cref="SA2CamObject"/> using the provided data.
		/// </summary>
		/// <param name="mode">Camera Mode</param>
		/// <param name="priority">Camera's Priority</param>
		/// <param name="adjmode">Camera's Adjustment Mode</param>
		/// <param name="colmode">Camera's Collision Type</param>
		/// <param name="colposx">Collision Volume's X Position</param>
		/// <param name="colposy">Collision Volume's Y Position</param>
		/// <param name="colposz">Collision Volume's Z Position</param>
		/// <param name="colangx">Collision Volume's X Angle</param>
		/// <param name="colangy">Collision Volume's Y Angle</param>
		/// <param name="colangz">Collision Volume's Z Angle</param>
		/// <param name="colsclx">Collision Volume's X Scale</param>
		/// <param name="colscly">Collision Volume's Y Scale</param>
		/// <param name="colsclz">Collision Volume's Z Scale</param>
		/// <param name="camposx">Camera's X Position</param>
		/// <param name="camposy">Camera's Y Position</param>
		/// <param name="camposz">Camera's Z Position</param>
		/// <param name="camangx">Camera's X Angle</param>
		/// <param name="camangy">Camera's Y Angle</param>
		/// <param name="camangz">Camera's Z Angle</param>
		/// <param name="camtgtx">Camera Target's X Position</param>
		/// <param name="camtgty">Camera Target's Y Position</param>
		/// <param name="camtgtz">Camera Target's Z Position</param>
		/// <param name="iprop1">Camera Integer Property 1</param>
		/// <param name="iprop2">Camera Integer Property 2</param>
		/// <param name="iprop3">Camera Integer Property 3</param>
		/// <param name="iprop4">Camera Integer Property 4</param>
		/// <param name="iprop5">Camera Integer Property 5</param>
		/// <param name="iprop6">Camera Integer Property 6</param>
		/// <param name="iprop7">Camera Integer Property 7</param>
		/// <param name="iprop8">Camera Integer Property 8</param>
		/// <param name="fprop1">Camera Float Property 1</param>
		/// <param name="fprop2">Camera Float Property 2</param>
		/// <param name="fprop3">Camera Float Property 3</param>
		/// <param name="fprop4">Camera Float Property 4</param>
		/// <param name="fprop5">Camera Float Property 5</param>
		/// <param name="fprop6">Camera Float Property 6</param>
		/// <param name="fprop7">Camera Float Property 7</param>
		/// <param name="fprop8">Camera Float Property 8</param>
		public SA2CAMObject(SA2CamMode mode, byte priority, SA2CamAdjustMode adjmode, SA2CamCollisionShape colmode,
			float colposx, float colposy, float colposz, int colangx, int colangy, int colangz, float colsclx, float colscly, float colsclz,
			float camposx, float camposy, float camposz, int camangx, int camangy, int camangz, float camtgtx, float camtgty, float camtgtz,
			int iprop1, int iprop2, int iprop3, int iprop4, int iprop5, int iprop6, int iprop7, int iprop8,
			float fprop1, float fprop2, float fprop3, float fprop4, float fprop5, float fprop6, float fprop7, float fprop8)
		{
			Mode = mode;
			Priority = priority;
			AdjustMode = adjmode;
			CollisionShape = colmode;

			Collision = new Node(colposx, colposy, colposz, colangx, colangy, colangz, colsclx, colscly, colsclz);

			CameraPosition = new FloatVector(camposx, camposy, camposz);
			CameraRotation = new RotationVector(camangx, camangy, camangz);
			CameraTarget = new FloatVector(camtgtx, camtgty, camtgtz);

			IntProperty1 = iprop1; IntProperty2 = iprop2; IntProperty3 = iprop3; IntProperty4 = iprop4;
			IntProperty5 = iprop5; IntProperty6 = iprop6; IntProperty7 = iprop7; IntProperty8 = iprop8;

			FloatProperty1 = fprop1; FloatProperty2 = fprop2; FloatProperty3 = fprop3; FloatProperty4 = fprop4;
			FloatProperty5 = fprop5; FloatProperty6 = fprop6; FloatProperty7 = fprop7; FloatProperty8 = fprop8;
		}

		#endregion

		#region Functions
		/// <summary>
		/// <see cref="IBinarySerializable"/> method for reading <see cref="SA2CamObject"/>.
		/// </summary>
		/// <param name="endianBinaryReader"></param>
		public void Read(EndianBinaryReader endianBinaryReader)
		{
			Mode = endianBinaryReader.ReadEnum<SA2CamMode>();
			AdjustMode = endianBinaryReader.ReadEnum<SA2CamAdjustMode>();
			Priority = endianBinaryReader.ReadInt32();
			CollisionShape = endianBinaryReader.ReadEnum<SA2CamCollisionShape>();

			Collision = endianBinaryReader.ReadObject<Node>();

			CameraPosition = endianBinaryReader.ReadObject<FloatVector>();
			CameraRotation = endianBinaryReader.ReadObject<RotationVector>();
			CameraTarget = endianBinaryReader.ReadObject<FloatVector>();

			IntProperty1 = endianBinaryReader.ReadInt32();
			IntProperty2 = endianBinaryReader.ReadInt32();
			IntProperty3 = endianBinaryReader.ReadInt32();
			IntProperty4 = endianBinaryReader.ReadInt32();
			IntProperty5 = endianBinaryReader.ReadInt32();
			IntProperty6 = endianBinaryReader.ReadInt32();
			IntProperty7 = endianBinaryReader.ReadInt32();
			IntProperty8 = endianBinaryReader.ReadInt32();

			FloatProperty1 = endianBinaryReader.ReadSingle();
			FloatProperty2 = endianBinaryReader.ReadSingle();
			FloatProperty3 = endianBinaryReader.ReadSingle();
			FloatProperty4 = endianBinaryReader.ReadSingle();
			FloatProperty5 = endianBinaryReader.ReadSingle();
			FloatProperty6 = endianBinaryReader.ReadSingle();
			FloatProperty7 = endianBinaryReader.ReadSingle();
			FloatProperty8 = endianBinaryReader.ReadSingle();
		}

		/// <summary>
		/// <see cref="IBinarySerializable"/> method for writing <see cref="SA2CamObject"/>.
		/// </summary>
		/// <param name="endianBinaryWriter"></param>
		public void Write(EndianBinaryWriter endianBinaryWriter)
		{
			endianBinaryWriter.WriteEnum(Mode);
			endianBinaryWriter.WriteEnum(AdjustMode);
			endianBinaryWriter.WriteInt32(Priority);
			endianBinaryWriter.WriteEnum(CollisionShape);

			endianBinaryWriter.WriteObject(Collision);

			endianBinaryWriter.WriteObject(CameraPosition);
			endianBinaryWriter.WriteObject(CameraRotation);
			endianBinaryWriter.WriteObject(CameraTarget);

			endianBinaryWriter.WriteInt32(IntProperty1);
			endianBinaryWriter.WriteInt32(IntProperty2);
			endianBinaryWriter.WriteInt32(IntProperty3);
			endianBinaryWriter.WriteInt32(IntProperty4);
			endianBinaryWriter.WriteInt32(IntProperty5);
			endianBinaryWriter.WriteInt32(IntProperty6);
			endianBinaryWriter.WriteInt32(IntProperty7);
			endianBinaryWriter.WriteInt32(IntProperty8);

			endianBinaryWriter.WriteSingle(FloatProperty1);
			endianBinaryWriter.WriteSingle(FloatProperty2);
			endianBinaryWriter.WriteSingle(FloatProperty3);
			endianBinaryWriter.WriteSingle(FloatProperty4);
			endianBinaryWriter.WriteSingle(FloatProperty5);
			endianBinaryWriter.WriteSingle(FloatProperty6);
			endianBinaryWriter.WriteSingle(FloatProperty7);
			endianBinaryWriter.WriteSingle(FloatProperty8);
		}

		/// <summary>
		/// Checks to see if the Camera is empty.
		/// </summary>
		/// <returns>True if the Camera's Mode, AdjustMode, Priority and CollisionShape are 0 and the Collision is empty, otherwise returns False.</returns>
		public bool IsEmpty()
		{
			if (Mode == 0 && AdjustMode == 0 && Priority == 0 && CollisionShape == 0 && Collision.IsEmpty())
				return true;
			else
				return false;
		}

		#endregion
		#endregion

		#region Static
		public static readonly int Size = 152;

		public static SA2CamMode GetCamModeFromString(string val)
		{
			bool parsed = Enum.TryParse<SA2CamMode>(val, out SA2CamMode result);

			if (parsed)
				return result;
			else
			{
				Console.WriteLine($"Invalid Camera Mode: {val}, returning None Camera Mode.");
				return SA2CamMode.None;
			}
		}

		public static SA2CamAdjustMode GetAdjustModeFromString(string val)
		{
			bool parsed = Enum.TryParse<SA2CamAdjustMode>(val, out SA2CamAdjustMode result);

			if (parsed)
				return result;
			else
			{
				Console.WriteLine($"Invalid Camera Adjust Mode: {val}, returning Relative3 Adjust Mode.");
				return SA2CamAdjustMode.Relative3;
			}
		}

		public static SA2CamCollisionShape GetCollisionShapeFromInt(int val)
		{
			return (SA2CamCollisionShape)val;
		}

		#endregion
	}
}
