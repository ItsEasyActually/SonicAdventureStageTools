using Amicitia.IO.Binary;

namespace SAST.Lib.DataTypes
{
	/// <summary>
	/// Stores a public accessible <see cref="FloatVector"/> for Position, <see cref="RotationVector"/> for Rotation, and a <see cref="FloatVector"/> for Scale.
	/// </summary>
	public class Node : IBinarySerializable
	{
		#region Internal
		#region Variables
		/// <summary>
		/// Position of the <see cref="Node"/> in 3D Space.
		/// </summary>
		public FloatVector Position { get; set; } = new FloatVector();

		/// <summary>
		/// Rotation of the <see cref="Node"/>.
		/// </summary>
		public RotationVector Rotation { get; set; } = new RotationVector();

		/// <summary>
		/// Scale of the <see cref="Node"/>.
		/// </summary>
		public FloatVector Scale { get; set; } = new FloatVector();

		#endregion

		#region Constructors
		/// <summary>
		/// Default constructor.
		/// 
		/// Creates a new <see cref="Node"/> with a default <see cref="FloatVector"/> for <see cref="Position"/> and <see cref="Scale"/> and a default <see cref="RotationVector"/> for <see cref="Rotation"/>.
		/// </summary>
		public Node()
		{
			Position = new FloatVector();
			Rotation = new RotationVector();
			Scale = new FloatVector();
		}

		/// <summary>
		/// Creates a new <see cref="Node"/> using supplied <see cref="FloatVector"/>s and <see cref="RotationVector"/>.
		/// </summary>
		/// <param name="pos"></param>
		/// <param name="rot"></param>
		/// <param name="scl"></param>
		public Node(FloatVector pos, RotationVector rot, FloatVector scl)
		{
			Position = pos;
			Rotation = rot;
			Scale = scl;
		}

		/// <summary>
		/// Creates a new <see cref="Node"/> using the supplied values.
		/// </summary>
		/// <param name="posx">X Position</param>
		/// <param name="posy">Y Position</param>
		/// <param name="posz">Z Position</param>
		/// <param name="angx">X Angle</param>
		/// <param name="angy">Y Angle</param>
		/// <param name="angz">Z Angle</param>
		/// <param name="sclx">X Scale</param>
		/// <param name="scly">Y Scale</param>
		/// <param name="sclz">Z Scale</param>
		public Node(float posx, float posy, float posz,
			int angx, int angy, int angz,
			float sclx, float scly, float sclz)
		{
			Position = new FloatVector(posx, posy, posz);
			Rotation = new RotationVector(angx, angy, angz);
			Scale = new FloatVector(sclx, scly, sclz);
		}

		#endregion

		#region Functions
		/// <summary>
		/// <see cref="IBinarySerializable"/> method for reading <see cref="Node"/>.
		/// </summary>
		/// <param name="endianBinaryReader"></param>
		public void Read(BinaryObjectReader endianBinaryReader)
		{
			Position = endianBinaryReader.ReadObject<FloatVector>();
			Rotation = endianBinaryReader.ReadObject<RotationVector>();
			Scale = endianBinaryReader.ReadObject<FloatVector>();
		}

		/// <summary>
		/// <see cref="IBinarySerializable"/> method for writing <see cref="Node"/>.
		/// </summary>
		/// <param name="endianBinaryWriter"></param>
		public void Write(BinaryObjectWriter endianBinaryWriter)
		{
			endianBinaryWriter.WriteObject(Position);
			endianBinaryWriter.WriteObject(Rotation);
			endianBinaryWriter.WriteObject(Scale);
		}

		/// <summary>
		/// Checks if the <see cref="Node"/> is equal to a new <see cref="Node"/>.
		/// </summary>
		/// <returns>True when Node is new, otherwise False.</returns>
		public bool IsEmpty()
		{
			if (Position.IsEmpty() && Scale.IsEmpty())
				return true;
			else
				return false;
		}

		#endregion
		#endregion
	}
}
