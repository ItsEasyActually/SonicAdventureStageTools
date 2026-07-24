using Amicitia.IO.Binary;

namespace SAST.Lib.DataTypes
{
	public class Rotation : IBinarySerializable
	{
		#region Internal
		#region Variables
		/// <summary>
		/// Angle in BAMS.
		/// </summary>
		public int Angle { get; set; } = 0;

		/// <summary>
		/// The <see cref="Angle"/> in Degrees.
		/// </summary>
		public float Degrees { get { return AngleToDegrees(); } }

		/// <summary>
		/// The <see cref="Angle"/> in Radians.
		/// </summary>
		public float Radians { get { return AngleToRadians(); } }

		#endregion

		#region Constructors
		/// <summary>
		/// Default constructor.
		/// </summary>
		public Rotation() { }

		/// <summary>
		/// Creates a Rotation from an int.
		/// </summary>
		/// <param name="angle"></param>
		public Rotation(int angle)
		{
			Angle = angle;
		}

		/// <summary>
		/// Creates Rotation from a ushort, used when Short Rotations are used.
		/// </summary>
		/// <param name="angle"></param>
		public Rotation(ushort angle)
		{
			Angle = angle;
		}

		#endregion

		#region Functions
		/// <summary>
		/// Converts the <see cref="Angle"/> to Degrees.
		/// </summary>
		private float AngleToDegrees()
		{
			return BAMSToDegrees(Angle);
		}

		/// <summary>
		/// Converts the <see cref="Angle"/> to Radians.
		/// </summary>
		private float AngleToRadians()
		{
			return BAMSToRadians(Angle);
		}

		/// <summary>
		/// Angle (in Degrees) is used to set the <see cref="Rotation"/>'s angle.
		/// </summary>
		/// <param name="angle"></param>
		public void FromDegrees(float angle)
		{
			Angle = DegreesToBAMS(angle);
		}

		/// <summary>
		/// Angle (in Radians) is used to set the <see cref="Rotation"/>'s angle.
		/// </summary>
		/// <param name="angle"></param>
		public void FromRadians(float angle)
		{
			Angle = RadiansToBAMS(angle);
		}

		/// <summary>
		/// Returns the Angle as a string with the Degrees and Radians conversions in paranethesis
		/// </summary>
		/// <returns>[Angle] (Deg: [Degrees Angle], Rad: [Radians Angle])</returns>
		public override string ToString()
		{
			return $"{Angle} (DEG: {Degrees}, RAD: {Radians})";
		}

		/// <summary>
		/// Returns the Angle as a <see cref="short"/>.
		/// </summary>
		/// <returns></returns>
		public short ToInt16() { return (short)Angle; }

		/// <summary>
		/// Returns the Angle as a <see cref="ushort"/>.
		/// </summary>
		/// <returns></returns>
		public ushort ToUInt16()
		{
			if (int.IsNegative(Angle))
				return (ushort)(Angle >> 16 & 0xFFFF);
			else
				return (ushort)Angle;
		}

		/// <summary>
		/// <see cref="IBinarySerializable"/> method for reading <see cref="Rotation"/>.
		/// </summary>
		/// <param name="endianBinaryReader"></param>
		public void Read(BinaryObjectReader endianBinaryReader)
		{
			Angle = endianBinaryReader.ReadInt32();
		}

		/// <summary>
		/// <see cref="IBinarySerializable"/> method for writing <see cref="Rotation"/>.
		/// </summary>
		/// <param name="endianBinaryReader"></param>
		public void Write(BinaryObjectWriter endianBinaryWriter)
		{
			endianBinaryWriter.WriteInt32(Angle);
		}
		#endregion

		#endregion

		#region Static 
		#region Variables
		private static readonly float BAMSConverter = 65536.0f;
		private static readonly float DegreesConverter = 360.0f;
		private static readonly float RadiansConverter = 2 * MathF.PI;
		#endregion

		#region Functions
		#region Conversion
		/// <summary>
		/// Converts a BAMS Angle to a Degrees Angle
		/// </summary>
		/// <returns>Angle in Degrees</returns>
		public static float BAMSToDegrees(int value) { return value / BAMSConverter * DegreesConverter; }

		/// <summary>
		/// Converts a Degrees Angle to a BAMS Angle
		/// </summary>
		/// <returns>Angle in BAMS</returns>
		public static int DegreesToBAMS(float value) { return (int)(value / DegreesConverter * BAMSConverter); }

		/// <summary>
		/// Converts a BAMs Angle to a Radians Angle
		/// </summary>
		/// <returns>Angle in Radians</returns>
		public static float BAMSToRadians(int value) { return value / BAMSConverter * RadiansConverter; }

		/// <summary>
		/// Converts a Radians Angle to a BAMS Angle
		/// </summary>
		/// <returns>Angle in BAMS</returns>
		public static int RadiansToBAMS(float value) { return (int)(value / RadiansConverter * BAMSConverter); }

		#endregion

		#region Creation
		/// <summary>
		/// Creates a new <see cref="Rotation"/> from a Degree angle.
		/// </summary>
		/// <param name="angle"></param>
		/// <returns></returns>
		public static Rotation CreateRotationFromDegrees(float angle)
		{
			return new Rotation(DegreesToBAMS(angle));
		}

		/// <summary>
		/// Creates a new <see cref="Rotation"/> from a Radians angle.
		/// </summary>
		/// <param name="angle"></param>
		/// <returns></returns>
		public static Rotation CreateRotationFromRadians(float angle)
		{
			return new Rotation(RadiansToBAMS(angle));
		}

		#endregion

		#endregion

		#endregion
	}
}
