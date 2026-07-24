using Amicitia.IO.Binary;
using SAST.Lib.DataTypes;
using SAST.Lib.Extensions;

namespace SAST.Lib.CAM.SA1
{
	public class SA1CAMObject : CAMObject, IBinarySerializable
	{
		#region Internal
		#region Variables
		/// <summary>
		/// Mode (or type) for the camera. 
		/// 
		/// See <see cref="SA1CamMode"/> for more information.
		/// </summary>
		public SA1CamMode Mode { get; set; } = SA1CamMode.Follow;

		/// <summary>
		/// Method in which one camera object will transition to another as the player moves between camera volumes.
		/// 
		/// See <see cref="SA1CamAdjustMode"/> for more information.
		/// </summary>
		public SA1CamAdjustMode AdjustMode { get; set; } = SA1CamAdjustMode.Relative3;

		/// <summary>
		/// Type of collision volume to be used by the camera.
		/// 
		/// See <see cref="SA1CamCollisionShape"/> for more information.
		/// </summary>
		public SA1CamCollisionShape CollisionShape { get; set; } = SA1CamCollisionShape.Sphere;

		/// <summary>
		/// Camera's Distance to the player.
		/// 
		/// Usage varies per camera type.
		/// </summary>
		public float CameraDistance { get; set; } = 0.0f;

		#endregion

		#region Constructors
		/// <summary>
		/// Default constructor for an <see cref="SA1CamObject"/>.
		/// </summary>
		public SA1CAMObject() { }

		/// <summary>
		/// Creates a new <see cref="SA1CamObject"/> using the provided data.
		/// </summary>
		/// <param name="mode">Camera Mode</param>
		/// <param name="priority">Camera's Priority</param>
		/// <param name="adjmode">Camera's Adjustment Mode</param>
		/// <param name="colmode">Camera's Collision Type</param>
		/// <param name="colangx">Collision Volume's X Angle</param>
		/// <param name="colangy">Collision Volume's Y Angle</param>
		/// <param name="colposx">Collision Volume's X Position</param>
		/// <param name="colposy">Collision Volume's Y Position</param>
		/// <param name="colposz">Collision Volume's Z Position</param>
		/// <param name="colsclx">Collision Volume's X Scale</param>
		/// <param name="colscly">Collision Volume's Y Scale</param>
		/// <param name="colsclz">Collision Volume's Z Scale</param>
		/// <param name="camangx">Camera's X Angle</param>
		/// <param name="camangy">Camera's Y Angle</param>
		/// <param name="camposx">Camera's X Position</param>
		/// <param name="camposy">Camera's Y Position</param>
		/// <param name="camposz">Camera's Z Position</param>
		/// <param name="camtgtx">Camera Target's X Position</param>
		/// <param name="camtgty">Camera Target's Y Position</param>
		/// <param name="camtgtz">Camera Target's Z Position</param>
		/// <param name="dist">Camera's Distance Value</param>
		public SA1CAMObject(SA1CamMode mode, byte priority, SA1CamAdjustMode adjmode, SA1CamCollisionShape colmode,
			int colangx, int colangy, float colposx, float colposy, float colposz, float colsclx, float colscly, float colsclz,
			int camangx, int camangy, float camposx, float camposy, float camposz, float camtgtx, float camtgty, float camtgtz,
			float dist)
		{
			Mode = mode;
			Priority = priority;
			AdjustMode = adjmode;
			CollisionShape = colmode;
			Collision = new Node(colposx, colposy, colposz, colangx, colangy, 0, colsclx, colscly, colsclz);
			CameraRotation = new RotationVector(camangx, camangy, 0);
			CameraPosition = new FloatVector(camposx, camposy, camposz);
			CameraTarget = new FloatVector(camtgtx, camtgty, camtgtz);
			CameraDistance = dist;
		}

		#endregion

		#region Functions
		/// <summary>
		/// <see cref="IBinarySerializable"/> method for reading <see cref="SA1CamObject"/>.
		/// </summary>
		/// <param name="endianBinaryReader"></param>
		public void Read(BinaryObjectReader endianBinaryReader)
		{
			Mode = endianBinaryReader.ReadEnum<SA1CamMode>();
			Priority = endianBinaryReader.ReadByte();
			AdjustMode = endianBinaryReader.ReadEnum<SA1CamAdjustMode>();
			CollisionShape = endianBinaryReader.ReadEnum<SA1CamCollisionShape>();

			Collision = new Node();
			Collision.Rotation = new RotationVector(endianBinaryReader.ReadInt16(), endianBinaryReader.ReadInt16(), 0);
			Collision.Position = endianBinaryReader.ReadObject<FloatVector>();
			Collision.Scale = endianBinaryReader.ReadObject<FloatVector>();

			CameraRotation = new RotationVector(endianBinaryReader.ReadInt16(), endianBinaryReader.ReadInt16(), 0);
			CameraTarget = endianBinaryReader.ReadObject<FloatVector>();
			CameraPosition = endianBinaryReader.ReadObject<FloatVector>();
			CameraDistance = endianBinaryReader.ReadSingle();
		}

		/// <summary>
		/// <see cref="IBinarySerializable"/> method for writing <see cref="SA1CamObject"/>.
		/// </summary>
		/// <param name="endianBinaryWriter"></param>
		public void Write(BinaryObjectWriter endianBinaryWriter)
		{
			endianBinaryWriter.WriteEnum(Mode);
			endianBinaryWriter.WriteByte((byte)Priority);
			endianBinaryWriter.WriteEnum(AdjustMode);
			endianBinaryWriter.WriteEnum(CollisionShape);

			endianBinaryWriter.WriteInt16(Collision.Rotation.X.ToInt16());
			endianBinaryWriter.WriteInt16(Collision.Rotation.Y.ToInt16());
			endianBinaryWriter.WriteObject(Collision.Position);
			endianBinaryWriter.WriteObject(Collision.Scale);

			endianBinaryWriter.WriteInt16(CameraRotation.X.ToInt16());
			endianBinaryWriter.WriteInt16(CameraRotation.Y.ToInt16());
			endianBinaryWriter.WriteObject(CameraTarget);
			endianBinaryWriter.WriteObject(CameraPosition);
			endianBinaryWriter.WriteSingle(CameraDistance);
		}

		public static SA1CamMode GetCamModeFromString(string val)
		{
			bool parsed = Enum.TryParse<SA1CamMode>(val, out SA1CamMode result);

			if (parsed)
				return result;
			else
			{
				Console.WriteLine($"Invalid Camera Mode: {val}, returning Follow Camera Mode.");
				return SA1CamMode.Follow;
			}
		}

		public static SA1CamAdjustMode GetAdjustModeFromString(string val)
		{
			bool parsed = Enum.TryParse<SA1CamAdjustMode>(val, out SA1CamAdjustMode result);

			if (parsed) 
				return result;
			else
			{
				Console.WriteLine($"Invalid Camera Adjust Mode: {val}, returning Relative3 Adjust Mode.");
				return SA1CamAdjustMode.Relative3;
			}
		}

		public static SA1CamCollisionShape GetCollisionShapeFromInt(int val)
		{
			return (SA1CamCollisionShape)val;
		}

		#endregion
		#endregion
	}
}
