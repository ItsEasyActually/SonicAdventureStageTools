using Kermalis.EndianBinaryIO;
using SAST.Lib.DataTypes;
using SAST.Lib.Extensions;
using System.Security.Cryptography;

namespace SAST.Lib.SET
{
	/// <summary>
	/// Represents a placeable object within a stage, used by both SA1 and SA2.
	/// </summary>
	public class SETObject : IBinarySerializable
	{
		#region Enum
		/// <summary>
		/// Flags used by a <see cref="SETObject"/> in its 
		/// </summary>
		[Flags]
		public enum SetFlags
		{
			/// <summary>
			/// SADX - Sets clip level the lowest setting (highest distance from player).
			/// SA2 - "Substansive" or Primary Set File flag.
			/// </summary>
			NoFlags = 0,

			/// <summary>
			/// SADX - Sets the clip level to the medium setting.
			/// SA2 - No effect.
			/// </summary>
			Flag1 = 1,

			/// <summary>
			/// SADX - Sets the clip level to the highest setting (lowest distance from player).
			/// SA2 - No effect.
			/// </summary>
			Flag2 = 2,

			/// <summary>
			/// SADX - No effect.
			/// SA2 - "Unsubstansive" or Decoration Set File flag.
			/// </summary>
			Flag4 = 8,
		}
		#endregion

		#region Internal
		#region Variables
		private ushort objectID = 0;

		/// <summary>
		/// Object ID, Corresponds to the Object List for the specified level.
		/// </summary>
		public int ObjectID 
		{ 
			get {  return objectID; }
			set { objectID = (ushort)(value & 0xFFF); }
		}

		private byte flags = 0;

		/// <summary>
		/// Clip Distance, <see cref="SetFlags"/>
		/// </summary>
		public SetFlags Flags 
		{ 
			get { return (SetFlags)flags; } 
			set { flags = (byte)value; }
		}

		/// <summary>
		/// Stores the Position, Rotation, and Scale values from the set file.
		/// 
		/// These properties can be used in varying ways by the underlying object code from the game. These are not indicative of what the values are always used for.
		/// </summary>
		public Node Node { get; set; } = new Node();

		#endregion

		#region Constructors
		public SETObject() { }

		public SETObject(int id, int flags,
			float xpos, float ypos, float zpos,
			int xang, int yang, int zang,
			float xscl, float yscl, float zscl)
		{
			ObjectID = id;
			Flags = (SetFlags)flags;
			Node = new Node(xpos, ypos, zpos, xang, yang, zang, xscl, yscl, zscl);
		}

		#endregion

		#region Functions
		/// <summary>
		/// <see cref="IBinarySerializable"/> method for reading <see cref="SETObject"/>.
		/// </summary>
		/// <param name="endianBinaryReader"></param>
		public void Read(EndianBinaryReader endianBinaryReader)
		{
			ushort bits = endianBinaryReader.ReadUInt16();
			ObjectID = bits;
			Flags = (SetFlags)((bits >> 12) & 0xF);
			Node.Rotation = endianBinaryReader.ReadShortRotationVector();
			Node.Position = endianBinaryReader.ReadObject<FloatVector>();
			Node.Scale = endianBinaryReader.ReadObject<FloatVector>();
		}

		/// <summary>
		/// <see cref="IBinarySerializable"/> method for writing <see cref="SetObject"/>.
		/// </summary>
		/// <param name="endianBinaryWriter"></param>
		public void Write(EndianBinaryWriter endianBinaryWriter)
		{
			ushort bits = (ushort)(ObjectID | ((int)Flags << 12));
			endianBinaryWriter.WriteUInt16(bits);
			endianBinaryWriter.WriteShortRotationVector(Node.Rotation);
			endianBinaryWriter.WriteObject(Node.Position);
			endianBinaryWriter.WriteObject(Node.Scale);
		}

		/// <summary>
		/// Returns a correct three axis rotation
		/// </summary>
		/// <param name="order"></param>
		/// <returns></returns>
		public RotationVector GetCorrectedRotationOrderForBlender(string order)
		{
			RotationVector vec = Node.Rotation;

			if (Enum.TryParse(order, out RotationVector.AxisOrder axisOrder))
			{
				if (axisOrder != RotationVector.AxisOrder.XYZ)
					vec.SwapAxisOrder(axisOrder, RotationVector.AxisOrder.XYZ);
			}

			vec.SwapOrientation();

			return vec;
		}

		public void SetObjectFlags(int val) { flags = (byte)val; }

		#endregion
		#endregion

		#region Static
		public static readonly int Size = 40;

		#endregion
	}
}
